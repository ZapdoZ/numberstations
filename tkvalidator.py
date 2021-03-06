import tkinter as tk
from tkinter import messagebox as tkmsg


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
        # print("[" + groupname + "] " + "Your singular group must be a valid number, quitting")
        tkmsg.showerror(groupname, "Singular group must be a valid number")
        return False
    if varlengthtype == 0:
        # check if main ID is length characters long
        if len(str(groupint)) != length:
            # print("[" + groupname + "] " + "Your group must be " + str(length) + " digits long")
            tkmsg.showerror(groupname, "Your group must be {} digits long".format(str(length)))
            return False
        else:
            print("[" + groupname + "] " + "Group " + str(groupint) + " accepted")
    elif varlengthtype == 1:
        acceptablelengths = [3, 4]
        if len(str(groupint)) not in acceptablelengths:
            # print("[" + groupname + "] " + "Your group must be 3 or 4 digits long")
            tkmsg.showerror(groupname, "Your group must be 3 or 4 digits long")
            return False
        else:
            print("[" + groupname + "] " + "Group " + str(groupint) + " accepted")
    elif varlengthtype == 2:
        acceptablelengths = [1, 2, 3]
        if len(str(groupint)) not in acceptablelengths:
            print("[" + groupname + "] " + "Your group must be 1, 2 or 3 digits long")
            tkmsg.showerror(groupname, "Your group must be 1, 2 or 3 digits long")
            return False
        else:
            print("[" + groupname + "] " + "Group " + str(groupint) + " accepted")
    else:
        print("Varlengthtype not set, report this bug")

def multigroupcheck(maingroups):
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
                tkmsg.showerror("MainGroups Error", "The groups may only contain numbers. Correct group Nr {}".format(str(Nr+1)))
                return False
        while len(primgroupLST[Nr]) != 5:
            tkmsg.showerror("MainGroups Error", "Group number " + str(Nr+1) + " is not valid (must contain exactly 5 digits)")
            return False
        print("Group #" + str(Nr+1) + " " + str(primgroupLST[Nr]) + " Accepted")



