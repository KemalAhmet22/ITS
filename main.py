import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
class UDPlistener:
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)
        Parser.Message_Parser(data)

class Parser:
    def Message_Parser():
        Nmea_parse = Message.split(",")

        for element in Nmea_parse:
            print(element)