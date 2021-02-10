import tkinter as tk
from stations import *
import tkvalidator
import multiprocess
from tkinter import filedialog
import tkinter.messagebox as tkmsg


class E11Frame():
    def __init__(self):
        self.title = "E11"
        self.e11frame = tk.Frame(root)

        self.IDlabel = tk.Label(self.e11frame, text="3-digit ID")
        self.grpcntlabel = tk.Label(self.e11frame, text="Group Count")
        self.msgLabel = tk.Label(self.e11frame, text="Message text")
        self.launchbutton = tk.Button(self.e11frame, text="Start station",
                                      command=lambda: launchstation(Station="E11",
                                                                    ID=self.ID.get(),
                                                                    grpcnt=self.grpcnt.get(),
                                                                    message=self.message.get("1.0", 'end-1c')))

        self.ID = tk.Entry(self.e11frame)
        self.grpcnt = tk.Entry(self.e11frame)
        self.message = tk.Text(self.e11frame)

        self.IDlabel.place(x=10, y=10)
        self.ID.place(x=10, y=30)
        self.grpcntlabel.place(x=10, y=60)
        self.grpcnt.place(x=10, y=80)
        self.msgLabel.place(x=10, y=110)
        self.message.place(x=10, y=130, width=395, height=300)
        self.launchbutton.place(x=550, y=400, width=80, height=30)

    def show(self):
        self.e11frame.place(x=0, y=0, width=640, height=480)

    def hide(self):
        self.e11frame.place_forget()

    def resetbutton(self):
        self.launchbutton["text"] = "Start station"
        self.launchbutton["command"] = lambda: launchstation(Station="E11",
                                                             ID=self.ID.get(),
                                                             grpcnt=self.grpcnt.get(),
                                                             message=self.message.get("1.0", 'end-1c'))

    def resetall(self):
        self.resetbutton()
        self.ID.delete(0, 'end')
        self.grpcnt.delete(0, 'end')
        self.message.delete(1.0, 'end')


class S11aFrame():
    def __init__(self):
        self.title = "S11a"
        self.s11aframe = tk.Frame(root)

        self.IDlabel = tk.Label(self.s11aframe, text="3-digit ID")
        self.grpcntlabel = tk.Label(self.s11aframe, text="Group Count")
        self.msgLabel = tk.Label(self.s11aframe, text="Message text")
        self.launchbutton = tk.Button(self.s11aframe, text="Start station",
                                      command=lambda: launchstation(Station="S11a",
                                                                    ID=self.ID.get(),
                                                                    grpcnt=self.grpcnt.get(),
                                                                    message=self.message.get("1.0", 'end-1c')))

        self.ID = tk.Entry(self.s11aframe)
        self.grpcnt = tk.Entry(self.s11aframe)
        self.message = tk.Text(self.s11aframe)

        self.IDlabel.place(x=10, y=10)
        self.ID.place(x=10, y=30)
        self.grpcntlabel.place(x=10, y=60)
        self.grpcnt.place(x=10, y=80)
        self.msgLabel.place(x=10, y=110)
        self.message.place(x=10, y=130, width=395, height=300)
        self.launchbutton.place(x=550, y=400, width=80, height=30)

    def show(self):
        self.s11aframe.place(x=0, y=0, width=640, height=480)

    def hide(self):
        self.s11aframe.place_forget()

    def resetbutton(self):
        self.launchbutton["text"] = "Start station"
        self.launchbutton["command"] = lambda: launchstation(Station="S11a",
                                                             ID=self.ID.get(),
                                                             grpcnt=self.grpcnt.get(),
                                                             message=self.message.get("1.0", 'end-1c'))

    def resetall(self):
        self.resetbutton()
        self.ID.delete(0, 'end')
        self.grpcnt.delete(0, 'end')
        self.message.delete(1.0, 'end')


