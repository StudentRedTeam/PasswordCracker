from random import *
import os

pwd=input("Enter password: ")

pwd_all=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
pw=""
while pw!=pwd:
    pw=''
    for letter in range(len(pwd)):
        guess_passwd=pwd_all[randint(0,len(pwd_all)-1)]
        pw=str(guess_passwd)+str(pw)
        print(pw)
        print("Cracking password...Please wait")
        clear_screen()


print("Your password is "+pw)


