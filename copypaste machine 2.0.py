import os
import time
try:
    import pyautogui
except ImportError:
    print ("Attempting to install pyautogui")
    os.system("python -m pip install pyautogui")

#----settings to change----
linesInCode = 1000 #The amount of lines in the copypasta. You won't have to change this unless your copypasta is over 100 lines. (Doesn't have to be exact) Default: 1000
timeToWait = 0.25 #How long to wait in between entered lines. Default: 0.25 (In seconds)
pathOfPasta = '' #Path of your copypasta (.txt) file. YOU WILL NEED TO CHANGE THIS FOR IT TO WORK. Put your path into '' or ""
startTime = 5 #Time between running program and starting writing. Default: 5 (In seconds)
#--------------------------

aFile = open(pathOfPasta, 'r')
f = aFile.readlines()
print("Starting in",startTime,"seconds.")
time.sleep(startTime)

print("~Starting~")

count = 0

timerStart = time.perf_counter()

while count <=linesInCode:
    try:
        pyautogui.write(f[count])
        count= count+1
        time.sleep(timeToWait)
        
    except IndexError:
        timerEnd = time.perf_counter()
        print("~Finished~")
        print(f"Copypasta took {timerEnd - timerStart:0.4f} seconds to print.")
        break

aFile.close()

#Credits -- Created by Hobbson