import socket
import hashlib

def connect():
    # create an INET, STREAMing socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on whichever port the server is running on
    client.connect(("docker.hackthebox.eu",39659))
    return client

def get_request():
    client = connect()
    client.sendall(b'GET / HTTP/1.0\r\n\r\n')
    resp = client.recv(4096)
    print(resp)
    client.close()

#def post_request():

def main():
    connect()
    get_request()

main()
