from sre_parse import WHITESPACE
from tkinter import*
main_window= Tk()
main_window.title("SCRA GUI")
main_window.minsize(width=200,height=300)
main_window.maxsize(width=700,height=555)
l1=Label(main_window,text="SCRA Robot Control",font=('Times', 24))
l1.place(x=180,y=10)
#left side
l2=Label(main_window,text="Forward Kinematics", font=('Times', 16))
l2.place(x=60,y=70)
#j1
def zeroFunction() :
    print('0 button is clicked.')

b1=Button(main_window,text=0,bg="blue",width=6,height=0,fg="white",command=zeroFunction)
b1.place(x=60,y=120)

def blankFunction() :
    print('blank button is clicked.')

b1=Button(main_window,bg="dark blue",width=18,height=0,command=blankFunction)
b1.place(x=110,y=120)

def jogFunction() :
    print('JOG- button is clicked.')

b1=Button(main_window,text="JOG-",bg="dark blue",width=6,height=1,fg="white",command=jogFunction)
b1.place(x=60,y=165)

def oneFunction() :
    print('1 button is clicked.')

b1=Button(main_window,text=1,bg="dark blue",width=4,height=0,fg="white",command=oneFunction)
b1.place(x=132,y=167)

def jog1Function() :
    print('JOG+ button is clicked.')

b1=Button(main_window,text="JOG+",bg="dark blue",width=6,height=1,fg="white",command=jog1Function)
b1.place(x=190,y=165)
#j2 buttons

b1=Button(main_window,text=0,bg="blue",width=12,height=0,fg="white",command=zeroFunction)
b1.place(x=60,y=210)

b1=Button(main_window,bg="dark blue",width=12,height=0,command=blankFunction)
b1.place(x=150,y=210)

b1=Button(main_window,text="JOG-",bg="dark blue",width=6,height=1,fg="white",command=jogFunction)
b1.place(x=60,y=255)

b1=Button(main_window,text=1,bg="dark blue",width=4,height=0,fg="white",command=oneFunction)
b1.place(x=132,y=257)

b1=Button(main_window,text="JOG+",bg="dark blue",width=6,height=1,fg="white",command=jog1Function)
b1.place(x=190,y=255)
#j3 buttons

b1=Button(main_window,text=0,bg="blue",width=12,height=0,fg="white",command=zeroFunction)
b1.place(x=60,y=310)

b1=Button(main_window,bg="dark blue",width=12,height=0,command=blankFunction)
b1.place(x=150,y=310)

b1=Button(main_window,text="JOG-",bg="dark blue",width=6,height=1,fg="white",command=jogFunction)
b1.place(x=60,y=355)

b1=Button(main_window,text=1,bg="dark blue",width=4,height=0,fg="white",command=oneFunction)
b1.place(x=132,y=357)

b1=Button(main_window,text="JOG+",bg="dark blue",width=6,height=1,fg="white",command=jog1Function)
b1.place(x=190,y=355)
#z buttons

def hundredFunction() :
    print('100 button is clicked.')

b1=Button(main_window,text=100,bg="blue",width=18,height=0,fg="white",command=hundredFunction)
b1.place(x=60,y=410)

b1=Button(main_window,bg="dark blue",width=6,height=0,command=blankFunction)
b1.place(x=190,y=410)

def submitFunction() :
    print('Submit button is clicked.')

b1=Button(main_window,text="JOG-",bg="dark blue",width=6,height=1,fg="white",command=jogFunction)
b1.place(x=60,y=455)

b1=Button(main_window,text=1,bg="dark blue",width=4,height=0,fg="white",command=oneFunction)
b1.place(x=132,y=457)

b1=Button(main_window,text="JOG+",bg="dark blue",width=6,height=1,fg="white",command=jog1Function)
b1.place(x=190,y=455)

l3=Label(main_window,text="J1",font=('Times', 30))
l3.place(x=10,y=130)
l3=Label(main_window,text="J2",font=('Times', 30))
l3.place(x=10,y=220)
l3=Label(main_window,text="J3",font=('Times', 30))
l3.place(x=10,y=320)
l3=Label(main_window,text="Z",font=('Times', 30))
l3.place(x=10,y=420)
#rightside
l2=Label(main_window,text="Inverse Kinematics", font=('Times', 16))
l2.place(x=450,y=70)
l3=Label(main_window,text="X:365",font=('Times', 18))
l3.place(x=380,y=200)
l3=Label(main_window,text="Y:0",font=('Times', 18))
l3.place(x=480,y=200)
l3=Label(main_window,text="Z:100",font=('Times', 18))
l3.place(x=580,y=200)
l3=Label(main_window,text="Gripper",font=('Times', 16))
l3.place(x=480,y=280)
l3=Label(main_window,text="CLOSE",font=('Times', 16))
l3.place(x=380,y=320)
l3=Label(main_window,text="OPEN",font=('Times', 16))
l3.place(x=580,y=320)
l3=Label(main_window,text="Speed",font=('Times', 14))
l3.place(x=410,y=488)
l3=Label(main_window,text="Acceleration",font=('Times', 14))
l3.place(x=550,y=488)
l3=Label(main_window,text="Last saved position",font=('Times', 10))
l3.place(x=335,y=408)
l3=Label(main_window,text="None",font=('Times', 10))
l3.place(x=335,y=425)
#right buttons

b1=Button(main_window,bg="dark blue",width=6,height=0,fg="white",command=blankFunction)
b1.place(x=400,y=160)

b1=Button(main_window,bg="dark blue",width=6,height=0,fg="white",command=blankFunction)
b1.place(x=500,y=160)

b1=Button(main_window,bg="dark blue",width=6,height=0,fg="white",command=blankFunction)
b1.place(x=600,y=160)

def moveFunction() :
    print('MOVE TO POSITION button is clicked.')

b1=Button(main_window,text="MOVE TO POSITION",bg="dark blue",width=20,height=1,fg="white",command=moveFunction)
b1.place(x=450,y=240)

b1=Button(main_window,text="100",bg="blue",width=15,height=0,fg="white",command=hundredFunction)
b1.place(x=455,y=320)

def saveFunction() :
    print('SAVE POSITION button is clicked.')

b1=Button(main_window,text="SAVE POSITION",bg="dark blue",width=19,height=2,fg="white",command=saveFunction)
b1.place(x=335,y=360)

def runFunction() :
    print('RUN PROGRAM button is clicked.')

b1=Button(main_window,text="RUN PROGRAM",bg="dark blue",width=19,height=2,fg="white",command=runFunction)
b1.place(x=525,y=360)

def updateFunction() :
    print('(UPDATE) button is clicked.')

b1=Button(main_window,text="(UPDATE)",bg="dark blue",width=16,height=1,fg="white",command=updateFunction)
b1.place(x=530,y=410)

def clearFunction() :
    print('(CLEAR) button is clicked.')

b1=Button(main_window,text="(CLEAR)",bg="dark blue",width=13,height=1,fg="white",command=clearFunction)
b1.place(x=355,y=452)

def fiveFunction() :
    print('500 button is clicked.')

b1=Button(main_window,text="500",bg="dark blue",width=20,height=0,fg="white",command=fiveFunction)
b1.place(x=355,y=520)

b1=Button(main_window,text="500",bg="dark blue",width=20,height=0,fg="white",command=fiveFunction)
b1.place(x=530,y=520)
main_window.mainloop()



