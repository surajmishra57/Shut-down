from tkinter import *
from tkinter.ttk import Combobox
import os
from tkinter import messagebox
from tkinter.font import Font

def Cancel():
    root.destroy()

def Clear():
    combo.set("Select")
    hour.set('H')
    Hour.set('H')
    mint.set('M')
    Mint.set('M')
    sec.set('S')
    Sec.set('S')
def final():
    chack=["H",'0','1','2','3','4','5','6','7','8','9']
    chackm=["M",'0','1','2','3','4','5','6','7','8','9']
    chacks=["S",'0','1','2','3','4','5','6','7','8','9']
    Action=combo.get()
    h=hour.get()
    H=Hour.get()
    m=mint.get()
    M=Mint.get()
    s=sec.get()
    S=Sec.get()
    print(type(H))
    if Action not in  ("Shut down","Restart","Logout"):
        messagebox.showerror("Error","Select Options first")
        return 0
    if h not in chack:
        messagebox.showerror("Error","Invalid hour")
        return 0
    if H not in chack:
        messagebox.showerror("Error","Invalid hour")
        return 0
    if m not in chackm:
        messagebox.showerror("Error","Invalid minute")
        return 0
    if M not in chackm:
        messagebox.showerror("Error","Invalid minute")
        return 0
    if s not in chacks:
        messagebox.showerror("Error","Invalid second")
        return 0
    if S not in chacks:
        messagebox.showerror("Error","Invalid second")
        return 0
    if h=='H':
        h='0'
    if H=='H':
        H='0'
    if m=='M':
        m='0'
    if M=='M':
        M='0'
    if s=='S':
        s='0'
    if S=='S':
        S='0'
    Ghanta=(h+H)
    Minate=(m+M)
    Seconde=(s+S)
    HOUR=int(Ghanta)
    MIN=int(Minate)
    SEC=int(Seconde)
    if HOUR ==0 and MIN==0 and SEC==0:
        if Action=='Shut down':
            result=messagebox.askquestion("SHOW INFO","System will shut down Immediate")
            if result=='yes':
                os.system("shutdown -s -t 00")
                root.destroy()
        if Action=='Restart':
            result=messagebox.askquestion("SHOW INFO","System will Restart Immediate")
            if result=='yes':
                os.system("shutdown -r -t 00")
                root.destroy()
        if Action=='Logout':
            result=messagebox.askquestion("SHOW INFO","System will LogOut Immediate")
            if result=='yes':
                os.system("shutdown -l -t 00")
                root.destroy()
            
    TIME=HOUR*60
    TIME=TIME+MIN
    Timesec=TIME*60
    Timesec=Timesec+SEC
    if Action=="Shut down":
        command="shutdown -s -t "
        Shut=command+str(Timesec)
        result=messagebox.askquestion("TIME SET","System will down in %d Hour %d Min %d Sec"%(HOUR,MIN,SEC))
        if result=='yes':
            os.system(Shut)
            root.destroy()
    if Action=="Restart":
        commande="shutdown -r -t "
        SRestart=commande+str(Timesec)
        result=messagebox.askquestion("TIME SET","System will Restart in %d Hour %d Min %d Sec"%(HOUR,MIN,SEC))
        if result=='yes':
            os.system(SRestart)
            root.destroy()
    if Action=="Logout":
        comm="shutdown -l -t "
        Lock=comm+str(Timesec)
        result=messagebox.askquestion("TIME SET","System will LogOut in %d Hour %d Min %d Sec"%(HOUR,MIN,SEC))
        if result=='yes':
            os.system(Lock)
            root.destroy()
            
    




    
root=Tk()
root.title("Computer Timer")
root.geometry("600x600+350+50")
fontsize=3
frm=Frame(root,width=600,height=800,bg="lightblue")
canvas=Canvas(frm,width=300,height=190,bg="black")
canv=Canvas(frm,width=300,height=15,bg="white")
can=Canvas(frm,width=300,height=15,bg="black")
computer=Label(canv,text="COMPUTER",font=fontsize,bg="white")
computer.place(x=110,y=0)
canvas.place(x=150,y=50)
canv.place(x=150,y=240)
can.place(x=150,y=270)
h=Label(frm,text="HOUR",font=fontsize,bg="lightblue")
h.place(x=210,y=390)
m=Label(frm,text="MINUTE",font=fontsize,bg="lightblue")
m.place(x=280,y=390)
s=Label(frm,text="SECOND",font=fontsize,bg="lightblue")
s.place(x=360,y=390)

V=["Shut down","Restart","Logout"]
combo=Combobox(frm,values=V,width=20)
combo.set("Select")
combo.place(x=230,y=350)

H=list(range(0,10))
hour=Combobox(frm,values=H,width=2)
hour.place(x=200,y=410)
hour.set("H")
Hour=Combobox(frm,values=H,width=2)
Hour.place(x=235,y=410)
Hour.set("H")

mint=Combobox(frm,values=H,width=2)
mint.set("M")
Mint=Combobox(frm,values=H,width=2)
Mint.set("M")
mint.place(x=280,y=410)
Mint.place(x=315,y=410)

sec=Combobox(frm,values=H,width=2)
sec.set("S")
Sec=Combobox(frm,values=H,width=2)
Sec.set("S")
sec.place(x=360,y=410)
Sec.place(x=395,y=410)

button=Button(frm,text=" Done ",bg="gray",command=final)
button.place(x=290,y=510)
clearbutton=Button(frm,text=" Clear ",bg="gray",command=Clear)
clearbutton.place(x=200,y=510)
Cancelbutton=Button(frm,text=" Cancel ",bg="gray",command=Cancel)
Cancelbutton.place(x=380,y=510)
frm.pack()

root.mainloop()

