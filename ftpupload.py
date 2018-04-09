import ftplib
import time

isim=str(time.strftime("rec%b%d18.mp3"))
name=str(time.strftime("%b/rec%b%d18.mp3"))

def logftp(data):
    dosya = open("ftp-logs.txt","a")
    dosya.write(time.ctime()+" "+data+"\n")
    dosya.close()

ftp = ftplib.FTP()
host = "1.2.3.4"
port = 21
ftp.connect(host, port)
logftp("ftp baglandi")
print (ftp.getwelcome())
try:
    ftp.login("username", "password")
    ftp.cwd("/htdocs")#path
    #print(ftp.pwd())
    # uzak dosyanın ismi
    mp3_dosya = isim
    # local dosya adres
    mp3_dosya_yolu = name
    filee=open(mp3_dosya_yolu,'rb')
    ftp.storbinary("STOR " + mp3_dosya, filee)
    filee.close()
    logftp("send success "+str(name))
except:
    logftp("failed to login")
