#Modules
import os

#Main
if __name__=='__main__':
    print("****Welcome to speaker****")
    while True:
        x=input("Enter your word: ")
        if x== "q":
            break
        command=f"say {x}"
        os.system(command)