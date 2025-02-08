from tkinter import *
from tkinter import ttk

#C:\Users\abdelkabir\Desktop\My_Project\My_Project\calcolator\Calcolator_1.py
root=Tk()
root.geometry('302x372+300+100')
root.config(background='white')
root.resizable(False,False)
root.overrideredirect(False)

frame1=LabelFrame(root,bg='white',width=297,height=110,bd=0,highlightbackground='#AEBAFC',highlightcolor='red',highlightthickness=1)
frame1.place(x=2,y=4)

entry_0=Entry(frame1,bg='white',font=('tajwal',18),bd=0)
entry_0.place(x=2,y=1)

label1=Label(frame1,text='',bg='white')
label1.place(x=2,y=60)

b=Button(frame1,text='ㆁ',font=16,bd=0,bg='white')
b.place(x=265,y=1)

var110=StringVar()
color_var='#F7F7F7'
click_color='#A9A9A9'
nomber_color='#5B5B5B'
color_var1='#FCFCFC'
cadr='#BFBFBF'
cadr1='#97FFBA'

def Cal(N,label):
    label.config(bg=click_color,fg='green')
    def rc():
        label.config(bg=color_var,fg=nomber_color)
    root.after(50,rc)
    entry_0.insert(END,N)
    try:
        E_Qual()
        label1.config(fg='#b7b7b7',font=('tajwal',10))
    except:
        label1.config(text='')
        
def Delete():
    b18.config(bg=click_color)
    def rc2():
        b18.config(bg=color_var)
    root.after(50,rc2)
    var_1=entry_0.get()
    Var_2=len(var_1)
    entry_0.delete(Var_2-1)
    label1.config(text='',fg='blue')
def Clear():
    b17.config(bg=click_color)
    def rc2():
        b17.config(bg=color_var)
    root.after(50,rc2)
    entry_0.delete(0,END) 
    label1.config(text='',fg='blue')
