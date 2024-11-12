# num=int(input("Enter any number: "))
# if num>0:
    # print("Positive Number")
# elif num<0:
    # print("Negative Number")
# else:
    # print("Zero")

# The above code is now implemented in a loop 
import time   #time functions
while True:
    value=input("enter a value to classify or type Exit or exit to terminate: ")
    if value.lower()=="exit":
        print("Program is about to terminate.")
        time.sleep(1)   # to delay program for given time 
        print("1")
        time.sleep(1) 
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("Program has terminated. Good Bye!!")
        break
    else:
        new_value=int(value)
        if new_value>0:
            print("Positive")
        elif new_value<0:
             print("Negative")
        else:
             print("Zero")

    