class E07Frame():
    def __init__(self):
        self.title = "E07"
        self.e07frame = tk.Frame(root)

        self.IDlabel = tk.Label(self.e07frame, text="3-digit Main ID")
        self.secidlabel = tk.Label(self.e07frame, text="3/4-digit Secondary ID")
        self.grpcntlabel = tk.Label(self.e07frame, text="Group Count")
        self.msgLabel = tk.Label(self.e07frame, text="Message text")
        self.launchbutton = tk.Button(self.e07frame, text="Start station",
                                      command=lambda: launchstation(Station="E07",
                                                                    ID=self.ID.get(),
                                                                    secid=self.secid.get(),
                                                                    grpcnt=self.grpcnt.get(),
                                                                    message=self.message.get("1.0", 'end-1c')))

        self.ID = tk.Entry(self.e07frame)
        self.secid = tk.Entry(self.e07frame)
        self.grpcnt = tk.Entry(self.e07frame)
        self.message = tk.Text(self.e07frame)

        self.IDlabel.place(x=10, y=10)
        self.ID.place(x=10, y=30)
        self.secidlabel.place(x=10, y=60)
        self.secid.place(x=10, y=80)
        self.grpcntlabel.place(x=10, y=110)
        self.grpcnt.place(x=10, y=130)
        self.msgLabel.place(x=10, y=160)
        self.message.place(x=10, y=180, width=395, height=250)
        self.launchbutton.place(x=550, y=400, width=80, height=30)

    def show(self):
        self.e07frame.place(x=0, y=0, width=640, height=480)

    def hide(self):
        self.e07frame.place_forget()

    def resetbutton(self):
        self.launchbutton["text"] = "Start station"
        self.launchbutton["command"] = lambda: launchstation(Station="E07",
                                                             ID=self.ID.get(),
                                                             secid=self.secid.get(),
                                                             grpcnt=self.grpcnt.get(),
                                                             message=self.message.get("1.0", 'end-1c'))

    def resetall(self):
        self.resetbutton()
        self.ID.delete(0, 'end')
        self.secid.delete(0, 'end')
        self.grpcnt.delete(0, 'end')
        self.message.delete(1.0, 'end')


class E07aFrame():
    def __init__(self):
        self.title = "E07a"
        self.e07aframe = tk.Frame(root)

        self.IDlabel = tk.Label(self.e07aframe, text="3-digit Main ID")
        self.secidlabel = tk.Label(self.e07aframe, text="3/4-digit Secondary ID")
        self.thirdidlabel = tk.Label(self.e07aframe, text="5-digit extra group")
        self.grpcntlabel = tk.Label(self.e07aframe, text="Group Count")
        self.msgLabel = tk.Label(self.e07aframe, text="Message text")
        self.launchbutton = tk.Button(self.e07aframe, text="Start station",
                                      command=lambda: launchstation(Station="E07a", ID=self.ID.get(),
                                                                    secid=self.secid.get(),
                                                                    thirid=self.thirdid.get(),
                                                                    grpcnt=self.grpcnt.get(),
                                                                    message=self.message.get("1.0", 'end-1c')))

        self.ID = tk.Entry(self.e07aframe)
        self.secid = tk.Entry(self.e07aframe)
        self.thirdid = tk.Entry(self.e07aframe)
        self.grpcnt = tk.Entry(self.e07aframe)
        self.message = tk.Text(self.e07aframe)

        self.IDlabel.place(x=10, y=10)
        self.ID.place(x=10, y=30)
        self.thirdidlabel.place(x=150, y=10)
        self.thirdid.place(x=150, y=30)
        self.secidlabel.place(x=10, y=60)
        self.secid.place(x=10, y=80)
        self.grpcntlabel.place(x=10, y=110)
        self.grpcnt.place(x=10, y=130)
        self.msgLabel.place(x=10, y=160)
        self.message.place(x=10, y=180, width=395, height=250)
        self.launchbutton.place(x=550, y=400, width=80, height=30)

    def show(self):
        self.e07aframe.place(x=0, y=0, width=640, height=480)

    def hide(self):
        self.e07aframe.place_forget()

    def resetbutton(self):
        self.launchbutton["text"] = "Start station"
        self.launchbutton["command"] = lambda: launchstation(Station="E07a", ID=self.ID.get(),
                                                             secid=self.secid.get(), grpcnt=self.grpcnt.get(),
                                                             thirid=self.thirdid.get(),
                                                             message=self.message.get("1.0", 'end-1c'))

    def resetall(self):
        self.resetbutton()
        self.ID.delete(0, 'end')
        self.secid.delete(0, 'end')
        self.thirdid.delete(0, 'end')
        self.grpcnt.delete(0, 'end')
        self.message.delete(1.0, 'end')


