from time import sleep
import sys
import validator
import os


os.system("rm /tmp/out.wav")
os.system("sox -n -r 44100 /tmp/out.wav trim 0.0 0.0")

def playsound(sound):
  os.system("sox /tmp/out.wav {} /tmp/out2.wav".format(sound))
  os.system("mv /tmp/out2.wav /tmp/out.wav")

def sleep(secs):
   os.system("sox -n -r 44100 /tmp/sltemp.wav trim 0.0 {}".format(secs))
   os.system("sox /tmp/out.wav /tmp/sltemp.wav /tmp/out2.wav")
   os.system("mv /tmp/out2.wav /tmp/out.wav")

def e11():
    # ---beginning---
    # sets the line to read from and converts the string to a list
    activeline = all_lines[1]
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    # fetches the group count
    grpcnt = ([all_lines[2][i:i + 1] for i in range(0, len(all_lines[2]), 1)])
    # deletes last item "\n" from the lists
    del grpcnt[-1]
    del activelist[-1]
    # prints some info
    print("For ID " + ' '.join(activelist))
    print("with " + ' '.join(grpcnt) + " groups")
    # plays the starting numbers (ID; Oblique; Group count)
    for Nr in range(30):
        sleep(0.5)
        for Nr in range(3):
            activenumber = activelist[Nr]
            playsound("E11/{}.wav".format(activenumber))
            sleep(0.23)
        playsound("E11/Oblique.wav")
        sleep(0.23)
        for Nr in range(len(grpcnt)):
            activegrpcntnumber = grpcnt[Nr]
            playsound("E11/{}.wav".format(activegrpcntnumber))
            sleep(0.23)
    # Attention!
    sleep(0.5)
    print("Attention!")
    playsound("E11/Attention.wav")
    sleep(0.5)
    # ---MAIN PART---
    activeline = all_lines[3]
    activelist = activeline.split()
    for Nr in range(len(activelist)):
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
    playsound("E11/Attention.wav")
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


def s11a():
    # basically the same as e11
    # ---beginning---
    # sets the line to read from and converts the string to a list
    activeline = all_lines[1]
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    # fetches the group count
    grpcnt = ([all_lines[2][i:i + 1] for i in range(0, len(all_lines[2]), 1)])
    # deletes last item "\n" from the lists
    del grpcnt[-1]
    del activelist[-1]
    # prints some info
    print("For ID " + ' '.join(activelist))
    print("with " + ' '.join(grpcnt) + " groups")
    # plays the starting numbers (ID; Cherta; Group count)
    for Nr in range(30):
        sleep(0.5)
        for Nr in range(3):
            activenumber = activelist[Nr]
            playsound("S11a/{}.wav".format(activenumber))
            sleep(0.23)
        playsound("S11a/Cherta.wav")
        sleep(0.23)
        for Nr in range(len(grpcnt)):
            activegrpcntnumber = grpcnt[Nr]
            playsound("S11a/{}.wav".format(activegrpcntnumber))
            sleep(0.23)
    # Vnimanie!
    sleep(0.5)
    print("Vnimanie!")
    playsound("S11a/Vnimanie.wav")
    sleep(0.5)
    # ---MAIN PART---
    activeline = all_lines[3]
    activelist = activeline.split()
    for Nr in range(len(activelist)):
        activegroup = activelist[Nr]
        activesplitgroup = ([activegroup[i:i + 1] for i in range(0, len(activegroup), 1)])
        print(' '.join(activesplitgroup))
        for Nr in range(2):
            for Nr in range(5):
                activenumber = activesplitgroup[Nr]
                playsound("S11a/{}.wav".format(activenumber))
                sleep(0.23)
            sleep(0.5)
    print("Vnimanie!")
    playsound("S11a/Vnimanie.wav")
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
                playsound("S11a/{}.wav".format(activenumber))
                sleep(0.23)
            sleep(0.5)
    # End it all
    print("Konets!")
    playsound("S11a/Konets.wav")


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
    for Nr in range(len(activelist)):
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


def e07a():
    # ---beginning---
    # sets the line to read from and converts the string to a list;
    activeline = all_lines[1]
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    grpcnt = ([all_lines[4][i:i + 1] for i in range(0, len(all_lines[4]), 1)])
    extragroup = ([all_lines[2][i:i + 1] for i in range(0, len(all_lines[2]), 1)])
    # deletes last item
    del grpcnt[-1]
    del activelist[-1]
    del extragroup[-1]
    print("For ID " + ' '.join(activelist))
    print("1 message")
    print("With extra group " + ' '.join(extragroup))
    # plays the starting numbers (ID ID ID Msgcnt)
    for Nr in range(8):
        sleep(0.4)
        for Nr in range(3):
            sleep(1.1)
            for Nr in range(3):
                activenumber = activelist[Nr]
                playsound("E07/{}.wav".format(activenumber))
                sleep(0.4)
        sleep(1.1)
        playsound("E07/1.wav")
        sleep(1.1)
        for Nr in range(len(extragroup)):
            activenumber = extragroup[Nr]
            playsound("E07/{}.wav".format(activenumber))
            sleep(0.4)
    # Mid part. Plays 3/4-digit group and grpcnt twice
    activeline = all_lines[3]
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
    activeline = all_lines[5]
    activelist = activeline.split()
    for Nr in range(len(activelist)):
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


# check if given cli input isn't too long, exit if so
if len(sys.argv) > 2:
    print("Invalid input. Refer to documentation")
    exit()

# tries to load the text file from the given cli argument
try:
    text_file = open((sys.argv[1]))
# exits if there is no cli argument
except IndexError:
    print("Invalid input. Refer to documentation")
    exit()
# exits if the file doesn't exist
except FileNotFoundError:
    print("File doesn't exist")
    exit()

# puts all lines of the text file into a list
all_lines = text_file.readlines()
print("Starting custom station as " + str(all_lines[0]))

# checks for mode in first line, checks the file and starts the required function
if all_lines[0] == "E11\n":
    validator.sggroupcheck(all_lines[1], 3, 0, "Primary ID")
    validator.sggroupcheck(all_lines[2], 0, 2, "Group count")
    validator.multigroupcheck(all_lines[3])
    print("\n")
    print("Begin message")
    e11()
elif all_lines[0] == "E07\n":
    validator.sggroupcheck(all_lines[1], 3, 0, "Primary ID")
    validator.sggroupcheck(all_lines[2], 0, 1, "Secondary ID")
    validator.sggroupcheck(all_lines[3], 0, 2, "Group count")
    validator.multigroupcheck(all_lines[4])
    print("\n")
    print("Begin message")
    e07()
elif all_lines[0] == "E07a\n":
    validator.sggroupcheck(all_lines[1], 3, 0, "Primary ID")
    validator.sggroupcheck(all_lines[2], 5, 0, "Third ID")
    validator.sggroupcheck(all_lines[3], 0, 1, "Secondary ID")
    validator.sggroupcheck(all_lines[4], 0, 2, "Group count")
    validator.multigroupcheck(all_lines[5])
    print("\n")
    print("Begin message")
    e07a()
elif all_lines[0] == "S11a\n":
    validator.sggroupcheck(all_lines[1], 3, 0, "Primary ID")
    validator.sggroupcheck(all_lines[2], 0, 2, "Group count")
    validator.multigroupcheck(all_lines[3])
    print("\n")
    print("Begin message")
    s11a()
else:
    print("File invalid")

os.system("mv /tmp/out.wav out.wav")
