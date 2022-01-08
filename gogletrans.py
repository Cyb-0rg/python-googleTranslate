from tkinter import *
from tkinter import ttk, messagebox

import googletrans
from googletrans import Translator
import textblob

import pyttsx3
import speech_recognition as sr

def sp_recognizer():
    
    with sr.Microphone() as source:
        try:
            audio = rec.listen(source, timeout=5, phrase_time_limit=5)
            print(rec.recognize_google(audio))
            
        except(sr.UnknownValueError):
            print("gibberishit")
        except(sr.WaitTimeoutError):
            print("nothing")
        except(sr.RequestError):
            print("offline")
        


root=Tk()
root.title("Google translate")
root.geometry("1080x480")


def label_change():
    c1=combo1.get()
    c2=combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000, label_change)


def translator():
    global language
    try:
        text_=text1.get(1.0, END)
        
        c3=combo1.get()
        c4=combo2.get()
        if (text_):
            words=textblob.TextBlob(text_) 
            lan=words.detect_language()
            for i,j in language.items():
                if (j==c4):
                    lan_=i
            words=words.translate(from_lang=lan, to =str(lan_))
            text2.delete(1.0,END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror("google translate", "please try again")

def flip():
    
    text_1= text1.get(1.0, END)
    text_2=text2.get(1.0, END)

    text2.delete(1.0,END)
    text2.insert(END, text_1)

    text1.delete(1.0,END)
    text1.insert(END, text_2)

    c3=combo1.get()
    c4=combo2.get()

    combo1.set(c4)
    combo2.set(c3)
    


    
def reader1():
    text_to_read=text1.get(1.0, END)
    engine= pyttsx3.init()
    #change_voice(engine, "nl_BE", "VoiceGenderFemale")
    engine.say(text_to_read)
    engine.runAndWait()

def reader2():
    text_to_read=text2.get(1.0, END)
    engine= pyttsx3.init()
    engine.say(text_to_read)
    engine.runAndWait()


def saver():
    
    global root2
    root2=Tk()
    root2.title("save document")
    root2.geometry("300x120")

    label0= Label(root2,text="file name:")
    label0.place(relx =0.14, rely = 0.2, anchor= CENTER)
    
    global fileName
    fileName = Entry(root2, width =20)
    fileName.place(relx =0.5, rely = 0.2, anchor= CENTER)
    
    done = Button (root2, text="save", bd=1, command= saver2)
    done.place(relx =0.5, rely = 0.5, anchor= CENTER)
    
    label01= Label(root2,text=".txt")
    label01.place(relx =0.70, rely = 0.2, anchor= CENTER)
    
    root2.mainloop()
   
def saver2b():
    global root2
    root2=Tk()
    root2.title("save document")
    root2.geometry("300x120")

    label0= Label(root2,text="file name:")
    label0.place(relx =0.14, rely = 0.2, anchor= CENTER)
    
    global fileName
    fileName = Entry(root2, width =20)
    fileName.place(relx =0.5, rely = 0.2, anchor= CENTER)

    label01= Label(root2,text=".txt")
    label01.place(relx =0.7, rely = 0.2, anchor= CENTER)
    
    done = Button (root2, text="save", bd=1, command= saver2b2)
    done.place(relx =0.5, rely = 0.5, anchor= CENTER)
    
    
    root2.mainloop()    

def saver2b2 ():
    fileName2= "saved\\"
    fileName2+=fileName.get()
    fileName2+=".txt"


    kayit = open(fileName2, "w+")
    kayit.write(text2.get(1.0, END))
    
    kayit.close()
    root2.destroy()
    #print(fileName2)
    
def saver2 ():


    if ( True ):
        fileName2= "saved\\"
        fileName2+=fileName.get()
        fileName2+=".txt"


        kayit = open(fileName2, "w+")
        kayit.write(text1.get(1.0, END))
        
        kayit.close()
        root2.destroy()
        #print(fileName2)
    
image_icon= PhotoImage(file="images/google.png")
root.iconphoto(False,image_icon)



language=googletrans.LANGUAGES
languageV=list(language.values())
lang1= language.keys()




combo1=ttk.Combobox(root, values=languageV, font="Roboto 14", state= "r")
combo1.place(x=110, y=50)
combo1.set("Select Language")

label1= Label(root,text="ENGLISH", font="Roboto 10", bg="white", fg="blue",width=12, bd=2, relief=GROOVE )
label1.place(x=10,y=96)

########the text area1##########
frame1=Frame(root, bg="blue",bd=2)
frame1.place(x=10, y=118, width= 440, height= 210)

text1= Text(frame1, font="Britannic 12", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width= 440-4, height= 210-4)


scrollbar1= Scrollbar(frame1)
scrollbar1.pack(side="right",  fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

##########################

combo2=ttk.Combobox(root, values=languageV, font="Roboto 14", state= "r")
combo2.place(x=730, y=50)
combo2.set("Select Language")

label2= Label(root,text="ENGLISH", font="Roboto 10", bg="white",fg="green", width=12, bd=2, relief=GROOVE )
label2.place(x=620,y=96)

########the text area2##########
frame2=Frame(root, bg="green",bd=2)
frame2.place(x=620, y=118, width= 440, height= 210)

text2= Text(frame2, font="Britannic 12", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width= 440-4, height= 210-4)

scrollbar2= Scrollbar(frame2)
scrollbar2.pack(side="right",  fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

soundIcon = PhotoImage(file= "images/sound.png")
flipIcon = PhotoImage(file= "images/synchronize-24.png")
saveIcon = PhotoImage(file= "images/save3.png")

##########################

translate= Button(root, text="Translate", font="Roboto 12 bold", activebackground="#6ee684", bg="#51a9db", fg="white", cursor="hand2",bd=2.5 , command=translator)
translate.place(x= 485, y=270 )

flip= Button(root,  image=flipIcon ,  activebackground="#ffd6d6", cursor="hand2",bd=0.5 , command=flip)
flip.place(x=520, y=130)

read= Button(root, image=soundIcon,  activebackground="#51a9db", cursor="hand2",bd=0.8 , command=reader1)
read.place(x= 14, y=330 )

read2= Button(root, image=soundIcon ,activebackground="#6ee684", cursor="hand2",bd=0.8 , command=reader2)
read2.place(x= 624, y=330 )

save= Button(root, image=saveIcon ,activebackground="#51a9db", cursor="hand2",bd=0, command=saver)
save.place(x= 56, y=330 )

save2= Button(root, image=saveIcon ,activebackground="#6ee684", cursor="hand2",bd=0, command=saver2b) #saver2b #sp_recognizer
save2.place(x= 668, y=330 )

##########################
label_change()
root.configure(bg="#e1e3e2")
root.mainloop()