class G06Frame():
    def __init__(self):
        self.title = "G06"
        self.g06frame = tk.Frame(root)

        self.IDlabel = tk.Label(self.g06frame, text="3-digit Main ID")
        self.secidlabel = tk.Label(self.g06frame, text="3-digit Secondary ID")
        self.grpcntlabel = tk.Label(self.g06frame, text="Group Count")
        self.msgLabel = tk.Label(self.g06frame, text="Message text")
        self.launchbutton = tk.Button(self.g06frame, text="Start station",
                                      command=lambda: launchstation(Station="G06",
                                                                    ID=self.ID.get(),
                                                                    secid=self.secid.get(),
                                                                    grpcnt=self.grpcnt.get(),
                                                                    message=self.message.get("1.0", 'end-1c')))

        self.ID = tk.Entry(self.g06frame)
        self.secid = tk.Entry(self.g06frame)
        self.grpcnt = tk.Entry(self.g06frame)
        self.message = tk.Text(self.g06frame)

        self.IDlabel.place(x=10, y=10)
        self.ID.place(x=10, y=30)
        self.secidlabel.place(x=10, y=60)
        self.secid.place(x=10, y=80)
        self.grpcntlabel.place(x=10, y=110)
        self.grpcnt.place(x=10, y=130)
        self.msgLabel.place(x=10, y=160)
        self.message.place(x=10, y=180, width=395, height=250)
        self.launchbutton.place(x=550, y=400, width=80, height=30)

    def show(self):
        self.g06frame.place(x=0, y=0, width=640, height=480)

    def hide(self):
        self.g06frame.place_forget()

    def resetbutton(self):
        self.launchbutton["text"] = "Start station"
        self.launchbutton["command"] = lambda: launchstation(Station="G06",
                                                             ID=self.ID.get(),
                                                             secid=self.secid.get(),
                                                             grpcnt=self.grpcnt.get(),
                                                             message=self.message.get("1.0", 'end-1c'))

    def resetall(self):
        self.resetbutton()
        self.ID.delete(0, 'end')
        self.secid.delete(0, 'end')
        self.grpcnt.delete(0, 'end')
        self.message.delete(1.0, 'end')


def setactiveframe(newframe):
    global activeframe
    if newframe == activeframe:
        pass
    else:
        activeframe.hide()
        activeframe = newframe
        activeframe.show()
        root.title("NumberStations v1 Alpha-1 - {}".format(activeframe.title))


def initstation(**kwargs):
    if kwargs.get("station") == "E11":
        chklist = [None, None, None]
        chklist[0] = tkvalidator.sggroupcheck(kwargs.get("ID"), 3, 0, "Primary ID")
        chklist[1] = tkvalidator.sggroupcheck(kwargs.get("grpcnt"), 0, 2, "Group count")
        chklist[2] = tkvalidator.multigroupcheck(kwargs.get("message"))
        for Nr in range(len(chklist)):
            if chklist[Nr] is not None:
                tkmsg.showerror("Validator Error", "File Error in check " + str(Nr))
        if False not in chklist:
            e11(kwargs.get("ID"), kwargs.get("grpcnt"), kwargs.get("message"))
        else:
            tkmsg.showerror("Validator Error", "Station could not be started - invalid input")
    elif kwargs.get("station") == "S11a":
        chklist = [None, None, None]
        chklist[0] = tkvalidator.sggroupcheck(kwargs.get("ID"), 3, 0, "Primary ID")
        chklist[1] = tkvalidator.sggroupcheck(kwargs.get("grpcnt"), 0, 2, "Group count")
        chklist[2] = tkvalidator.multigroupcheck(kwargs.get("message"))
        for Nr in range(len(chklist)):
            if chklist[Nr] is not None:
                tkmsg.showerror("Validator Error", "File Error in check " + str(Nr))
        if False not in chklist:
            s11a(kwargs.get("ID"), kwargs.get("grpcnt"), kwargs.get("message"))
        else:
            tkmsg.showerror("Validator Error", "Station could not be started - invalid input")
    elif kwargs.get("station") == "E07":
        chklist = [None, None, None, None]
        chklist[0] = tkvalidator.sggroupcheck(kwargs.get("ID"), 3, 0, "Primary ID")
        chklist[1] = tkvalidator.sggroupcheck(kwargs.get("secid"), 0, 1, "Secondary ID")
        chklist[2] = tkvalidator.sggroupcheck(kwargs.get("grpcnt"), 0, 2, "Group count")
        chklist[3] = tkvalidator.multigroupcheck(kwargs.get("message"))
        for Nr in range(len(chklist)):
            if chklist[Nr] is not None:
                tkmsg.showerror("Validator Error", "File Error in check " + str(Nr))
        if False not in chklist:
            e07(kwargs.get("ID"), kwargs.get("secid"), kwargs.get("grpcnt"), kwargs.get("message"))
        else:
            tkmsg.showerror("Validator Error", "Station could not be started - invalid input")
    elif kwargs.get("station") == "E07a":
        chklist = [None, None, None, None, None]
        chklist[0] = tkvalidator.sggroupcheck(kwargs.get("ID"), 3, 0, "Primary ID")
        chklist[1] = tkvalidator.sggroupcheck(kwargs.get("secid"), 0, 1, "Secondary ID")
        chklist[2] = tkvalidator.sggroupcheck(kwargs.get("thirdid"), 5, 0, "Third ID")
        chklist[3] = tkvalidator.sggroupcheck(kwargs.get("grpcnt"), 0, 2, "Group count")
        chklist[4] = tkvalidator.multigroupcheck(kwargs.get("message"))
        for Nr in range(len(chklist)):
            if chklist[Nr] is not None:
                tkmsg.showerror("Validator Error", "File Error in check " + str(Nr))
        if False not in chklist:
            e07a(kwargs.get("ID"), kwargs.get("secid"), kwargs.get("thirdid"), kwargs.get("grpcnt"), kwargs.get("message"))
        else:
            tkmsg.showerror("Validator Error", "Station could not be started - invalid input")
            mainbuttonchange(activeframe, "start")  # Button doesn't actually reset tho. We can leave this for now.
    elif kwargs.get("station") == "G06":
        chklist = [None, None, None, None]
        chklist[0] = tkvalidator.sggroupcheck(kwargs.get("ID"), 3, 0, "Primary ID")
        chklist[1] = tkvalidator.sggroupcheck(kwargs.get("secid"), 3, 0, "Secondary ID")
        chklist[2] = tkvalidator.sggroupcheck(kwargs.get("grpcnt"), 0, 2, "Group count")
        chklist[3] = tkvalidator.multigroupcheck(kwargs.get("message"))
        for Nr in range(len(chklist)):
            if chklist[Nr] is not None:
                tkmsg.showerror("Validator Error", "File Error in check " + str(Nr))
        if False not in chklist:
            g06(kwargs.get("ID"), kwargs.get("secid"), kwargs.get("grpcnt"), kwargs.get("message"))
        else:
            tkmsg.showerror("Validator Error", "Station could not be started - invalid input")
    else:
        tkmsg.showerror("InitStation Error", "Unknown Station in InitStation - report this bug")


