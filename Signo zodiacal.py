from tkinter import *
from tkinter import messagebox

win=Tk()
win.title('Signo Zodiacal')
win.geometry('350x300')
win.config(background='Indigo')

def signo():

    dia = int(entry_day.get())
    mes = int(entry_mes.get())
    
    if (21 <= dia <= 31 and mes==3) or (1 <= dia <= 20 and mes==4 ):
        mensaje =  "Tu signo zodiacal es Aries."  
    elif (21 <= dia <= 30 and mes==4) or (1 <= dia <= 20 and mes==5 ):
        mensaje = "Tu signo zodiacal es Tauro."
    elif (21 <= dia <= 31 and mes==5) or (1 <= dia <= 21 and mes==6 ):
        mensaje = "Tu signo zodiacal es Géminis."
    elif(22 <= dia <= 30 and mes==6) or (1 <= dia <= 22 and mes==7 ):
        mensaje = "Tu signo zodiacal es Cáncer."
    elif (23 <= dia <= 31 and mes==7) or (1 <= dia <= 23 and mes==8 ):
        mensaje = "Tu signo zodiacal es Leo."
    elif (24 <= dia <= 31 and mes==8) or (1 <= dia <= 22 and mes==9 ):
        mensaje = "Tu signo zodiacal es Virgo."
    elif (23 <= dia <= 30 and mes==9) or (1 <= dia <= 22 and mes==10 ):
        mensaje = "Tu signo zodiacal es Libra."
    elif (23 <= dia <= 31 and mes==10) or (1 <= dia <= 22 and mes==11 ):
        mensaje = "Tu signo zodiacal es Escorpio."
    elif (23 <= dia <= 30 and mes==11) or (1 <= dia <= 21 and mes==12 ):
        mensaje = "Tu signo zodiacal es Sagitario."
    elif (22 <= dia <= 31 and mes==12) or (1 <= dia <= 20 and mes==1):
        mensaje = "Tu signo zodiacal es Capricornio."
    elif (21 <= dia <= 31 and mes==1) or (1 <= dia <= 19 and mes==2 ):
        mensaje = "Tu signo zodiacal es Acuario."
    elif (20 <= dia <= 29 and mes==2) or (1 <= dia <= 20 and mes==3 ):
        mensaje = "Tu signo zodiacal es Piscis."
    else:
        mensaje = 'Lo sentimos, \n los datos introducidos \n no son correctos'
        
    e4.config(text=mensaje)
    
    
    

bienvenida = ''' Saludos. Para conocer tu signo zodiacal, \n coloca en cifras el día y mes de tu nacimiento \n y dale al botón. '''
Label(win, text=bienvenida, font=('Aharoni', 12), bg='Indigo', fg='Aqua').pack(pady=10)
Label(win, text='Día', font=('Aharoni', 10), bg='Indigo', fg='Aqua').place(x=125, y=90)
Label(win, text='Mes', font=('Aharoni', 10), bg='Indigo', fg='Aqua').place(x=125, y=120)
e4 = Label(win, font=('Aharoni', 12), bg='Indigo', fg='Aqua')
e4.place(x=80, y=200)

entry_day = Entry(win, width=7)
entry_day.place(x=165, y=90)
entry_mes = Entry(win, width=7)
entry_mes.place(x=165, y=120)

btn = Button(win, text='Mi signo', command=signo,  font=('Aharoni', 12), bg='Indigo', fg='Aqua', activebackground='Purple', cursor='hand2')
btn.place(x=135, y=160)

win.mainloop()
