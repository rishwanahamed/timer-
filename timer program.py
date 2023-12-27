import time       #this is time module for using creating time and provide delay
import winsound   #winsound help to make sound from system speakers

def timer(a):
    print("Timer set for {} seconds".format(a))
    for i in range(a,-1,-1):
        print("The Time remaining {}".format(i),end='\r')  #r is over write the existing line
        time.sleep(1)
    print("\n Time Up!")

    for i in range(3):
        winsound.Beep(1000,1000)     #this is 1000hz frequency and 1000 milliseconds
        time.sleep(.1)
if __name__=="__main__":   #the execution starts here
    try:
        user_input=int(input("enter the seconds"))
        timer(user_input)
    except ValueError:
        print("invalid value")