from math import ceil
import time


n=10
while(n>0):
    print(n)
    n=n-1


seconds=int(input("Enter The Number of Seconds: "))
#int and input both require parenthesis 
def Countdown_timer(seconds):
 while(seconds>0):
    minutes= int (seconds/60)
    seconds= int (seconds % 60)
    Timer = f'{minutes}:{seconds}'
    #tick symbols act as parenthesis in this sense, it is used to retrieve texts AND vaules
    print(Timer,end="\r") 
    time.sleep(1)
    seconds-=1
    #can be written two ways seconds=seconds-1 being an alternitive
    
 print("Times up!")

Countdown_timer(seconds)



#you can mass indent by highlighting and pressing tab