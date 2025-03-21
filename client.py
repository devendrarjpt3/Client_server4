import socket

def start_client(server_name, port):
    """Connects to the server and sends messages."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_name, port))
        print(f"Connected to {server_name}:{port}")
          while True:
            message = input("Enter message (type 'quit' to exit): ")
            client_socket.sendall(message.encode())
             response =client_socket.recv(1024).decode()
            print (f"Server response: {response}")

            if message.lower() == "quit":
                print("Exiting client.")
                break
               
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_name = "cclinux3"
    port = 40000  # Same port as the server
    start_client(server_name, port)