def insertintoentry(Frame, textfile):
    text = open(textfile)
    lines = text.readlines()
    if lines[0] == "E11\n":
        chklist = [None, None, None]
        setactiveframe(E11)
        chklist[0] = tkvalidator.sggroupcheck(lines[1], 3, 0, "Primary ID")
        chklist[1] = tkvalidator.sggroupcheck(lines[2], 0, 2, "Group count")
        chklist[2] = tkvalidator.multigroupcheck(lines[3])
        for Nr in range(len(chklist)):
            if chklist[Nr] is not None:
                tkmsg.showerror("Validator Error", "File Error in check " + str(Nr))
        if False not in chklist:
            Frame.ID.insert(0, lines[1][:-1])
            Frame.grpcnt.insert(0, lines[2][:-1])
            Frame.message.insert('1.0', lines[3])
        else:
            tkmsg.showerror("Validator Error", "File could not be inserted - File invalid")
    elif lines[0] == "S11a\n":
        chklist = [None, None, None]
        setactiveframe(S11a)
        chklist[0] = tkvalidator.sggroupcheck(lines[1], 3, 0, "Primary ID")
        chklist[1] = tkvalidator.sggroupcheck(lines[2], 0, 2, "Group count")
        chklist[2] = tkvalidator.multigroupcheck(lines[3])
        for Nr in range(len(chklist)):
            if chklist[Nr] is not None:
                tkmsg.showerror("Validator Error", "File Error in check " + str(Nr))
        if False not in chklist:
            Frame.ID.insert(0, lines[1][:-1])
            Frame.grpcnt.insert(0, lines[2][:-1])
            Frame.message.insert('1.0', lines[3])
        else:
            tkmsg.showerror("Validator Error", "File could not be inserted - File invalid")
    elif lines[0] == "E07\n":
        chklist = [None, None, None, None]
        setactiveframe(E07)
        chklist[0] = tkvalidator.sggroupcheck(lines[1], 3, 0, "Primary ID")
        chklist[1] = tkvalidator.sggroupcheck(lines[2], 0, 1, "Secondary ID")
        chklist[2] = tkvalidator.sggroupcheck(lines[3], 0, 2, "Group count")
        chklist[3] = tkvalidator.multigroupcheck(lines[4])
        for Nr in range(len(chklist)):
            if chklist[Nr] is not None:
                tkmsg.showerror("Validator Error", "File Error in check " + str(Nr))
        if False not in chklist:
            Frame.ID.insert(0, lines[1][:-1])
            Frame.secid.insert(0, lines[2][:-1])
            Frame.grpcnt.insert(0, lines[3][:-1])
            Frame.message.insert('1.0', lines[4])
        else:
            tkmsg.showerror("Validator Error", "File could not be inserted - File invalid")
    elif lines[0] == "E07a\n":
        chklist = [None, None, None, None, None]
        setactiveframe(E07a)
        chklist[0] = tkvalidator.sggroupcheck(lines[1], 3, 0, "Primary ID")
        chklist[1] = tkvalidator.sggroupcheck(lines[3], 0, 1, "Secondary ID")
        chklist[2] = tkvalidator.sggroupcheck(lines[2], 5, 0, "Third ID")
        chklist[3] = tkvalidator.sggroupcheck(lines[4], 0, 2, "Group count")
        chklist[4] = tkvalidator.multigroupcheck(lines[5])
        for Nr in range(len(chklist)):
            if chklist[Nr] is not None:
                tkmsg.showerror("Validator Error", "File Error in check " + str(Nr))
        if False not in chklist:
            Frame.ID.insert(0, lines[1][:-1])
            Frame.thirdid.insert(0, lines[2][:-1])
            Frame.secid.insert(0, lines[3][:-1])
            Frame.grpcnt.insert(0, lines[4][:-1])
            Frame.message.insert('1.0', lines[5])
        else:
            tkmsg.showerror("Validator Error", "File could not be inserted - File invalid")
    elif lines[0] == "G06\n":
        chklist = [None, None, None, None]
        setactiveframe(G06)
        chklist[0] = tkvalidator.sggroupcheck(lines[1], 3, 0, "Primary ID")
        chklist[1] = tkvalidator.sggroupcheck(lines[2], 3, 0, "Secondary ID")
        chklist[2] = tkvalidator.sggroupcheck(lines[3], 0, 2, "Group count")
        chklist[3] = tkvalidator.multigroupcheck(lines[4])
        for Nr in range(len(chklist)):
            if chklist[Nr] is not None:
                tkmsg.showerror("Validator Error", "File Error in check " + str(Nr))
        if False not in chklist:
            Frame.ID.insert(0, lines[1][:-1])
            Frame.secid.insert(0, lines[2][:-1])
            Frame.grpcnt.insert(0, lines[3][:-1])
            Frame.message.insert('1.0', lines[4])
        else:
            tkmsg.showerror("Validator Error", "File could not be inserted - File invalid")


