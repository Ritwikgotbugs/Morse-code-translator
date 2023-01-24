import tkinter as tk
import textwrap
import playsound
import time
import customtkinter as ctk
import os

#Function for translating the given text to Morse
def translate():
# Morse code dictionary
    Morse_dict = { 'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ',':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-',' ':' '} 
    try:
        morse_text = ""
        crypt=input_field.get()
        crypt = crypt.upper()
        for letter in crypt:
            morse_text += Morse_dict[letter] + ' '
        return morse_text


    except:
        return 'Error in Morse Code'
    
#Function for displaying the result
def on_submit():
    input_text = input_field.get()
    morse_text = translate()
    text_widget.insert('1.0', (morse_text))
   
#Audio player
def audio():
    morse_text=translate()
    for code in morse_text:
        if code == '.':
            playsound.playsound("dot_file.wav")
        elif code == '-':
            playsound.playsound("dash_file.wav")
        elif code== ' ':
            time.sleep(0.5)


#TK window
text_2_morse = ctk.CTk()
text_2_morse.title("Text to Morse")
text_2_morse.resizable(False,False)


#Custom Tkinter for Dark Theme
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


#Geometry & Config
text_2_morse.geometry('450x500')
text_2_morse.config(bg='#0e2038')
text_2_morse.iconphoto(False, tk.PhotoImage(file="morse icon.png"))


#coordinates to place the window in the center
x_cordinate = 415
y_cordinate = 80
text_2_morse.geometry("+%d+%d" % (x_cordinate, y_cordinate))


#Text label
label=tk.Label(text_2_morse,text='Enter a Sentence:', font=('Arial',15),fg='#fff')
label.config(bg='#0e2038')
label.pack(pady=10)


#Input field for text
input_field = tk.Entry(text_2_morse,font=('Arial',20))
input_field.pack()

# Create a button
insert_button = tk.Button(text_2_morse, text="Translate", command=lambda: text_widget.delete('1.0', tk.END) or text_widget.insert('1.0', on_submit()),font=('Arial',15))
insert_button.pack(pady=10)

#Text2 label
label_2=tk.Label(text_2_morse,text='Morse Code:',font=('Arial',15),fg='#fff')
label_2.config(bg='#0e2038')
label_2.pack()

#Morse Code Text
text_widget = tk.Text(text_2_morse,width=30, height=10,font=('Arial',15))
text_widget.pack(pady=1)

#Audio button
Audio_button=tk.Button(text_2_morse,text='Listen Morse Code',command=audio,font=('Arial',15))
Audio_button.pack(pady=10)


text_2_morse.mainloop()