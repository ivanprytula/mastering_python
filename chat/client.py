import logging
import socket
import threading

from .helpers import find_free_port, get_host

logger = logging.getLogger(__name__)

HOST = get_host()
PORT = find_free_port()


def listen_for_messages_from_server(client):
    while True:
        message = client.recv(2048).decode("utf-8")

        if message:
            username = message.split("~")[0]
            content = message.split("~")[1]
            print(f"[{username}] {content}")
        else:
            logger.warning("Message received from server is empty.")


def send_message_to_server(client):
    while True:
        message = input("Enter message: ")
        if message:
            client.sendall(message.encode())
        else:
            logger.warning("Empty message")


def communicate_to_server(client: socket.socket):
    username = input("Enter username: ")
    if username:
        client.sendall(username.encode())
    else:
        logger.warning("Username cannot be empty.")
        exit(0)

    threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()

    send_message_to_server(client)


def main():
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"Client is connected to {HOST} {PORT}")
    except socket.error as error_msg:
        logger.warning(
            f"Unable to connect to server host {HOST} and port {PORT}. Reason: "
            f"{error_msg}"
        )

    communicate_to_server(client)


if __name__ == "__main__":
    main()
