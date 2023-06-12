class Point:
    a = 20
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __del__(self):
    #     print("Mushaobs Destructori")

    def get(self):
        print(self.x, self.y)

p= Point(30,40)
p.get()
print(Point.a)
print(p.x)

class Stack:
    def __init__(self, a):
        self.a = a

    def push(self, a):
        self.a.append(a)
        print(self.a)

    def pop(self):
        self.a.pop()
        print(self.a)

    def top(self):
        return self.a[len(self.a)-1]

     def count(self):
         return len(self.a)

      def isempty(self):
        if len(self.a)==0:
            return True


c = Stack([1,2,3])
c.push(56)
c.push(34)
c.top()
#c.isempty()

class Rigi:
    def __init__(self,a):
        self.a=a

    def push(self,a):
        return print(self.a.insert(0,a))

    def pop(self):
        return self.a.pop(0)

    def back(self):
        return print(self.a[0])

     def count(self):
         return len(self.a)

      def isempty(self):
        if len(self.a)==0:
            return True

rigi = Rigi([1,2,3])
rigi.push(5)
#rigi.pop()
rigi.back()
#rigi.count()
#rigi.isempty()

class Hashtable:
    def __init__(self):
        self.a = []
        self.b = []

    def getValue(self,a):
        try:
            i = self.a.index(a)
            return print(self.b[i])
        except:
            print("Ar arsebobs")

    def find(self, x):
        if self.a.count(x) == 0:
            print("ar arsebobs")
            return False
        else:
            return True

    def add(self,x,y):
        if(self.a.count(x) == 0):
            self.a.append(x)
            self.b.append(y)
            print("Shetanilia", x, y)
        else:
            print("Dakavebulia key")


    def remove(self,key):
        if (self.find(key)==True):
            i = self.a.index(key)
            self.a.pop(i)
            self.b.pop(i)
            print("Waishala", key)

htable = Hashtable()
htable.add("f",4)
htable.add("f",4)
htable.getValue("c")
htable.add("f",4)
htable.find("5")
htable.remove("a")
print(htable.a,htable.b)

# მემკვიდრეობა
class A:
    pass

# # ქვეკლასი
class B(A):
    pass

class Person:
    def __init__(self,n,l):
        self.name=n
        self.lastname=l

    def getinto(self):
        print(self.name,self.lastname)

class Student(Person):
    def __init__(self,name,lastname,spec):
        Person.__init__(self,name,lastname)
        self.spec=spec

    def getinto(self):
        print("სახელი: {0} გვარი: {1} სპეციალობა: {2}".format(self.name,self.lastname,self.spec))


studenti=Student("გ","მ","სტუდენტი")
studenti.getinto()

class Vist:
    def __init__(self):
        self.a = []

    def push(self, a):
        self.a.append(a)

    def pop(self):
        return self.a.pop()

    def top(self):
        return self.a[len(self.a)-1]

    def count(self):
        return len(self.a)

    def isempty(self):
        if len(self.a)==0:
            return True

class Stack(Vist):
    def push(self, a):
        super().push(a)
    def getit(self):
        print(self.a)



test = Stack()
test.push("50")
test.push("500")
test.push("3123")
print(test.top())
test.getit()

# მრავალობითი მემკვიდრეობა
class A:
    def info(self):
        print("A")

class B:
    def info(self):
        print("B")

class C(A,B):
    pass

C1=C()
C1.info()

# გრაფიკული ინტერფეისი
import tkinter

form=tkinter.Tk()

def click(value):
    print("Log:",value)
    # text.set("hello world")
    if( int(text.get()) & int(text2.get())):
        result=int(text.get())+int(text2.get())
        text3.set(result)
        print("Result:",result)
    print("Email:",text.get())
    print("Password:",text2.get())

# input value
text=tkinter.StringVar()
text2=tkinter.StringVar()
text3=tkinter.StringVar()

# eMail
Label=tkinter.Label(text="eMail")
Label.grid(row=1,column=1)

# input
Input=tkinter.Entry(width="30", textvariable=text, bg="white")
Input.place(x="30",y="30")
Input.grid(row=2,column=1)

# Password
Label2=tkinter.Label(text="Password")
Label2.grid(row=3,column=1)

# input2
Input2=tkinter.Entry(width="30", textvariable=text2, bg="white")
Input2.place(x="30",y="55")
Input2.grid(row=4,column=1)

# ღილაკი
button=tkinter.Button(text="add",fg="black", bg="red", command=lambda:click(value="Clicked !"))
button.place(x="30",y="80")
button.grid(row=5,column=1)

# Result
Input3=tkinter.Entry(width="30", textvariable=text3, bg="white")
Input3.place(x="30",y="55")
Input3.grid(row=6,column=1)

# გაშვება
form.geometry("500x400")
form.mainloop()
