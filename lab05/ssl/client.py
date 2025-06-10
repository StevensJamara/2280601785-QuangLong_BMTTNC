import socket
import ssl
import threading

server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
    except:
        pass
    finally:
        ssl_socket.close()
        print(f"Closing connection to {ssl_socket.getpeername()}")
    
#Generate a client socket and wrap it with SSL context    
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False

#Config SSL's connection
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_socket.connect(server_address)

# Start a thread to receive data from the server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Send data to the server
while True:
    try:
        message = input("Enter message to send (or 'exit' to quit): ")
        ssl_socket.sendall(message.encode('utf-8'))
    except KeyboardInterrupt:
        pass
    finally:
        ssl_socket.close()