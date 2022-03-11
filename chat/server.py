import logging
import socket
import threading

from .helpers import find_free_port, get_host

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

HOST = get_host()
PORT = find_free_port()
LISTENER_LIMIT = 5

active_clients = []


def listen_for_messages(client, username: str) -> None:
    """Keeps listening for messages from the connected clients.

    In case if it received a message, it will call the send_message_to_all()
    to send the received message to all currently connected clients.

    :param client:
    :param username:
    :return: None
    """
    while True:
        message = client.recv(2048).decode("utf-8")
        if message != "":
            final_msg = f"{username} ~ {message}"
            send_messages_to_all(final_msg)
        else:
            logger.warning(f"The message send from client {username} is empty")


def send_message_to_client(client, message: str) -> None:
    """Sends message to a single client."""
    client.sendall(message.encode())


def send_messages_to_all(message: str) -> None:
    """Sends a message to all connected clients."""
    for user in active_clients:
        send_message_to_client(user[1], message)


def client_handler(client: socket.socket) -> None:
    """
    Listens for client message that contains the username.

    :param client:
    :return: None
    """

    while True:

        username = client.recv(2048).decode("utf-8")
        if username != "":
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            logger.warning("Client username is empty")

    threading.Thread(
        target=listen_for_messages,
        args=(
            client,
            username,
        ),
    ).start()


def main() -> None:
    """
    1. Creates a socket object (that acts as the server)
    2. Binds IP/HOST and Port to the server
    3. Set up listener limit
    4. Accepts any upcoming connection from clients
    5. Calls the client handler for any new connected client

    :return: None
    """
    # 1:
    # AF_INET -> IPv4 addresses; SOCK_STREAM -> use TCP packets for communication
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    try:
        # 2: Provides the server w/ an address
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
        logger.info(f"Running the server on {HOST} {PORT}")
    except socket.error as error_msg:
        logger.warning(
            f"Unable to bind to host {HOST} and port {PORT}. Reason: {error_msg}"
        )

    # 3: Set server limit
    server.listen(LISTENER_LIMIT)

    # 4:
    while True:
        client, address = server.accept()
        logger.info(f"Successfully connected to client {address[0]} {address[1]}")
        print(f"Successfully connected to client {address[0]} {address[1]}")
        threading.Thread(target=client_handler, args=(client,)).start()


if __name__ == "__main__":
    main()
