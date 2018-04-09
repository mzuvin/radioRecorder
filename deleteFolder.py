import os
import time

def log(data):
    dosya = open("delete-logs.txt","a")
    dosya.write(time.ctime()+" "+data+"\n")
    dosya.close()

isim=str(time.strftime("%b"))

sil="rm -fr "+str(isim)
varMi=os.path.exists("/home/radyo/"+str(isim))
if varMi==True:
    try:
        for i in os.walk("/home/radyo/"+isim):
            log(str(i))
        os.system(sil)
        log("Gorev tamamlandi.")
    except Exception as e:
        log("hata: "+ str(e.message))
if varMi==False:
    log("klasor yok"+ str(isim))
