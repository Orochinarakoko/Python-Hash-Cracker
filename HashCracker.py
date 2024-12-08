import hashlib
import tkinter as tk
from tkinter import messagebox as msg
import time

#----------------------------------------------------

def set_md5():
    button_md5.configure(bg = "black",fg = "white")
    button_sha1.configure(bg = "white",fg = "black")
    button_sha224.configure(bg = "white",fg = "black")
    button_sha256.configure(bg = "white",fg = "black")
    button_sha384.configure(bg = "white",fg="black")
    button_sha512.configure(bg = "white", fg = "black")
    button_blake2b.configure(bg = "white",fg = "black")


   
    global hash_option
    hash_option = 1
    print(str(hash_option))

def set_sha1():
    button_sha1.configure(bg = "black",fg = "white")
    button_md5.configure(bg = "white",fg = "black")
    button_sha224.configure(bg = "white",fg = "black")
    button_sha256.configure(bg = "white",fg = "black")
    button_sha384.configure(bg = "white",fg="black")
    button_sha512.configure(bg = "white", fg = "black")
    button_blake2b.configure(bg = "white",fg = "black")



    global hash_option
    hash_option = 2
    print(str(hash_option))

def set_sha224():
    button_sha224.configure(bg = "black",fg = "white")
    button_md5.configure(bg = "white",fg = "black")
    button_sha1.configure(bg = "white",fg = "black")
    button_sha256.configure(bg = "white",fg = "black")
    button_sha384.configure(bg = "white",fg="black")
    button_sha512.configure(bg = "white", fg = "black")
    button_blake2b.configure(bg = "white",fg = "black")




   
    global hash_option
    hash_option = 3
    print(str(hash_option))
   
def set_sha256():
    button_sha256.configure(bg = "black",fg = "white")
    button_md5.configure(bg = "white",fg = "black")
    button_sha1.configure(bg = "white",fg = "black")
    button_sha224.configure(bg = "white",fg = "black")
    button_sha384.configure(bg = "white",fg="black")
    button_sha512.configure(bg = "white", fg = "black")
    button_blake2b.configure(bg = "white",fg = "black")



    global hash_option
    hash_option = 4
    print(str(hash_option))

def set_sha384():
    button_sha384.configure(bg = "black",fg="white")
    button_sha256.configure(bg = "white",fg = "black")
    button_md5.configure(bg = "white",fg = "black")
    button_sha1.configure(bg = "white",fg = "black")
    button_sha224.configure(bg = "white",fg = "black")
    button_sha512.configure(bg = "white", fg = "black")
    button_blake2b.configure(bg = "white",fg = "black")



    global hash_option
    hash_option = 5
    print(str(hash_option))

def set_sha512():
    button_sha384.configure(bg = "white",fg="black")
    button_sha256.configure(bg = "white",fg = "black")
    button_md5.configure(bg = "white",fg = "black")
    button_sha1.configure(bg = "white",fg = "black")
    button_sha224.configure(bg = "white",fg = "black")
    button_sha512.configure(bg = "black", fg = "white")
    button_blake2b.configure(bg = "white",fg = "black")

    global hash_option
    hash_option = 6
    print(str(hash_option))

def set_blake2b():
    button_sha384.configure(bg = "white",fg="black")
    button_sha256.configure(bg = "white",fg = "black")
    button_md5.configure(bg = "white",fg = "black")
    button_sha1.configure(bg = "white",fg = "black")
    button_sha224.configure(bg = "white",fg = "black")
    button_sha512.configure(bg = "white", fg = "black")
    button_blake2b.configure(bg = "black",fg = "white")

    global hash_option
    hash_option = 7
    print(str(hash_option))

   
   
   

   

   
#----------------------------------------------------    

def main():
    try:

        wordlist = inputList.get()
        if ".txt" not in wordlist:
            wordlist = wordlist + ".txt"

        

        



        
        file = open(wordlist , "r")
        begin_cracking.configure(bg = "red",fg = "yellow")
        hashed = enterHash.get()
        hashed = hashed.encode("utf-8")
        print(hashed)
       
        if hash_option == 1:
            print("md5")
            for line in file:
                line = line.encode("utf-8")
                the_hash2 = hashlib.md5(line.strip()).hexdigest()
                if hashed == the_hash2.encode("utf-8"):
                    line = line.decode()
                    msg.showinfo(f"HASH FOUND",f"Hash = {line}")
                    begin_cracking.configure(bg = "white",fg = "black")
                    break


        elif hash_option == 2:
            for line in file:
                line = line.encode("utf-8")
                the_hash2 = hashlib.sha1(line.strip()).hexdigest()
                if hashed == the_hash2.encode("utf-8"):
                    line = line.decode()
                    msg.showinfo(f"HASH FOUND",f"Hash = {line}")
                    begin_cracking.configure(bg = "white",fg = "black")
                    break
       

        elif hash_option == 3:
            for line in file:
                line = line.encode("utf-8")
                the_hash2 = hashlib.sha224(line.strip()).hexdigest()
                if hashed == the_hash2.encode("utf-8"):
                    line = line.decode()
                    msg.showinfo(f"HASH FOUND",f"Hash = {line}")
                    begin_cracking.configure(bg = "white",fg = "black")
                    break
           
       
        elif hash_option == 4:
            for line in file:
                line = line.encode("utf-8")
                the_hash2 = hashlib.sha256(line.strip()).hexdigest()
                if hashed == the_hash2.encode("utf-8"):
                    line = line.decode()
                    msg.showinfo(f"HASH FOUND",f"Hash = {line}")
                    begin_cracking.configure(bg = "white",fg = "black")
                    break

        elif hash_option == 5:
            for line in file:
                line = line.encode("utf-8")
                the_hash2 = hashlib.sha384(line.strip()).hexdigest()
                if hashed == the_hash2.encode("utf-8"):
                    line = line.decode()
                    msg.showinfo(f"HASH FOUND",f"Hash = {line}")
                    begin_cracking.configure(bg = "white",fg = "black")
                    break

        elif hash_option == 6:
            for line in file:
                line = line.encode("utf-8")
                the_hash2 = hashlib.sha512(line.strip()).hexdigest()
                if hashed == the_hash2.encode("utf-8"):
                    line = line.decode()
                    msg.showinfo(f"HASH FOUND",f"Hash = {line}")
                    begin_cracking.configure(bg = "white",fg = "black")
                    break

        elif hash_option == 7:
            for line in file:
                line = line.encode("utf-8")
                the_hash2 = hashlib.blake2b(line.strip()).hexdigest()
                if hashed == the_hash2.encode("utf-8"):
                    line = line.decode()
                    msg.showinfo(f"HASH FOUND",f"Hash = {line}")
                    begin_cracking.configure(bg = "white",fg = "black")
                    break
    except:
        msg.showinfo("ERROR","INVALID OR MISSING INPUTS")

           

       
       

