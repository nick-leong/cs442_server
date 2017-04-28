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

global connected

def on_accept_client(client_sock, address):
    global connected

    while True:

        try:
            msg = client_sock.recv(1024)

            if msg == None or msg == '':
                pass
            else:
                print "MSG:", msg

                if msg[0] == 'a': #amount of users connected
                    client_sock.send(str(connected))

                elif msg == "close":
                    connected=connected-1
                    print "closing connection with", address
                    client_sock.close()

                else:
                    client_sock.send("err")

        except socket_error as s_error:
            print "lost connection with:", address
            return 

def main():
    global connected
    connected = 0

    parser = argparse.ArgumentParser(description='Friend Explorer Socket Server')
    parser.add_argument('-p','--port', help='Socket Port', required=True)

    args = vars(parser.parse_args())

    s_port = args['port']

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    port = int(s_port)

    print "Host:", host, " | Port:", port

    sock.bind((host, port))

    print "looking for clients"
    sock.listen(5)

    while True:
        (conn, addr) = sock.accept()
        connected=connected+1
        print "found client:", addr
        thread.start_new_thread(on_accept_client, (conn, addr))

    sock.close()
    
    
if __name__ == "__main__":
    main()
