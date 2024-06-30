import string
import random
length=int(input("enter password length:"))
print('''choose character set for password:
      1.digits
      2.letters
      3.special characters
      4.exit''')
charlist=""
while (True):
    choice=int(input("pick a number"))
    if(choice==1):
      charlist+=string.ascii_letters
    elif(choice==2):
        charlist+=string.digits
    elif(choice==3):
        charlist+=string.punctuation
        
    elif(choice==4):
         break
    else:
            print("please pick a valid option!")
password=[]
for i in range(length):
    randomchar=random.choice(charlist)
    password.append(randomchar)
print("the random password is"+"".join(password))
               
               
