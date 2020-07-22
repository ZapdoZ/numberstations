import sys


def sggroupcheck(line, length, varlengthtype, groupname):
    # Varlengthtype is a pre-defined set of how sg groups can vary:
    # length must not be given when varlengthtype != 0
    # 0: cannot vary
    # 1: Can be 3 or 4 digits
    # 2: Can be 1 - 3 digits long

    # check if group is an integer
    try:
        groupint = int(line)
    except ValueError:
        print("[" + groupname + "] " + "Your singular group must be a valid number, quitting")
        exit()
    if varlengthtype == 0:
        # check if main ID is length characters long
        if len(str(groupint)) != length:
            print("[" + groupname + "] " + "Your group must be " + str(length) + " digits long")
            exit()
        else:
            print("[" + groupname + "] " + "Group " + str(groupint) + " accepted")
    elif varlengthtype == 1:
        acceptablelengths = [3, 4]
        if len(str(groupint)) not in acceptablelengths:
            print("[" + groupname + "] " + "Your group must be 3 or 4 digits long")
            exit()
        else:
            print("[" + groupname + "] " + "Group " + str(groupint) + " accepted")
    elif varlengthtype == 2:
        acceptablelengths = [1, 2, 3]
        if len(str(groupint)) not in acceptablelengths:
            # print(len(str(groupint)))
            print("[" + groupname + "] " + "Your group must be 1, 2 or 3 digits long")
            exit()
        else:
            print("[" + groupname + "] " + "Group " + str(groupint) + " accepted")
    else:
        print("Varlengthtype not set, report this bug")


def multigroupcheck():
    print("---Begin Main group check---")
    primgroupLST = maingroups.split()
    grpcnt = len(primgroupLST)
    for Nr in range(0, grpcnt):
        while True:
            try:
                grpchk = int(primgroupLST[Nr])
                if str(grpchk) == str(primgroupLST[Nr]):
                    break
            except ValueError:
                print("[Main groups] The groups may only contain numbers. Correct group Nr " + str(Nr+1))
                exit()
        while len(primgroupLST[Nr]) != 5:
            print("[Main groups] Group number " + str(Nr+1) + " is not valid (must contain exactly 5 digits)")
            exit()
        print("Group #" + str(Nr+1) +  " " + str(primgroupLST[Nr]) + " Accepted")

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

# they're always true
supportedModes = ["E11", "E07"]
all_lines = text_file.readlines()
stationmode = all_lines[0]
# print(stationmode)

# setting the stuff depending on selected mode
if stationmode == "E11\n":
    primID = all_lines[1]
    groupcount = all_lines[2]
    maingroups = all_lines[3]
elif stationmode == "E07\n":
    primID = all_lines[1]
    secID = all_lines[2]
    groupcount = all_lines[3]
    maingroups = all_lines[4]
elif stationmode == "E07a\n":
    primID = all_lines[1]
    thrdID = all_lines[2]
    secID = all_lines[3]
    groupcount = all_lines[4]
    maingroups = all_lines[5]
else:
    print("[Station Mode] Unsupported Station mode, quitting")
    print("Supported modes are " + ', '.join(supportedModes))
    exit()

# print(str(len(all_lines)))

if stationmode == "E11\n" and len(all_lines) != 4:
    print("[Station Mode] E11 files have to be exactly 4 lines long, quitting")
    exit()
elif stationmode == "E07\n" and len(all_lines) != 5:
    print("[Station Mode] E07 files have to be exactly 5 lines long, quitting")
    exit()
elif stationmode == "E07a\n" and len(all_lines) != 6:
    print("[Station Mode] E07a files have to be exactly 6 lines long, quitting")
    exit()



print("[Station Mode] Mode " + stationmode.rstrip("\n") + " ok")
if stationmode == "E11\n":
    sggroupcheck(primID, 3, 0, "Primary ID")
    sggroupcheck(groupcount, 0, 2, "Group count")
    multigroupcheck()
if stationmode == "E07\n":
    sggroupcheck(primID, 3, 0, "Primary ID")
    sggroupcheck(secID, 0, 1, "Secondary ID")
    sggroupcheck(groupcount, 0, 2, "Group count")
    multigroupcheck()
if stationmode == "E07a\n":
    sggroupcheck(primID, 3, 0, "Primary ID")
    sggroupcheck(thrdID, 5, 0, "Third ID")
    sggroupcheck(secID, 0, 1, "Secondary ID")
    sggroupcheck(groupcount, 0, 2, "Group count")
    multigroupcheck()