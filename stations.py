import validator
from time import sleep
from playsound import playsound


def e11(inputID, inputgrpcnt, inputmessage):
    # ---beginning---
    # sets the line to read from and converts the string to a list
    activeline = inputID
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    # fetches the group count
    grpcnt = ([inputgrpcnt[i:i + 1] for i in range(0, len(inputgrpcnt), 1)])
    # deletes last item "\n" from the lists
    # del grpcnt[-1]
    # del activelist[-1]
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
    activeline = inputmessage
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


def s11a(inputID, inputgrpcnt, inputmessage):
    # basically the same as e11
    # ---beginning---
    # sets the line to read from and converts the string to a list
    activeline = inputID
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    # fetches the group count
    grpcnt = ([inputgrpcnt[i:i + 1] for i in range(0, len(inputgrpcnt), 1)])
    # deletes last item "\n" from the lists
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
    activeline = inputmessage
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
    activeline = inputmessage
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


def g06(inputID, inputsecid, inputgrpcnt, inputmessage):
    # IndexError: list index out of range
    # sets the line to read from and converts the string to a list;
    activeline = inputID
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    grpcnt = ([inputgrpcnt[i:i + 1] for i in range(0, len(inputgrpcnt), 1)])
    print("For ID " + ''.join(activelist))
    print("1 message")
    # plays the starting ID for 4 minutes
    # (73x in real world transmission; timing inaccurate (might improve that in future versions)
    for i in range(73):
        for Nr in range(3):
            activenumber = activelist[Nr]
            playsound("Stasi/de/{}.wav".format(activenumber))
            sleep(0.35)
        sleep(1.18-0.35)
    # mid part. Plays 3 digit sec. group and groupcount twice
    activeline = inputsecid
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    print(' '.join(activelist))
    print("With " + ' '.join(grpcnt) + " groups")
    for i in range(2):
        for Nr in range(3):
            activenumber = activelist[Nr]
            playsound("Stasi/de/{}.wav".format(activenumber))
            sleep(0.35)
        sleep(1.18-0.35)
    for i in range(2):
        for Nr in range(len(grpcnt)):
            activenumber = grpcnt[Nr]
            playsound("Stasi/de/{}.wav".format(activenumber))
            sleep(0.35)
        sleep(1.18-0.35)
    # -- MAIN PART --
    activeline = inputmessage
    activelist = activeline.split()
    print(activelist)
    for i in range(len(activelist)):
        activegroup = activelist[i]
        activesplitgroup = ([activegroup[i:i + 1] for i in range(0, len(activegroup), 1)])
        print(' '.join(activesplitgroup))
        for j in range(2):
            for Nr in range(5):
                activenumber = activesplitgroup[Nr]
                playsound("Stasi/de/{}.wav".format(activenumber))
                sleep(0.35)
            sleep(1.18-0.35)
        # sleep(1.18-0.35)
    # End part
    activeline = inputsecid
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    print(' '.join(activelist))
    print(' '.join(grpcnt))
    for i in range(2):
        for Nr in range(3):
            activenumber = activelist[Nr]
            playsound("Stasi/de/{}.wav".format(activenumber))
            sleep(0.35)
        sleep(1.18-0.35)
    for i in range(2):
        for Nr in range(len(grpcnt)):
            activenumber = grpcnt[Nr]
            playsound("Stasi/de/{}.wav".format(activenumber))
            sleep(0.35)
        sleep(0.52-0.35)
    print("000 000")
    for i in range(6):
        playsound("Stasi/de/0.wav")
        sleep(0.35)


def e07(inputID, inputsecid, inputgrpcnt, inputmessage):
    # ---beginning---
    # sets the line to read from and converts the string to a list;
    activeline = inputID
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    grpcnt = ([inputgrpcnt[i:i + 1] for i in range(0, len(inputgrpcnt), 1)])
    # deletes last item
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
    activeline = inputsecid
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
    activeline = inputmessage
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


def e07a(inputID, inputsecid, inputthirdid, inputgrpcnt, inputmessage):
    # ---beginning---
    # sets the line to read from and converts the string to a list;
    activeline = inputID
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
    grpcnt = ([inputgrpcnt[i:i + 1] for i in range(0, len(inputgrpcnt), 1)])
    extragroup = ([inputthirdid[i:i + 1] for i in range(0, len(inputthirdid), 1)])
    # deletes last item
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
    activeline = inputsecid
    activelist = ([activeline[i:i + 1] for i in range(0, len(activeline), 1)])
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
    activeline = inputmessage
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


