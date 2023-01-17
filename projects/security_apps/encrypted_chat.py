import socket
import threading

import rsa # pip install rsa

# Generate my public key pair
# Generaly we generate this and store in a secure location (temporary keys)

public_key, private_key = rsa.newkeys(1024)
public_partner = None

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

    # send : "save_pkcs1("PEM")" is packaging the key as bytes, foirmat PEM
    client.send(public_key.save_pkcs1("PEM"))
    # receive
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("172.22.32.1", 9999))

    # receive
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    # send : "save_pkcs1("PEM")" is packaging the key as bytes, foirmat PEM
    client.send(public_key.save_pkcs1("PEM"))

else:
    exit()


def sending_messages(c):
    while True:
        message = input("")
        # encrypt the messages before sending with the public key of the partner
        c.send(rsa.encrypt(message.encode(), public_partner))
        print("You " + message)

def receiving_messages(c):
    while True:
        # decrypt the messages
        print("Partner: " + rsa.decrypt(c.recv(1024), private_key).decode())

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()


    