def E_Qual(): 
    def Calcolator(x):
        try:
            if '+' in x:
                try:
                    v=x.index('+')
                    v1=''.join(x[:v])
                    v2=''.join(x[v+1:])
                    var_4=int(v1)+int(v2)
                    return var_4

                except:
                    v=x.index('+')
                    v1=''.join(x[:v])
                    v2=''.join(x[v+1:])
                    var_4=float(v1)+float(v2)
                    return var_4      
            elif '-' in x:
                try:
                    v=x.index('-')
                    v1=''.join(x[:v])
                    v2=''.join(x[v+1:])
                    var_4=int(v1)-int(v2)
                    return var_4
                except:
                    v=x.index('-')
                    v1=''.join(x[:v])
                    v2=''.join(x[v+1:])
                    var_4=float(v1)-float(v2)
                    return var_4     
            elif 'x' in x:
                try:
                    v=x.index('x')
                    v1=''.join(x[:v])
                    v2=''.join(x[v+1:])
                    var_4=int(v1)*int(v2)
                    return var_4
                except:
                    v=x.index('x')
                    v1=''.join(x[:v])
                    v2=''.join(x[v+1:])
                    var_4=float(v1)*float(v2)
                    return var_4      
            elif '/' in x:
                try:
                    v=x.index('/')
                    v1=''.join(x[:v])
                    v2=''.join(x[v+1:])
                    var_4=int(v1)/int(v2)
                    return var_4
                except:
                    v=x.index('/')
                    v1=''.join(x[:v])
                    v2=''.join(x[v+1:])
                    var_4=float(v1)/float(v2)
                    return var_4  
        except:
            pass 
    def Isharat(List): 
        List_2=[]
        for row in List:
            if row == '-' :
                List_2.append(row)
            if row == '+' :
                List_2.append(row)
            if row == 'x' :
                List_2.append(row)
            if row == '/' :
                List_2.append(row)
            else:
                pass
        return List_2
    def Nambers(List1):
        list_y=[]
        list_x=List1
        x=''
        for row in list_x:
            if row == '+':
                list_y.append(x)
                x=''
            elif row == '-':
                list_y.append(x)
                x=''
            elif row == 'x':
                list_y.append(x)
                x=''
            elif row == '/':
                list_y.append(x)
                x=''
            else:
                x+=row
        if List_1[-1] !=  ' '  :
            xx=True
            c=-1
            while xx:
                if   List_1[c] != '+' and List_1[c] != '-' and List_1[c] != 'x' and List_1[c] != '/':
                    c-=1
                else:
                    y=''.join(List_1[c+1:])
                    list_y.append(y)
                    xx=False
        return list_y
    def Eqoual(list2,list3):
        if   list2 ==[]:
            list4='{}'.format(list3[0])
            return list4  
        else:   
            Eqoual=''
            w=0
            for x in list2:              
                if Eqoual=='':
                    vv=[list3[w],'{}'.format(x),list3[w+1]]
                    w+=1
                    Eqoual=Calcolator(vv)
                else:
                    vv1=['{}'.format(Eqoual),'{}'.format(x),list3[w+1]]
                    Eqoual=''
                    w+=1
                    Eqoual=Calcolator(vv1)         
            return Eqoual
    try:
        List_1=[]
        List_1.extend(entry_0.get()) 
        List_2=Isharat(List_1)
        List_3=Nambers(List_1)
        x1=True
        while x1 :
            if 'x' in List_2:
                var10=List_2.index('x')
                var11=List_3[var10],List_2[var10],List_3[var10+1]
                var12=Calcolator(var11)
                List_2.remove(List_2[var10])
                List_3.remove(List_3[var10])
                List_3.remove(List_3[var10])
                List_3.insert(var10,'{}'.format(var12))
            else:
                x1=False
        x2=True
        while x2 :
            if '/' in List_2:
                var13=List_2.index('/')
                var14=List_3[var13],List_2[var13],List_3[var13+1]
                var15=Calcolator(var14)
                List_2.remove(List_2[var13])
                List_3.remove(List_3[var13])
                List_3.remove(List_3[var13])
                List_3.insert(var13,'{}'.format(var15))
            else:
                x2=False   
        Eq=Eqoual(List_2,List_3)
        fd='{}'.format(Eq)
        v=[]
        for row in fd:
            v.append(row)
        try:   
            if v[-1]=='0' and v[-2]=='.':
                v.pop()
                v.pop()
                nat=''.join(v)
                label1.config(text=f'= {nat}',fg='blue',font=('tajwal',16,'bold'))
                var110.set(nat)
            else:
                label1.config(text=f'= {Eq}',fg='blue',font=('tajwal',16,'bold'))
                var110.set(Eq)
        except:

            label1.config(text=f'= {Eq}',fg='blue',font=('tajwal',16,'bold'))
            var110.set(Eq)
        # print(List_1) # the Entry
        # print(List_2) # isharat
        # print(List_3) # numbers
        # print(Eqoual) # natija
    except:
        Ls=entry_0.get()
        try:
            try:
                Eq = int(Ls)
                label1.config(text=f'= {Ls}',fg='blue',font=('tajwal',16,'bold')) 
                var110.set(Ls)
            except:
                pass
            try:
                Eq = float(Ls)
                label1.config(text=f'= {Ls}',fg='blue',font=('tajwal',16,'bold')) 
                var110.set(Ls)
            except:
                  label1.config(text='Enter the right nombers',fg='red')
                  var110.set(Ls)
        except:     
            pass
Datatimer=[]
Datatimer1=[]

def Timer():
    Datatimer.append(entry_0.get())
    Datatimer1.append(var110.get())

def X():
    root.config(bg='white')
    frame1.config(bg='white')
    entry_0.config(bg='white')
    b.config(bg='white')
    label1.config(bg='white', fg='blue')
    FrameTimer1.destroy()
    b.config(state=NORMAL)

