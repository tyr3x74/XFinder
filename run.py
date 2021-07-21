import requests as rq
from os import system
################################
## Author : Tyr3X             ##
################################

# Please don't remove author name

def admin():
    page = []
    error = []
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
                error.append(url)
                pass
            else:
                page.append(url)
                open("admin.result.txt", "a").write(url + "\n")                
        else:
            error.append(url)
            pass
        print(end='\r[*] Page Found : %s - Page Not Found : %s'%(
                str(len(page)),
                str(len(error))
              ),
              flush=True
             )    
    print("\n\nsaved : admin.result.txt")       
               
def dirs():
    page = []
    error = []
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
                error.append(url)
                pass
            else:
                page.append(url)
                open("dir.result.txt", "a").write(url + "\n")
        else:
            error.append(url)
            pass          
        print(end='\r[*] Page Found : %s - Page Not Found : %s'%(
                str(len(page)),
                str(len(error))
              ),
              flush=True
             )    
    print("\n\nsaved : dir.result.txt")                   
def domain():
    page = []
    error = []
    system("clear")
    x = input(f"Enter url ( ex : https://google.com ) : ")
    c = open("db/db3.txt", "r")
    f1 = c.readlines()
    
    for i in f1:
        i = i.replace("\n", "")
        url = i + "." + x
        req = rq.get(url)
        if req.status_code != 404 and req.status_code != 401:
            if req.content == "Page not Found":
                error.append(url)
                pass
            else:
                page.append(url)
                open("domain.result.txt", "a").write(url + "\n")                
        else:
            error.append(url)
            pass
        print(end='\r[*] Page Found : %s - Page Not Found : %s'%(
                str(len(page)),
                str(len(error))
              ),
              flush=True
             )  
    print("\n\nsaved : domain.result.txt")                                 
        
def main():
    system("clear")
    print("========================\n      XFINDER v1.1\n========================\n== [1]> Admin finder  ==\n== [2]> Dir finder    ==\n== [3]> Domain finder ==\n========================\n")
    x = int(input('[@tyr3x]> '))
    if x == 1:
        admin()
    elif x == 2:
        dirs()
    elif x == 3:
        domain()
    else:
        raise Exception("Enter correct input!")
            
if __name__ == "__main__":
    main()
    
    


        
            
