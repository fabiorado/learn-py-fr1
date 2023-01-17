import socket
import threading

'''
Notes:
We need 1 cliente and 1 host minimum. Someone needs to host.


'''


# Interface com o usuario
choice = input("Do you want to host (1) or connect (2): ")

if choice == "1":
    # Internet socket = AF_INET
    # TCP = SOCK_STREAM / UDP = SOCK_DGRAM
    # Server feito somente para aceitar a connexão
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind
    # Take the IPv4 from "ipconfig" of the "Ethernet adapter"
    server.bind(("172.22.32.1", 9999))
    server.listen()

    # Only 1 connection
    # When a client connects, we want to accept the connection
    client, _ = server.accept()
elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("172.22.32.1", 9999))
else:
    exit()


def sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("You " + message)

def receiving_messages(c):
    while True:
        message = input("")
        print("Partner: " + c.recv(1024).decode())

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()


    
