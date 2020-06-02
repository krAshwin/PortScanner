#!/usr/bin/env python3

from threading import Thread
import socket

def check(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ('127.0.0.1', port)
    res = sock.connect_ex(location)

    if res == 0:
        print("Port {0} is open!".format(port))
    else:
        print("Port {0} is not open!".format(port))

    sock.close()


def main():

    ports = (21,22,80,443)
    for port in ports:
        thread  = Thread(target=check, args=(port,))
        thread.start()


if __name__ == '__main__':
    main()