
#Import the required Libraries
import PyPDF2
from gtts import gTTS
from tkinter import *
from tkinter import filedialog
import os
#Create an instance of tkinter frame
win= Tk()
#Set the Geometry
win.geometry("1920x1020")
#Create a Text Box
text= Text(win,width= 110,height=30)
text.pack(pady=20)
def quit_app():
   win.destroy()
def open_pdf():
   file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
   if file:
      #Open the PDF File
      pdf_file= PyPDF2.PdfReader(file)
      #Select a Page to read
      print(type(k))
      try:
          page= pdf_file.pages[int(k)]
      except Exception:
          label1=Label(win, text="Page Number Doesnt Exist", font=("Courier 22 bold"))
          label1.pack() 
          
          
      #Get the content of the Page
      global content
      try:
          content=page.extract_text()
          button.config(state='active')
      #Add the content to TextBox
          text.insert(1.0,content)
      except Exception:
          label1=Label(win, text="Page Number Doesnt Exist", font=("Courier 22 bold"))
          
    
def display_text():
   global entry
   
   string= entry.get()
   label.configure(text=string)
   global k
   k=string
   print(k)
   button2.config(state='active')
   
label=Label(win, text="Reading Page", font=("Courier 22 bold"))
label.pack()

def speak():
    tts = gTTS(content,lang='en',tld='co.uk')
    tts.save('hello11.mp3')
    print("Done")
    k=os.getcwd()+'\hello11.mp3'
    os.startfile(k)
    


    
def clear_text():
   text.delete(1.0, END)
   del k
   
   del pdf_file
   os.remove(hello11.mp3)
   
   
#button codes for text_to_speech
   
button=Button(win,text='Convert to Voice',height= 1, width=20,command=speak)#done
button.config(state='disabled')
button2=Button(win,text='Open a PDF File',height= 1, width=20,command=open_pdf)#done
button2.config(state='disabled')
entry= Entry(win, width= 20)
entry.focus_set()

button3=Button(win,text=' Page Number to read ',height= 1, width=20,command=display_text)#done
button4=Button(win,text='clear text',height= 1, width=20,command=clear_text)
button5=Button(win,text='QUIT',height= 1, width=20,command=quit_app)#done
entry.pack(pady=10)
button3.pack(pady=0)
button2.pack()



button.pack()
button4.pack()
button5.pack()





#Create a Menu
my_menu= Menu(win)
win.config(menu=my_menu)
#Add dropdown to the Menus
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu= file_menu)
file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_command(label="Clear",command=clear_text)
file_menu.add_command(label="Quit",command=quit_app)
win.mainloop()
