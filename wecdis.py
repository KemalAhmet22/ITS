import socket
from textwrap import wrap
class Read:
    def __init__(self):
        self.my_obj = VTG()

    def Readmeth(self):

        localIP = "127.0.0.1"
        localPort = 5005
        bufferSize = 1024
        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        sock.bind((localIP, localPort))

        while True:
            bytesAddressPair = sock.recvfrom(bufferSize)
            message = bytesAddressPair[0]
            sens_mesaj = message.split(b',')
            sens_mesaj2= sens_mesaj[-1].split(b'*')    # Mode indicator EKLENECEK
            outputstring = message.hex()
            if sens_mesaj[0].__contains__(b'VTG'):
                obj_2.updateVTG(sens_mesaj,sens_mesaj2)
                check = obj_3.checksum(outputstring)
                cexk2 = str(sens_mesaj2[1])
                if cexk2.__contains__(check):  #contains dışı
                    print("Checksum Doğru")


class VTG:  #deneme
    def updateVTG(self, msg,msg2):
        print("Course over Ground True =", msg[1],msg[2])

        print("Course over Ground MAG =", msg[3],msg[4])

        print("Speed over Ground  Nautical=", msg[5],msg[6])

        print("Speed over Ground  kilometer=", msg[7], msg[8])

        print("Checksum = ",msg2[1])



def xor_strings(str1, str2):
    result = ""
    for i in range(len(str2)):
        int1 = int(str1[i], 16)
        int2 = int(str2[i], 16)

        xor_results = int1 ^ int2

        result += hex(xor_results)[2:]

    return result

class ChecksumCalc:

    def checksum(self,outputstring):
        hexlist = wrap(outputstring,2)
        for i in range(3):
            del hexlist[len(hexlist)-1]
        del hexlist[0]
        checksum2 = "00"
        for i in range(len(hexlist)):
            checksum2 = xor_strings(checksum2,hexlist[i])
        print(checksum2)
        return checksum2

obj_1 = Read()
obj_2 = VTG()
obj_3 = ChecksumCalc()
obj_1.Readmeth()
obj_3.checksum()



