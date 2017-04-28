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

def main():
    
    # parse all the arguments to the client 
    parser = argparse.ArgumentParser(description='Friend Explorer Socket Server')
    parser.add_argument('-p','--port', help='Socket Port', required=True)
    parser.add_argument('-d','--dest', help='Socket Dest', required=True)

    args = vars(parser.parse_args())

    s_port = args['port']
    dest = args['dest']

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(s_port)

    sock.connect((dest, port))

    try:
        msg = "hello"
        sock.send(msg)

        amount_received = 0
        amount_expected = 1

        while amount_received < amount_expected:
            result_data = sock.recv(1024)
            amount_received += len(result_data)

            sock.send("close")

    finally:
        sock.close()
    

if __name__ == "__main__":
    main()
