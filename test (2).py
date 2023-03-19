import telnetlib


host ='192.168.0.1'


numarator = 0
disp_interf_bri = "display interface brief"


def write_in_file():
    f = open('pythonfile.txt', 'a')
    f.write(str(vartext))  # tot outputul
    f.close()





def read_from_file():
    file = open('pythonfile.txt', 'r')
    lines = file.read().splitlines()
    last_line = lines[-3]  # internet addres is 8.8.8.8/24
    print(last_line)
    return last_line







def insert():
    numarator +=1
    telnet = telnetlib.Telnet(host)
    username = input("Introdu useru barosane:")
    password = input("Introdu pw barosane:")
    print(telnet.read_until(b'Username:').decode('ascii'))
    telnet.write(username.encode('utf-8') + b"\n")

    print(tn.read_until(b'Password:').decode('ascii'))
    tn.write(password.encode('utf-8') + b"\n")





param = 1
while 1:
    tn = telnetlib.Telnet(host)
    username = input("Introdu useru barosane:")
    password = input("Introdu pw barosane:")
    #read and write username
    print(tn.read_until(b'Username:').decode('ascii'))
    tn.write(username.encode('utf-8') + b"\n")

        # read and write pw
    print(tn.read_until(b'Password:').decode('ascii'))
    tn.write(password.encode('utf-8') + b"\n")

    if(username == 'cata' and password =='Huawei@12'):
        numarator = 0
        #print(tn.read_until(b'<HUAWEI>').decode('ascii'))

        tn.write('sys'.encode('utf-8') + b"\n")

        print(tn.read_until(b'[HUAWEI]').decode('ascii' ) )
        # tn.write('disp ip int Vlanif 2'.encode('utf-8') + b"\n")
        # vartext = tn.read_until(b'/24').decode('ascii')
        # print(vartext)

        infinity = 0


        while infinity == 0  :
            tn.write('screen-length 0 temporary'.encode('utf-8') + b"\n")
            tn.write('sy'.encode('utf-8') + b"\n")



            tn.write('disp ip int Vlanif 2'.encode('utf-8') + b"\n")

            vartext = tn.read_until(b'Broadcast address').decode("utf-8")
            #print(vartext)

            write_in_file()
            read_from_file()
            print("TUTIIIIIIIIIIIIIIIIIIIIIIIIII")
            print(read_from_file())

            if (read_from_file() == 'Internet Address is 8.8.8.8/24 '):
                print("e bn")
                continue

            else :

                print("WARNING ! ADRESA IP A FOST SCHIMBATA !")
                tn.write('int Vlanif 2'.encode('utf-8') + b"\n")
                tn.write('undo ip address'.encode('utf-8') + b"\n")
                tn.write('ip address 8.8.8.8 24'.encode('utf-8') + b"\n")

                tn.write('quit'.encode('utf-8') + b"\n")














        #regex = re.search('Internet Address is 8.8.8.8/24',vartext)   # true

    else:


        print(tn.read_until(b'\n').decode('ascii'))
        print("username sau pw gresit !!!!!!! ;)")
        while numarator > 0 :
            insert()

