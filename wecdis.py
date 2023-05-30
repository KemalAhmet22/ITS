import socket
from textwrap import wrap
class Read:
    def __init__(self):
        self.my_obj = Identifier()

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
                obj_2.updateVTG(sens_mesaj,sens_mesaj2)       #Log a yazdırma
                if str(sens_mesaj2[1]).__contains__(obj_3.checksum(outputstring)):  #contains dışı  Checksum
                    print("Checksum Doğru")

            elif sens_mesaj[0].__contains__(b'RMC'):
                obj_2.updateRMC(sens_mesaj, sens_mesaj2)  # Log a yazdırma
                if str(sens_mesaj2[1]).__contains__(obj_3.checksum(outputstring)):  # contains dışı  Checksum
                    print("Checksum Doğru")

            elif sens_mesaj[0].__contains__(b'GLL'):
                obj_2.updateGLL(sens_mesaj, sens_mesaj2)  # Log a yazdırma
                if str(sens_mesaj2[1]).__contains__(obj_3.checksum(outputstring)):  # contains dışı  Checksum     Büyük harf küçük harf eşitiği sıkıntı
                    print("Checksum Doğru")

            elif sens_mesaj[0].__contains__(b'GGA'):
                obj_2.updateGGA(sens_mesaj, sens_mesaj2)  # Log a yazdırma
                if str(sens_mesaj2[1]).__contains__(obj_3.checksum(outputstring)):  # contains dışı  Checksum     Büyük harf küçük harf eşitiği sıkıntı
                    print("Checksum Doğru")

            elif sens_mesaj[0].__contains__(b'VBW'):
                obj_2.updateVBW(sens_mesaj, sens_mesaj2)  # Log a yazdırma
                if str(sens_mesaj2[1]).__contains__(obj_3.checksum(outputstring)):  # contains dışı  Checksum     Büyük harf küçük harf eşitiği sıkıntı
                    print("Checksum Doğru")

class Identifier:
    def updateVTG(self, msg,msg2):
        print("                 VTG MESAJI                    ")
        print("Course over Ground True =", msg[1],msg[2])
        print("Course over Ground MAG =", msg[3],msg[4])
        print("Speed over Ground  Nautical=", msg[5],msg[6])
        print("Speed over Ground  kilometer=", msg[7], msg[8])
        print("Checksum = ",msg2[1])

    def updateRMC(self,msg, msg2):
        print("                 RMC MESAJI                    ")
        print("Saat ve validity =", msg[1], msg[2])
        print("latitude =", msg[3], msg[4])
        print("longitude =", msg[5], msg[6])
        print("SOG/ COG", msg[7], msg[8])
        print("date",msg[9])
        print("Checksum = ", msg2[1])

    def updateGLL(self,msg,msg2):
        print("                 GLL MESAJI                    ")
        print("latitude =", msg[1], msg[2])
        print("longitude =", msg[3], msg[4])
        print("UTC saat", msg[5])
        print("status", msg[6])
        print("mode indicator", msg[7])
        print("Checksum = ", msg2[1])

    def updateGGA(self,msg,msg2):
        print("                 GGA MESAJI                    ")
        print("UTC saat", msg[1])
        print("latitude =", msg[2], msg[3])
        print("longitude =", msg[4], msg[5])
        print("Qualiity indicator", msg[6])
        print("number of satalites", msg[7])
        print("HDOP", msg[8])
        print("mean sea level ", msg[9],msg[10])
        print("WGS84 ", msg[11], msg[12])
        print("Age of Diff data", msg[13])
        print("Differential ref station ID", msg[14])
        print("Checksum = ", msg2[1])

    def updateVBW(self,msg,msg2):
        print("                 VBW MESAJI                    ")
        print("Longitudinal water speed", msg[1])
        print("Transverse water speed =", msg[2])
        print("status =", msg[3])
        print("Longitudinal ground speed", msg[4])
        print("Transverse ground speed", msg[5])
        print("status", msg[6])
        print("stern transverse water speed ", msg[7])
        print("status", msg[8])
        print("stern Transverse ground speed", msg[9])
        print("status", msg[10])
        print("Checksum = ", msg2[1])

class ChecksumCalc:
    def xor_strings(self, str1, str2):
        result = ""
        for i in range(len(str2)):
            int1 = int(str1[i], 16)
            int2 = int(str2[i], 16)

            xor_results = int1 ^ int2

            result += hex(xor_results)[2:]

        return result
    def checksum(self,outputstring):
        hexlist = wrap(outputstring,2)
        for i in range(3):
            del hexlist[len(hexlist)-1]
        del hexlist[0]
        checksum2 = "00"
        for i in range(len(hexlist)):
            checksum2 = self.xor_strings(checksum2,hexlist[i])
        print(checksum2)
        return checksum2

obj_1 = Read()
obj_2 = Identifier()
obj_3 = ChecksumCalc()
obj_1.Readmeth()
obj_3.checksum()



