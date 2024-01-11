import socket

class ServerConnector:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect_to_server(self):
        try:
            # Attempt to connect to the server
            socket.create_connection((self.host, self.port))
            print("Connection successful!")
        except socket.error as se:
            print(f"Socket error: {se}")
        except ConnectionError as ce:
            print(f"Connection error: {ce}")

# Example usage:
server_connector = ServerConnector('example.com', 80)
server_connector.connect_to_server()