#----------------------------------------------------
   
window = tk.Tk()

window.configure(bg="#00a2ed")
window.attributes("-zoomed",True)
window.title("Hash Cracker")

#----------------------------------------------------

lableone = tk.Label(window,
                    text="Hash Cracking Software",
                    fg = "white",
                    bg = "#00a2ed",
                    width = 100,
                    height = 3,
                    font = ("Segoe",50,"bold","underline"),
                    )
lableone.pack()

#----------------------------------------------------

labeltwo = tk.Label(window,
                    text = "1) Please enter the hashed password below:",
                    fg = "white",
                    bg = "#00a2ed",
                    width = 35,
                    height = 1,
                    font = ("Segoe",15)
                    )
labeltwo.place(relx = 0.15,rely = 0.2,anchor = "center")

#----------------------------------------------------

enterHash = tk.Entry(fg = "black" , bg = "white", width = 50)
enterHash.place(relx = 0.15 ,rely = 0.3 , anchor = "center")

#----------------------------------------------------

labelthree = tk.Label(window,
                      text = "2) Please select the hash type:",
                      fg = "white",
                      bg = "#00a2ed",
                      width = 50,
                      height = 2,
                      font = ("Segoe",15)
                      )
labelthree.place(relx = 0.5 , rely = 0.2,anchor = "center")

#----------------------------------------------------

button_md5 = tk.Button(text = "MD5",
                       fg = "black",
                       bg = "white",
                       width = 75,
                       height = 1,
                       command = set_md5
                       )
button_md5.place(relx = 0.5 , rely = 0.3 , anchor = "center")



#----------------------------------------------------

button_sha1 = tk.Button(text = "SHA1",
                       fg = "black",
                       bg = "white",
                       width = 75,
                       height = 1,
                       command = set_sha1
                       )
button_sha1.place(relx = 0.5 , rely = 0.35 , anchor = "center")


#----------------------------------------------------

button_sha224 = tk.Button(text = "SHA224",
                       fg = "black",
                       bg = "white",
                       width = 75,
                       height = 1,
                       command = set_sha224
                       )

button_sha224.place(relx = 0.5 , rely = 0.4 , anchor = "center")

#----------------------------------------------------

button_sha256 = tk.Button(text = "SHA256",
                       fg = "black",
                       bg = "white",
                       width = 75,
                       height = 1,
                       command = set_sha256
                       )

button_sha256.place(relx = 0.5 , rely = 0.45 , anchor = "center")



#---------------------------------------------------
button_sha384 = tk.Button(text = "SHA384",
                          fg = "black",
                          bg = "white",
                          height = 1,
                          width = 75,
                          command = set_sha384
                          )
button_sha384.place(relx =0.5 , rely = 0.5 , anchor = "center")
#---------------------------------------------------

button_sha512 = tk.Button(text = "SHA512",
                          fg = "black",
                          bg = "white",
                          height = 1,
                          width = 75,
                          command = set_sha512
                          )
button_sha512.place(relx = 0.5 , rely = 0.55 , anchor = "center")

#---------------------------------------------------

button_blake2b = tk.Button(text = "BLAKE2b",
                          fg = "black",
                          bg = "white",
                          height = 1,
                          width = 75,
                          command = set_blake2b
                          )
button_blake2b.place(relx = 0.5 , rely = 0.6 , anchor = "center")

#---------------------------------------------------

listLabel = tk.Label(text = "3) Enter wordlist name :",
                     fg = "white",
                     bg = "#00a2ed",
                     width = 35,
                     height = 1,
                     font = ("Segoe",15))

listLabel.place(relx = 0.85 , rely = 0.2 , anchor = "center")
                     





#----------------------------------------------------
inputList = tk.Entry(width = 50)

inputList.place(relx = 0.85,rely=0.3,anchor = "center")




#---------------------------------------------------

begin_cracking = tk.Button(text = "Begin Cracking",
                           fg = "black",
                           bg = "white",
                           height = 5,
                           width = 50,
                           font = ("Segoe",25,"bold"),
                           command = main
                           )

begin_cracking.place(relx = 0.5 , rely = 0.85 , anchor = "center")

                           

#----------------------------------------------------

window.mainloop()


