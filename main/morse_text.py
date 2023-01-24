import tkinter as tk
import textwrap
from gtts import gTTS
import os
import customtkinter as ctk


#Function to convert input morse code to text
def morse2text():
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
                '(':'-.--.', ')':'-.--.-',' ':' ','  ':'  '} 
    d_swap = {v: k for k, v in Morse_dict.items()}
    
    try:
        input=input_text.get()
        split_string = input.split()
        new_list = []
        for i in split_string:
            new_list.append(i)
            morse_text=''
            i=0
            while i<len(new_list):
                for letter in new_list:
                    morse_text += d_swap[letter] + ' '
                    i+=1
        txt= morse_text.replace(' ','').lower()
        
        return txt
    except:
        return 'Error in Morse Code'

#Function for displaying the result
def enter():
    morse=morse2text()
    text_widget.insert('1.0', (morse))


def on_submit():
    morse=morse2text()
    read_string(morse)

#Audio reader
def read_string(string):
    tts = gTTS(string)
    tts.save("output.mp3")
    os.system("start output.mp3")

#TK window
morse_text=ctk.CTk()
morse_text.title('Morse to Text')
morse_text.resizable(False,False)

#Custom Tkinter for Dark theme
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


#Geometry & Configuration
morse_text.geometry('450x500')
morse_text.config(bg='#0e2038')
morse_text.iconphoto(False, tk.PhotoImage(file="morse icon.png"))

#Coordinates to place the window in the center
x_cordinate = 415
y_cordinate = 80
morse_text.geometry("+%d+%d" % (x_cordinate, y_cordinate))

#Text label
text_label=tk.Label(text='Enter Morse Code:',font=('Arial',15),fg='#fff')
text_label.config(bg='#0e2038')
text_label.pack(pady=5)

#Input field
input_text=tk.Entry(morse_text)
input_text.config(width=20,font=('Arial',20),fg='#000000')
input_text.pack(pady=5)

#Note label
text_label=tk.Label(text='Note: This translator does not take more than one word at a time.',font=('Arial',11),fg='#fff')
text_label.config(bg='#0e2038')
text_label.pack()

# Create a button
insert_button = tk.Button(morse_text, text="Enter", command=lambda: text_widget.delete('1.0', tk.END) or text_widget.insert('1.0', enter()),font=('Arial',15))
insert_button.pack(pady=10)

#Morse Code Text
text_widget = tk.Text(morse_text,width=30, height=10,font=('Arial',15))
text_widget.pack(pady=1)

submit = tk.Button(morse_text,text='Audio', font=('Arial', 15),command=on_submit)
submit.pack(pady=10)

morse_text.mainloop()