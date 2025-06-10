import base64

def main():
    try:
        # Read the input file
        with open('input.txt', 'rb') as file:
            data = file.read().strip()

        decode_bytes = base64.b64decode(data)
        decode_string = decode_bytes.decode('utf-8')
        
        print(f"Decoded string: {decode_string}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()
    