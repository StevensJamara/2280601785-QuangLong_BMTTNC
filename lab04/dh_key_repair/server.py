from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_dh_paramaters():
    paramaters = dh.generate_parameters(generator=2, key_size=2048)
    return paramaters

def generate_server_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key

def main():
    # Generate Diffie-Hellman parameters
    parameters = generate_dh_paramaters()
    private_key, public_key = generate_server_key_pair(parameters)
    
    with open("dh_private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
        
if __name__ == "__main__":
    main()