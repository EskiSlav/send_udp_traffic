import os
import re
import socket
from datetime import datetime
from sys import argv
from time import sleep
from .exceptions import IPError, PortError

filename = "input.txt"




def check_ip(ip):
    reg = re.compile(r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b')
    if reg.fullmatch(ip) is None:
        raise IPError("Wrong IP")
    return True


def check_port(port):
    if not (res:=port > 0 and port < 65536):
        raise PortError("Port should be in range: 1-65535")
    return res


def check_file(filename):
    if not (res:=os.path.exists(filename)):
        raise FileNotFoundError
    return res


def check_argv():
    global filename

    if len(argv) > 4:
        exit()
        
    if '-h' in argv or '--help' in argv:
        print(f"USAGE: python3 {__file__.split('/')[-1]} IP PORT [filename..]")
        exit()

    try:
        ip = argv[1]
        port = int(argv[2])
    except IndexError:
        print("Either IP or Port not specified. ")
        print(f"USAGE: python3 {__file__.split('/')[-1]} IP PORT [filename..]")
        exit()

    try:
        filename = argv[3]
    except IndexError:
        print(f"File is not specified. Using {filename}.")

    try:
        check_ip(ip) 
        check_port(port)
        check_file(filename)
    except IPError as e:
        print(e)
        exit()
    except PortError as e: 
        print(e)
        exit()
        
        
def send_message(message, ip, port):
    byte_message = bytes(datetime.now().strftime("%m/%d/%Y, %H:%M:%S ") + message, "utf-8")
    opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    opened_socket.sendto(byte_message, (ip, port))
    print("Sent:", byte_message.decode())


def main():
    f = open(filename, 'r')
    lines = f.readlines()
    check_argv()
    print(f"Using filename {filename}")
    i = 0
    while True:
        for line in lines:
            send_message(f"{line[:-1]}", argv[1], int(argv[2]))
            sleep(1)
            i += 1
        sleep(5)


if __name__ == '__main__':
    main()
