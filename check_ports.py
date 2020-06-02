#!/usr/bin/env python3

from threading import Thread
import socket

def check(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ('127.0.0.1', port)
    res = sock.connect_ex(location)

    if res == 0:
        print("{0:5d}: Port OPEN!".format(port))
    else:
        print("{0:5d}: Port CLOSED!".format(port))

    sock.close()


def main():

    ports = (21,22,80,443)
    
    print("Port Status!\n======================")
    for port in ports:

        # daemon threads terminate as the program ends
        thread  = Thread(target=check, args=(port,), daemon= True)
        thread.start()
    
    # wait until thread executes completely
    thread.join()

if __name__ == '__main__':
    main()