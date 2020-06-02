#!/usr/bin/env python3

import sys
import socket

class Server():
    def __init__(self):
        super().__init__()

    def startServer(self,host,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind((host, port))
            print("Socket Binded!")
        except socket.error as e:
            print("Bind Error:",e)
            sys.exit()
        sock.listen()
        connection, addr = sock.accept()

        print("Connection established on {0}:{1}".format(host,port))

serve = Server()
serve.startServer('127.0.0.1',443)