def savetofile():
    f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return
    if activeframe.title == "E11":
        f.write("E11\n" + activeframe.ID.get() + "\n" + activeframe.grpcnt.get() + "\n" + activeframe.message.get("1.0", 'end-1c'))
        f.close()
    elif activeframe.title == "S11a":
        f.write("S11a\n" + activeframe.ID.get() + "\n" + activeframe.grpcnt.get() + "\n" + activeframe.message.get("1.0", 'end-1c'))
        f.close()
    elif activeframe.title == "E07":
        f.write("E07\n" + activeframe.ID.get() + "\n" + activeframe.secid.get() + "\n" + activeframe.grpcnt.get() + "\n" + activeframe.message.get("1.0", 'end-1c'))
        f.close()
    elif activeframe.title == "E07a":
        f.write("E07a\n" + activeframe.ID.get() + "\n" + activeframe.thirdid.get() + "\n" + activeframe.secid.get() + "\n" + activeframe.grpcnt.get() + "\n" + activeframe.message.get("1.0", 'end-1c'))
        f.close()
    elif activeframe.title == "G06":
        f.write("G06\n" + activeframe.ID.get() + "\n" + activeframe.secid.get() + "\n" + activeframe.grpcnt.get() + "\n" + activeframe.message.get("1.0", 'end-1c'))
        f.close()


def mainbuttonchange(Frame, status):
    if status == "start":
        Frame.resetbutton()
    elif status == "stop":
        Frame.launchbutton["text"] = "Stop station"
        Frame.launchbutton["command"] = killmainstation


def killmainstation():
    mainstation.terminate()
    mainbuttonchange(activeframe, "start")


