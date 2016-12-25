import socket
import sys
import time
import select
import os
import string
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8004)
client_socket.connect(server_address)

running = 1
input_object = [0,client_socket]

while running:
    inputready, outputready, exceptready = select.select(input_object, [], [])

    for i in inputready:
        print "hehe"
        fileName = sys.stdin.readline()

        fileName = fileName.strip('\n')

        request_header = fileName.split()[0] + ' '+'/'+fileName.split()[1]+' HTTP/1.1\r\nHost: localhost\r\n\r\n'

        client_socket.send(request_header)
        #print fileName
        response = ''
        recv = client_socket.recv(1024)
        print recv

client_socket.close()









