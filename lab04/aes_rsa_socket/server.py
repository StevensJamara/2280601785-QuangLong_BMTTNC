from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

# Generate RSA key pair
server_key = RSA.generate(2048)

# List of connected clients
clients = []

# Function to encrypt message
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Function to decrypt message
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Function to handle client connection
def handle_client(client_socket, client_address):
    print(f"Client {client_address} connected.")


    # Send public key to client
    client_socket.send(server_key.publickey().export_key(format='PEM'))
    
    client_received_key = RSA.import_key(client_socket.recv(2048))
    
    # Generate AES key
    aes_key = get_random_bytes(16)
    
    cipher_rsa = PKCS1_OAEP.new(client_received_key)
    encrypt_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypt_aes_key)
    
    clients.append((client_socket, aes_key))
    
    while True:
        encrypt_message = client_socket.recv(1024)
        decrypt_message = decrypt_message(aes_key, encrypt_message)
        print(f"Received from {client_address}: {decrypt_message}")
        
        for client, key in clients:
            if client != client_socket:
                encrypted = encrypt_message(key, decrypt_message)
                client.send(encrypted)
            if decrypt_message == 'exit':
                print(f"Client {client_address} disconnected.")
                break
        
        clients.remove((client_socket, aes_key))
        client_socket.close()
        print(f"Client {client_address} disconnected.")
        
        while True:
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                client_thread.start()            