def launchstation(**kwargs):
    global mainstation
    if kwargs.get("Station") == "E11":
        mainstation = multiprocess.Process(target=lambda: initstation(station="E11",
                                                                      ID=kwargs.get("ID"),
                                                                      grpcnt=kwargs.get("grpcnt"),
                                                                      message=kwargs.get("message")))
    elif kwargs.get("Station") == "S11a":
        mainstation = multiprocess.Process(target=lambda: initstation(station="S11a",
                                                                      ID=kwargs.get("ID"),
                                                                      grpcnt=kwargs.get("grpcnt"),
                                                                      message=kwargs.get("message")))
    elif kwargs.get("Station") == "E07":
        mainstation = multiprocess.Process(target=lambda: initstation(station="E07",
                                                                      ID=kwargs.get("ID"),
                                                                      secid=kwargs.get("secid"),
                                                                      grpcnt=kwargs.get("grpcnt"),
                                                                      message=kwargs.get("message")))
    elif kwargs.get("Station") == "E07a":
        mainstation = multiprocess.Process(target=lambda: initstation(station="E07a",
                                                                      ID=kwargs.get("ID"),
                                                                      secid=kwargs.get("secid"),
                                                                      thirdid=kwargs.get("thirid"),
                                                                      grpcnt=kwargs.get("grpcnt"),
                                                                      message=kwargs.get("message")))
    elif kwargs.get("Station") == "G06":
        mainstation = multiprocess.Process(target=lambda: initstation(station="G06",
                                                                      ID=kwargs.get("ID"),
                                                                      secid=kwargs.get("secid"),
                                                                      grpcnt=kwargs.get("grpcnt"),
                                                                      message=kwargs.get("message")))
    mainstation.start()
    mainbuttonchange(activeframe, "stop")


def selectfile():
    global fileselect
    fileselect = filedialog.askopenfilename(title="Select file to process",
                                            filetypes=(("Text files", "*.txt"), ("All Files", "*.*")))
    with open(fileselect) as file:
        lines = file.readlines()
        if lines[0] == "E11\n":
            E11.resetall()
            insertintoentry(E11, fileselect)
        elif lines[0] == "E07\n":
            E07.resetall()
            insertintoentry(E07, fileselect)
        elif lines[0] == "E07a\n":
            E07a.resetall()
            insertintoentry(E07a, fileselect)
        elif lines[0] == "S11a\n":
            S11a.resetall()
            insertintoentry(S11a, fileselect)
        elif lines[0] == "G06\n":
            G06.resetall()
            insertintoentry(G06, fileselect)
        else:
            tkmsg.showerror("Error opening file", "Unsupported Station Type")


# For reasons the Main code has to be behind a test for whether the code is being run or imported.
# Else, the launchstation() function will open a duplicate of root which you have to close
# before the station actually starts
if __name__ == "__main__":
    # The Window
    root = tk.Tk()
    root.title("NumberStations v1 Alpha-1")
    root.geometry("640x480")

    # The Awesome Menu
    menubar = tk.Menu(root)

    # File
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Load File", command=selectfile)
    filemenu.add_command(label="Save File", command=savetofile)
    menubar.add_cascade(label="File", menu=filemenu)

    # Station
    stationmenu = tk.Menu(menubar, tearoff=0)
    stationmenu.add_command(label="E11", command=lambda: setactiveframe(E11))
    stationmenu.add_command(label="E07", command=lambda: setactiveframe(E07))
    stationmenu.add_command(label="E07a", command=lambda: setactiveframe(E07a))
    stationmenu.add_command(label="S11a", command=lambda: setactiveframe(S11a))
    stationmenu.add_command(label="G06", command=lambda: setactiveframe(G06))
    menubar.add_cascade(label="Station", menu=stationmenu)
    # Help
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About NumberStations",
                         command=lambda: tkmsg.showinfo("About", "NumberStations v1 Alpha-2\nProgrammed by ZapdoZ"))
    menubar.add_cascade(label="Help", menu=helpmenu)

    # Set Frames and default
    E11 = E11Frame()
    E07 = E07Frame()
    E07a = E07aFrame()
    S11a = S11aFrame()
    G06 = G06Frame()
    activeframe = E11
    setactiveframe(E07)

    # More Main Window config
    root.title("NumberStations v1 Alpha-2 - {}".format(activeframe.title))
    root.resizable(False, False)
    root.config(menu=menubar)
    root.mainloop()
