from playsound import playsound
from time import sleep
import sys


def e11():
    # ---beginning---
    # sets the line to read from and converts the string to a list;
    # deletes last item
    activeline = all_lines[1]
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    grpcnt = ([all_lines[2][i:i + 1] for i in range(0, len(all_lines[2]), 1)])
    del grpcnt[-1]
    del activelist[-1]
    print("For ID " + ' '.join(activelist))
    print("with " + ' '.join(grpcnt) + " groups")
    # plays the starting numbers (ID Oblique Groupcount)
    for Nr in range(30):
        sleep(0.5)
        for Nr in range(3):
            activenumber = activelist[Nr]
            playsound("E11/{}.wav".format(activenumber))
            sleep(0.23)
        playsound("E11/Oblique.wav")
        sleep(0.23)
        for Nr in range (len(grpcnt)):
            activegrpcntnumber = grpcnt[Nr]
            playsound("E11/{}.wav".format(activegrpcntnumber))
            sleep(0.23)
    # Attention!
    sleep(0.5)
    print("Attention!")
    playsound("E11/attention.wav")
    sleep(0.5)
    # ---MAIN PART---
    activeline = all_lines[3]
    activelist = activeline.split()
    for Nr in range (len(activelist)):
        activegroup = activelist[Nr]
        activesplitgroup = ([activegroup[i:i + 1] for i in range(0, len(activegroup), 1)])
        print(' '.join(activesplitgroup))
        for Nr in range(2):
            for Nr in range(5):
                activenumber = activesplitgroup[Nr]
                playsound("E11/{}.wav".format(activenumber))
                sleep(0.23)
            sleep(0.5)
    print("Attention!")
    playsound("E11/attention.wav")
    sleep(0.5)
    # Repeat
    activeline = all_lines[3]
    activelist = activeline.split()
    for Nr in range (len(activelist)):
        activegroup = activelist[Nr]
        activesplitgroup = ([activegroup[i:i + 1] for i in range(0, len(activegroup), 1)])
        print(' '.join(activesplitgroup))
        for Nr in range(1):
            for Nr in range(5):
                activenumber = activesplitgroup[Nr]
                playsound("E11/{}.wav".format(activenumber))
                sleep(0.23)
            sleep(0.5)
    # End it all
    print("Out!")
    playsound("E11/out.wav")


def e07():
    # ---beginning---
    # sets the line to read from and converts the string to a list;
    activeline = all_lines[1]
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    grpcnt = ([all_lines[3][i:i + 1] for i in range(0, len(all_lines[3]), 1)])
    # deletes last item
    del grpcnt[-1]
    del activelist[-1]
    print("For ID " + ' '.join(activelist))
    print("1 message")
    # plays the starting numbers (ID ID ID Msgcnt)
    for Nr in range(9):
        sleep(0.4)
        for Nr in range(3):
            sleep(1.1)
            for Nr in range(3):
                activenumber = activelist[Nr]
                playsound("E07/{}.wav".format(activenumber))
                sleep(0.4)
        sleep(1.1)
        playsound("E07/1.wav")
    # Mid part. Plays 3/4-digit group and grpcnt twice
    activeline = all_lines[2]
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    del activelist[-1]
    sleep(3.9)
    print(' '.join(activelist))
    print("With " + ' '.join(grpcnt) + " groups")
    for Nr in range(2):
        for Nr in range(len(activelist)):
            activenumber = activelist[Nr]
            playsound("E07/{}.wav".format(activenumber))
            sleep(0.4)
        sleep(1.1)
        for Nr in range(len(grpcnt)):
            activegrpcountnumber = grpcnt[Nr]
            playsound("E07/{}.wav".format(activegrpcountnumber))
            sleep(1.1)
    sleep(3.9)
    # ---MAIN PART---
    activeline = all_lines[4]
    activelist = activeline.split()
    for Nr in range (len(activelist)):
        activegroup = activelist[Nr]
        activesplitgroup = ([activegroup[i:i + 1] for i in range(0, len(activegroup), 1)])
        print(' '.join(activesplitgroup))
        for Nr in range(1):
            for Nr in range(5):
                activenumber = activesplitgroup[Nr]
                playsound("E07/{}.wav".format(activenumber))
                sleep(0.4)
            sleep(1.1)
    # End it all
    sleep(3.9)
    print("000 000")
    for Nr in range(2):
        sleep(1.1)
        for Nr in range(3):
            playsound("E07/0.wav")
            sleep(0.4)


if len(sys.argv)>2:
    print("Invalid input. Refer to documentation")
    exit()
# txt = "e07test.txt"
try:
    text_file = open((sys.argv[1]))
except IndexError:
    print("Invalid input. Refer to documentation")
    exit()
except FileNotFoundError:
    print("File doesn't exist")
    exit()
# text_file = open(txt)
all_lines = text_file.readlines()
print("Starting custom station as " + str(all_lines[0]))
if all_lines[0] == "E11\n":
    e11()
elif all_lines[0] == "E07\n":
    e07()
else:
    print("File invalid")