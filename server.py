import socket

def get_server_address():
    """Detects the server's IP address automatically."""
    try:
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.4.4", 80))
        ip_address = temp_socket.getsockname()[0]
        temp_socket.close()
        return ip_address
    except Exception as e:
        print(f"Error getting server address: {e}")
        return "127.0.0.1"

def start_server(port):
    """Starts the server and waits for client connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = get_server_address()

    try:
        server_socket.bind((server_address, port))
        server_socket.listen(5)
        print(f"Server running on {server_address}:{port}")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connection from {addr}")

            with conn:
                while True:
                    data = conn.recv(1024).decode()
                    if not data:
                        break
                    if data.lower() == "quit":
                        print("Client requested to quit. Closing connection.")
                        conn.close()
                        return
                    print(f"Client : {data}")
                    response = input(f"Type Response: ")
                    conn.send(response.encode())
    except Exception as e:
       print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    port = 40000  # Set your desired port here
    start_server(port)

