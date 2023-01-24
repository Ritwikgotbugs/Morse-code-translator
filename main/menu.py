import tkinter as tk
from subprocess import call 
import customtkinter as ctk

#Call functions
def text_2_morse():
    call(["python", "C:/Users/Ritwik/Desktop/All/Projects/Morse-code-translator/main/text_morse.py"])
def morse_2_text():
    call(["python","C:/Users/Ritwik/Desktop/All/Projects/Morse-code-translator/main/morse_text.py"])
def speech_2_morse():
    call(["python","C:/Users/Ritwik/Desktop/All/Projects/Morse-code-translator/main/speech_morse.py"])

#Main TK window
menu= ctk.CTk()
menu.title("Morse Translator")
menu.geometry("400x350")
menu.config(bg='#0e2038')

#Message Box
def on_closing(menu):
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        menu.destroy()
menu.protocol("WM_DELETE_WINDOW", lambda: on_closing(menu))

#Using Custom Tkinter for dark theme
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


x_cordinate = 415
y_cordinate = 80
menu.geometry("+%d+%d" % (x_cordinate, y_cordinate))

#Icon for window
menu.iconphoto(False, tk.PhotoImage(file="morse icon.png"))

#Sentence label
label = tk.Label(menu, text="Choose any one of the given modes",fg='#fff')
label.config(padx=10, pady= 15, font=('Times new roman', 13,'bold'),bg='#0e2038')
label.pack()

#All menu buttons
button1 = tk.Button(menu, text='Morse Code to Text', width=25,height=3, command=morse_2_text,font=('Arial',10,'bold'), background="#0271c6",fg='#fff')
button2 = tk.Button(menu, text='Speech to Morse Code', width=25,height=3 ,font=('Arial',10,'bold'),command=speech_2_morse,background="#0271c6",fg='#fff')
button3 = tk.Button(menu, text='Text to Morse', width=25,height=3,font=('Arial',10,'bold'), command=text_2_morse, background="#0271c6",fg='#fff')
button4 = tk.Button(menu, text='Exit', width=25,height=3,font=('Arial',10,'bold'), command=menu.destroy, background="#0271c6",fg='#fff')

button1.pack(padx=1,pady=5)
button2.pack(padx=1,pady=5)
button3.pack(padx=1,pady=5)
button4.pack(padx=1,pady=5)

menu.mainloop()