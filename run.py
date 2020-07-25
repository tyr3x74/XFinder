import requests as rq
from stringcolor import *
from os import system
################################
## Author : Tyr3X             ##
################################

def admin():
    system("clear")
    e = input(f"Enter url ( ex : https://google.com ) : ")
    f = open("db/db1.txt", "r")

    b = f.readlines()


    for v in b:
        v = v.replace("\n", "")
        url = e + "/" + v
        req = rq.get(url)
        if req.status_code != 404 and req.status_code != 401:
            if req.content == "Page not Found":
                pass
            else:
                print(cs(f"[-] Page Found : {url}", "green"))
                exit()
        else:
            pass
def dirs():
    system("clear")
    link = input(f"Enter url ( ex : https://google.com ) : ")
    f = open("db/db2.txt","r")
    f1 = f.readlines()

    for i in f1: 
        i = i.replace("\n", "")
        url = link + "/" + i
        req = rq.get(url)
        if req.status_code != 401 and req.status_code != 404:
            if req.content == "Page not Found":
                pass
            else:
                print(cs(f"[+] Page Found : {url}", "green"))
        else:
            pass    
def domain():
    system("clear")
    x = input(f"Enter url ( ex : https://google.com ) : ")
    c = open("db/db3.txt", "r")
    f1 = c.readlines()
    
    for i in f1:
        i = i.replace("\n", "")
        link = i + "." + x
        req = rq.get(link)
        if req.status_code != 404 and req.status_code != 401:
            if "Page not Found" in req.content:
                pass
            else:
                print(cs(f"[+] Page Found : {link}", "green"))
        else:
            pass
        
        
def main():
    print("====================\n      Main Menu\n====================\n[1]> Admin finder\n[2]> Dir finder\n[3]> Domain finder\n====================")
    x = int(input('[@tyr3x]> '))
    if x == 1:
        admin()
    elif x == 2:
        dirs()
    elif x == 3:
        domain()
    else:
        system("clear")
        exit()
            
if __name__ == "__main__":
    main()
    
    


        
            
