import requests
import time
import os

def log(data):
    dosya = open("logs.txt","a")
    dosya.write(time.ctime()+" "+data+"\n")
    dosya.close()

try:
    isimKlasor=str(time.strftime("%b"))
    os.mkdir(isimKlasor)
    log("Klasor Create"+str(isimKlasor))
except:
    log("Klasor Hata")


stream_url = 'http://streamurl...'

r = requests.get(stream_url, stream=True)

isim=str(time.strftime("rec%b%d18.mp3"))

log("Record")
with open(isim, 'wb') as f:
    try:
        for block in r.iter_content(10):
            #time=str(time.strftime("%M"))
            #print time.strftime("%M")
            f.write(block)
            if time.strftime("%M") == "35":
                log("STOP")
                break
    except KeyboardInterrupt:
        pass

