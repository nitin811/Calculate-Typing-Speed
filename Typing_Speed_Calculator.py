from time import *  # This method Import everything from the time module directly into your program.
import random as r

def mistake(ParagraphTest,usertest):
    error=0
    for i in range(len(ParagraphTest)):
        try:
            if ParagraphTest[i] != usertest:
                error=error+1
        except:
            error=error+1
    return error

def speed_time(time_start,time_end,userInput):
    time_delay = time_end - time_start
    time_R = round(time_delay,2)
    speed = len(userInput)/time_R
    return round(speed)

while True:
    check=input("Ready for Test : Yes/No :")
    if check=="Yes":
        test=["You usually don't need to install tkinter separately"," it comes pre-installed with Python "," especially on Windows and Mac."]
        test1=r.choice(test)
        print()
        print("         ****Typing Speed****        ")
        print(test1)
        print()
        print()
        time_1=time()
        testInput=input("Enter :")
        time_2=time()

        print('Speed : ',speed_time(time_1,time_2,testInput),"words/sec")
        print("Error : ",mistake(test1,testInput))

    elif check=="No":
        print("It's ok, No problem !!!")
        break

    else:
        print("Invalid!!!!")