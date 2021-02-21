from itertools import product, permutations  
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

main = input("Objects (Seperated with comma without space) ")
toPick = input("How many objects in 1 comb? ")
mainArray = main.split(",")

repetition = input("Repetition? ")
try:
    int(toPick)
    if (repetition.lower() == "yes"):
        print("Repetition enabled!")
        finish = product(mainArray, repeat=int(toPick))  
        
        time.sleep(1)
        length = 0
        for i in list(finish):
            length += 1
            print(i)  
            keyboard.press(Key.enter)
            time.sleep(0.2)
            # for num in i:
            #     keyboard.tap(Key.backspace)
            for num in i:
                keyboard.type(num)

        print(str(length) + " possible combinations") 
    elif (repetition.lower() == "no"):
        print("Repetition disabled!")
        finish = permutations(mainArray, int(toPick)) 

        time.sleep(1)
        length = 0
        for i in list(finish):
            length += 1
            print(i)  
            keyboard.press(Key.enter)
            time.sleep(0.2)
            # for num in i:
            #     keyboard.tap(Key.backspace)
            for num in i:
                keyboard.type(num)

        print(str(length) + " possible combinations")
    else:
        print("Not a valid yes/no answer.")
except:
    print(toPick + " isn't a number")