def Frame_Timer():
    b.config(state=DISABLED)
    global FrameTimer1
    FrameTimer1=LabelFrame(root,bg='white',bd=0)
    FrameTimer1.place(x=0,y=115,width=303,height=256)
    Frame1=Frame(FrameTimer1)
    Frame1.pack(side=RIGHT,fill=Y,expand=1)
    my_canvas=Canvas(FrameTimer1,bg='white',bd=0,confine=True)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=True)



    root.config(bg='#8a7171')
    frame1.config(bg='#8a7171')
    entry_0.config(bg='#8a7171')
    b.config(bg='#8a7171')
    label1.config(bg='#8a7171',fg='#000066')
    



    y_scrollbar=ttk.Scrollbar(Frame1,orient=VERTICAL,command=my_canvas.yview)
    y_scrollbar.pack(fill=Y,expand=True)
    my_canvas.config(yscrollcommand=y_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))
    second_frame=Frame(my_canvas,bg='white')
    my_canvas.create_window((0,0),window=second_frame , anchor=NW)

    def create_frame(row1,text,commandcal):
        Framevar=Frame(second_frame,width=286,height=50,bg='white')
        Framevar.pack(pady=1)
        l1=Label(Framevar,text=row1,bg='white',fg='#313131',font=('tajwal',10,'bold'))
        l1.place(x=10,y=2)
        l2=Label(Framevar,text=text,bg='white',fg='#746cff',font=('tajwal',14,'bold'))
        l2.place(x=10,y=20)
        def enter_color(event):
            l1.config(bg='#C6D9FF')
            l2.config(bg='#C6D9FF')
            Framevar.config(bg='#C6D9FF')   
        def leave_color(event):
            Framevar.config(bg='white')
            l1.config(bg='white')
            l2.config(bg='white')
        def setcal(event):
            entry_0.delete(0,END) 
            label1.config(text='',fg='blue')
            entry_0.insert(END,f'{commandcal}')
            X()
        Framevar.bind('<Enter>',enter_color)
        Framevar.bind('<Leave>',leave_color)
        Framevar.bind('<ButtonRelease-1>',setcal)
    if not Datatimer:
        Label(second_frame,text='\t     there is no hestory yet !',bg='white').pack(pady=5)
    else:
        x1=0  
        for row in Datatimer:
            create_frame(row,'='+Datatimer1[x1],row)
            x1+=1
    b100=Label(FrameTimer1,bg='white',text=' x ',font=('tajwal',10),highlightthickness=1,highlightbackground='white')
    b100.place(x=263,y=2)
    def change1_color(event):
        b100.config(bg='#FFE6E6',highlightbackground='#FEC4C4')
    def reste1_color(event):
        b100.config(bg='white',highlightbackground='white')
    def Xs(event):
        X()
      
    b100.bind('<Enter>', change1_color)
    b100.bind('<Leave>',reste1_color)
    b100.bind('<ButtonRelease-1>',Xs)

def wi(event):
    try:
        FrameTimer1.destroy()
        b.config(state=NORMAL)
    except:
        pass
b.config(command=Frame_Timer)

def E_Qual1():
    b16.config(bg='#6F9FFF')
    def rc1():
        b16.config(bg=color_var)
    root.after(50,rc1)
    E_Qual()
    Timer()
    

