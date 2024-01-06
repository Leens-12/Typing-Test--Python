import time
import random

while True:
    sen1 = []
    file = open("Sentences and words", "r")
    while True:
        sen = file.readline()
        if sen == "":
            break
        sen1.append(sen)

    count_space= 0
    file.close()


    print("Hello, welcome to the Typing test!")
    print("You will be tested on how fast you type, accuracy level and the words per minute!")
    print('\nYour test starts in')

    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)

    time.sleep(1)
    print('GO!\n')

    print("\nYour sentence is,")
    c = random.randint(0, 16)
    print(sen1[c])
    a = sen1[c].strip().split(" ")

    start = time.time()
    user = input("\n")

    b = user.split(" ")

    for i in user:
        if i == " ":
            count_space = count_space + 1
    stop = time.time()
    time_ = stop - start
    print("Time:",time_)

    WPM = (count_space + 1)/ time_
    WPM = WPM * 60
    print("Words per minute:", WPM)

    accuracy_count = 0
    for i in range(len(a)):
        if i >= len(b):
            break
        if a[i] == b[i]:
            accuracy_count = accuracy_count + 1

    accuracy_ = accuracy_count / len(a)
    accuracy_ = accuracy_ * 100
    print("Accuracy:", accuracy_)

    choice = input("\nDo you want to play again, Y or N: ")

    if choice == "Y":
        print("\n-----------------------------------------------------------------------------------------\n")
        continue
    else:
        print("\nGoodbye!")
        print("Thank you for testing out your typing skills.")
        break