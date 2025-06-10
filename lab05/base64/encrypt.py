import base64

def main():
    # Get the input string from the user
    input_string = input("Enter a string to encode in Base64: ")

    # Encode the string in Base64
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))

    # Convert bytes to string
    encoded_string = encoded_bytes.decode('utf-8')

    with open('encoded.txt', 'w') as file:
        # Write the encoded string to a file
        file.write(encoded_string)
        
    print(f"Encoded string: {encoded_string}")

if __name__ == "__main__":
    main()