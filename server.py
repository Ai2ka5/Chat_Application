import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []


def listen_for_messages(client, username):
    while 1:

        message = client.recv(2048).decode('utf8')
        if message != "":
            final_msg = username + '~' + message
            send_message_to_all(final_msg)
        else:
            print(f"The message send from client {username} is empty")


def send_message_to_all(message):
    pass


def client_handler(client):
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != "":
            active_clients.append((username, client))

        else:
            print("Client username is empty")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    server.listen(LISTENER_LIMIT)

    while 1:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client,)).start()


if __name__ == "__main__":
    main()
