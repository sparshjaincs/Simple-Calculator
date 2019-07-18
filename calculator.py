from tkinter import *
import math


class cal:
    def __init__(self):
        self.total=0
        self.new_num=True
        self.current=""
        self.button=[]
        self.op_pending=False
        self.op=""
        self.eq = False
    def interface(self):
        self.top=Tk()
        self.top.geometry("330x490+400+200")
        self.top.configure(background="#333")
        self.top.resizable(False,False)
        self.top.title("CALCULATOR")
        obj1.frame()
        obj1.text()
        obj1.button_1()
        self.top.mainloop()
    def frame(self):
        self.frame1=Frame(self.top,width=400,height=100,bd=0,bg="#003")
        self.frame1.place(relx=0,rely=0)
        self.frame2=Frame(self.top,width=400,height=400,bd=0,bg="#000")
        self.frame2.place(relx=0,rely=.21)
    def button_1(self):
        number='789456123'
        i=0
        for j in range(1,4):
            for k in range(3):
                self.button.append(Button(self.frame2,width=5,height=4,text=number[i],padx=5,pady=5,fg="white",font=("arial",8,"bold")))
                self.button[i]["bg"]="#123456"
                self.button[i].grid(row=j,column=k,padx=1,pady=1)
                self.button[i]["command"]= lambda x=number[i]:obj1.num_press(x)
                i=i+1
        self.bttn_0 = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "0",fg="white",font=("arial",8,"bold"),bg="steel blue")
        self.bttn_0["command"] = lambda: obj1.num_press(0)
        self.bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)
        div = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "/",fg="white",font=("arial",8,"bold"),bg="steel blue")
        div["command"] = lambda: obj1.operation("divide")
        div.grid(row = 1, column = 3, padx=1, pady = 1)
        
        mult = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "x",fg="white",font=("arial",8,"bold"),bg="steel blue")
        mult["command"] = lambda: obj1.operation("times")
        mult.grid(row = 2, column = 3,  padx=1, pady = 1)
        minus = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "-",fg="white",font=("arial",8,"bold"),bg="steel blue")
        minus["command"] = lambda: obj1.operation("minus")
        minus.grid(row = 3, column = 3, padx=1, pady = 1)
        add = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "+",fg="white",font=("arial",8,"bold"),bg="steel blue")
        add["command"] = lambda: obj1.operation("add")
        add.grid(row = 4, column = 3,  padx=1, pady = 1)
        power = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "^",fg="white",font=("arial",8,"bold"),bg="orange")
        power["command"] = lambda: obj1.operation("raise")
        power.grid(row=2,column = 4,padx=1,pady=1)
        rootof = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "y-\/x",fg="white",font=("arial",8,"bold"),bg="orange")
        rootof["command"] = lambda: obj1.operation("rootof")
        rootof.grid(row=2, column=5, padx=1, pady=1)
        fact = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "!",fg="white",font=("arial",8,"bold"),bg="orange")
        fact["command"] = lambda: obj1.operation("fact")
        fact.grid(row=3,column=4, padx=1, pady=1)
        loge = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "ln",fg="white",font=("arial",8,"bold"),bg="orange")
        loge["command"] = lambda: obj1.operation("ln")
        loge.grid(row=3, column=5, padx=1, pady=1)
        log10 = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "log",fg="white",font=("arial",8,"bold"),bg="orange")
        log10["command"]= lambda: obj1.operation("log")
        log10.grid(row=4, column=4, padx=1 , pady=1)
        sine = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "sin",fg="white",font=("arial",8,"bold"),bg="orange")
        sine["command"]=lambda: obj1.operation("sine")
        sine.grid(row=5,column=0,padx=1,pady=1)
        cosine = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "cos",fg="white",font=("arial",8,"bold"),bg="orange")
        cosine["command"]=lambda: obj1.operation("cosine")
        cosine.grid(row=5,column=1,padx=1,pady=1)
        tangent = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "tan",fg="white",font=("arial",8,"bold"),bg="orange")
        tangent["command"]=lambda: obj1.operation("tangent")
        tangent.grid(row=5,column=2,padx=1,pady=1)
        exponent = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "e^x",fg="white",font=("arial",8,"bold"),bg="orange")
        exponent["command"]=lambda: obj1.operation("exp")
        exponent.grid(row=5,column=3,padx=1,pady=1)
        inv = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "1/x",fg="white",font=("arial",8,"bold"),bg="orange")
        inv["command"] = lambda: obj1.operation("inv")
        inv.grid(row=5,column=4,padx=1,pady=1)
        point = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = ".",fg="white",font=("arial",8,"bold"),bg="steel blue")
        point["command"] = lambda: obj1.num_press(".")
        point.grid(row = 4, column = 1, padx=1, pady = 1)
        neg= Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "+/-",fg="white",font=("arial",8,"bold"),bg="steel blue")
        neg["command"] = obj1.sign
        neg.grid(row = 4, column = 2,  padx=1, pady = 1)
        clear = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "C",fg="white",font=("arial",8,"bold"),bg="red")
        clear["command"] = obj1.clear
        clear.grid(row = 1, column = 4,  padx=1, pady = 1)
        all_clear = Button(self.frame2,height =4,width=5,padx=5, pady = 5, text = "AC",fg="white",font=("arial",8,"bold"),bg="red")
        all_clear["command"] = obj1.all_clear
        all_clear.grid(row = 1, column = 5, padx=1, pady = 1)
        equals = Button(self.frame2,height =9,width=5,padx=5, pady = 5, text = "=",fg="white",font=("arial",8,"bold"),bg="#123456")
        equals["command"] = obj1.calc_total
        equals.grid(row = 4, column = 5,columnspan=1,rowspan=2,padx=1, pady = 1)
                   
                                   
    def text(self):
        self.entry1=Entry(self.frame1,width=25,font=("arial",16,"bold"),justify=RIGHT,bd=2,relief=RAISED)
        self.entry1.place(relx=.03,rely=.4)
    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(self.entry1.get())
    def num_press(self,num):
        self.eq = False
        self.temp1=self.entry1.get()
        self.temp2=str(num)
        if self.new_num:
            self.current=self.temp2
            self.new_num=False
        else:
            if self.temp2==".":
                if self.temp2 in self.temp:
                    return
            self.current=self.temp1+self.temp2
        self.display(self.current)
    def operation(self,op):
        self.current=float(self.current)
        if self.op_pending:
            obj1.do_sum(self.current)
        elif not self.eq:
            self.total=self.current
        self.new_num=True
        self.op=op
        self.eq=False
        self.op_pending=True
    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True
    def all_clear(self):
        self.clear()
        self.total = 0
    def sign(self):
        self.eq = False
        self.current = -(float(self.entry1.get()))
        self.display(self.current)
    def display(self,value):
        self.entry1.delete(0, END)
        self.entry1.insert(0, value)
        
    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "raise":
            self.total = self.total ** self.current
        if self.op == "rootof":
            self.total = self.total ** (1/self.current)
        if self.op == "fact":
            self.total=int(self.entry1.get())
            self.total=math.factorial(self.total)
        if self.op == "ln":
            self.total = math.log(self.total)
        if self.op == "log":
            self.total=math.log(self.total,10)
        if self.op == "sine":
            self.total=math.sin(self.total)
        if self.op == "cosine":
            self.total = math.cos(self.total)
        if self.op == "tangent":
            self.total = math.tan(self.total)
        if self.op == "exp":
            self.total = math.exp(self.total)
        if self.op == "inv":
            self.total = 1/self.total
        self.new_num = True
        self.op_pending = False
        self.display(self.total)


obj1=cal()
obj1.interface()
    
