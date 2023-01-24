import tkinter as tk
import speech_recognition as sr 
import textwrap
import customtkinter as ctk

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
                '(':'-.--.', ')':'-.--.-', ' ':' '} 

#Function for speech recognition
def speech2morse():

    import speech_recognition as sr
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio_text = r.listen(source)
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            main_text=text
            return main_text
            

        except:
            return None
    r.stop_listening()

#Converting to morse
def morse_conversion():
    main_text=speech2morse()
    try:
        morse_text = ""
        main_text = main_text.upper()
        for letter in main_text:
            morse_text += Morse_dict[letter] + ' '
        return morse_text 

    except:
        return 'Error in Morse Code'

#Function for displaying the result
def click():
    #result1
    string=morse_conversion()
    text_widget.insert('1.0', (string))
 
#Tkinter
speech_morse=ctk.CTk()
speech_morse.title("Speech to Morse Code")
speech_morse.resizable(False,False) 

#Custom Tkinter for Dark theme
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

#Geometry and Config
speech_morse.geometry("600x350")
speech_morse.config(bg='#0e2038')
x_cordinate = 415
y_cordinate = 80
speech_morse.geometry("+%d+%d" % (x_cordinate, y_cordinate))

#Window Icon
speech_morse.iconphoto(False, tk.PhotoImage(file="morse icon.png"))

#Display Label
Display1=tk.Label(text='Click the Button to start the voice recognition', font=('Arial',16),fg='#fff')
Display1.config(bg='#0e2038')
Display1.pack()

#Audio Button
speak_button = tk.Button(speech_morse, text="Speak", command=lambda: text_widget.delete('1.0', tk.END) or text_widget.insert('1.0', click()),font=('Arial',15))
speak_button.pack(pady=10)

#Text label
result=tk.Label(speech_morse,text='Recognized:',bg='#0e2038',fg='#fff')
result.config(font=('Arial',15))    
result.pack()

#Morse Code Text
text_widget = tk.Text(speech_morse,width=30, height=5,font=('Arial',15))
text_widget.pack(pady=1)

speech_morse.mainloop()