b1=Label(root,text=1,bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b1.place(x=2,y=120)
b2=Label(root,text=2,bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b2.place(x=77,y=120)
b3=Label(root,text=3,bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b3.place(x=152,y=120)
b4=Label(root,text='/',bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b4.place(x=227,y=120)
b5=Label(root,text=4,bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b5.place(x=2,y=170)
b6=Label(root,text=5,bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b6.place(x=77,y=170)
b7=Label(root,text=6,bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b7.place(x=152,y=170)
b8=Label(root,text='-',bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b8.place(x=227,y=170)
b9=Label(root,text=7,bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b9.place(x=2,y=220)
b10=Label(root,text=8,bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b10.place(x=77,y=220)
b11=Label(root,text=9,bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b11.place(x=152,y=220)
b12=Label(root,text='+',bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b12.place(x=227,y=220)
b13=Label(root,text='.',bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b13.place(x=2,y=270)
b14=Label(root,text=0,bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b14.place(x=77,y=270)
b15=Label(root,text='x',bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b15.place(x=152,y=270)
b16=Label(root,text='=',bg=color_var,fg=nomber_color,bd=0,width=5,pady=35,font=('tajwal',17,'bold'))
b16.place(x=227,y=270)
b17=Label(root,text='C',bg=color_var,fg=nomber_color,bd=0,width=5,pady=10,font=('tajwal',17,'bold'))
b17.place(x=2,y=320)
b18=Label(root,text='〤',bg=color_var,fg=nomber_color,bd=0,width=10,padx=3,pady=10,font=('tajwal',17,'bold'))
b18.place(x=77,y=320)

b1.bind('<ButtonRelease-1>',lambda e: Cal(1,b1))
b2.bind('<ButtonRelease-1>',lambda e: Cal(2,b2))
b3.bind('<ButtonRelease-1>',lambda e: Cal(3,b3))
b4.bind('<ButtonRelease-1>',lambda e: Cal('/',b4))
b5.bind('<ButtonRelease-1>',lambda e: Cal(4,b5))
b6.bind('<ButtonRelease-1>',lambda e: Cal(5,b6))
b7.bind('<ButtonRelease-1>',lambda e: Cal(6,b7))
b8.bind('<ButtonRelease-1>',lambda e: Cal('-',b8))
b9.bind('<ButtonRelease-1>',lambda e: Cal(7,b9))
b10.bind('<ButtonRelease-1>',lambda e: Cal(8,b10))
b11.bind('<ButtonRelease-1>',lambda e: Cal(9,b11))
b12.bind('<ButtonRelease-1>',lambda e: Cal('+',b12))
b13.bind('<ButtonRelease-1>',lambda e: Cal('.',b13))
b14.bind('<ButtonRelease-1>',lambda e: Cal(0,b14))
b15.bind('<ButtonRelease-1>',lambda e: Cal('x',b15))
b16.bind('<ButtonRelease-1>',lambda e: E_Qual1())
b17.bind('<ButtonRelease-1>',lambda e: Clear())
b18.bind('<ButtonRelease-1>',lambda e: Delete())

def change_1color(event):
    b.config(bd=1)
def reste_1color(event):
    b.config(bd=0)
b.bind('<Enter>', change_1color)
b.bind('<Leave>',reste_1color)

def change_color(label,x,y,padx,pady):
    def w1():
        label.config(highlightbackground=cadr,padx=padx+1,pady=pady+1)
        label.place(x=x-2,y=y-2)
    root.after(50,w1)
    label.config(highlightbackground=cadr1,highlightthickness=1,bg=color_var1)
def reste_color(label,x,y,padx,pady):
    def r1():
        label.config(highlightthickness=0,bg=color_var,padx=padx,pady=pady)
        label.place(x=x,y=y)
    root.after(50,r1)
b1.bind('<Enter>',lambda e:change_color(b1,2,120,1,10))
b1.bind('<Leave>',lambda e:reste_color(b1,2,120,1,10))
b2.bind('<Enter>',lambda e:change_color(b2,77,120,1,10))
b2.bind('<Leave>',lambda e:reste_color(b2,77,120,1,10))
b3.bind('<Enter>',lambda e:change_color(b3,152,120,1,10))
b3.bind('<Leave>',lambda e:reste_color(b3,152,120,1,10))
b4.bind('<Enter>',lambda e:change_color(b4,227,120,1,10))
b4.bind('<Leave>',lambda e:reste_color(b4,227,120,1,10))
b5.bind('<Enter>',lambda e:change_color(b5,2,170,1,10))
b5.bind('<Leave>',lambda e:reste_color(b5,2,170,1,10))
b6.bind('<Enter>',lambda e:change_color(b6,77,170,1,10))
b6.bind('<Leave>',lambda e:reste_color(b6,77,170,1,10))
b7.bind('<Enter>',lambda e:change_color(b7,152,170,1,10))
b7.bind('<Leave>',lambda e:reste_color(b7,152,170,1,10))
b8.bind('<Enter>',lambda e:change_color(b8,227,170,1,10))
b8.bind('<Leave>',lambda e:reste_color(b8,227,170,1,10))
b9.bind('<Enter>',lambda e:change_color(b9,2,220,1,10))
b9.bind('<Leave>',lambda e:reste_color(b9,2,220,1,10))
b10.bind('<Enter>',lambda e:change_color(b10,77,220,1,10))
b10.bind('<Leave>',lambda e:reste_color(b10,77,220,1,10))
b11.bind('<Enter>',lambda e:change_color(b11,152,220,1,10))
b11.bind('<Leave>',lambda e:reste_color(b11,152,220,1,10))
b12.bind('<Enter>',lambda e:change_color(b12,227,220,1,10))
b12.bind('<Leave>',lambda e:reste_color(b12,227,220,1,10))
b13.bind('<Enter>',lambda e:change_color(b13,2,270,1,10))
b13.bind('<Leave>',lambda e:reste_color(b13,2,270,1,10))
b14.bind('<Enter>',lambda e:change_color(b14,77,270,1,10))
b14.bind('<Leave>',lambda e:reste_color(b14,77,270,1,10))
b15.bind('<Enter>',lambda e:change_color(b15,152,270,1,10))
b15.bind('<Leave>',lambda e:reste_color(b15,152,270,1,10))
b16.bind('<Enter>',lambda e:change_color(b16,227,270,1,35))
b16.bind('<Leave>',lambda e:reste_color(b16,227,270,1,35))
b17.bind('<Enter>',lambda e:change_color(b17,2,320,1,10))
b17.bind('<Leave>',lambda e:reste_color(b17,2,320,1,10))
b18.bind('<Enter>',lambda e:change_color(b18,77,320,3,10))
b18.bind('<Leave>',lambda e:reste_color(b18,77,320,3,10))

root.mainloop()