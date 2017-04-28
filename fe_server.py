import argparse
import time
import struct
import thread
import md5
import os
import binascii
import socket
import sys
import random
import collections
from socket import error as socket_error

def on_accept_client(client_sock, address):
    while True:

        try:
            msg = client_sock.recv(1024)
            print msg

            client_sock.send("ok")

            if msg is "close":
                print "closing connection with", address
                client_sock.close()

        except socket_error as s_error:
            return 

def main():

    parser = argparse.ArgumentParser(description='Friend Explorer Socket Server')
    parser.add_argument('-p','--port', help='Socket Port', required=True)

    args = vars(parser.parse_args())

    s_port = args['port']

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = int(s_port)

    sock.bind((host, port))

    print "looking for clients"
    sock.listen(5)

    while True:
        (conn, addr) = sock.accept()
        print "found client:", addr
        thread.start_new_thread(on_accept_client, (conn, addr))

    sock.close()
    
    
if __name__ == "__main__":
    main()
