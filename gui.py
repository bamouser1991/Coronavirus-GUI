import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
import Corona
import csv


 
def response(countries):
    if countries.lower() == 'world':
        return Corona.df.head(10)
    if countries.lower() == 'china':
        return Corona.df.head(1) 
    if countries.lower() == 'italy':
        return Corona.df.iloc[1:2]
    if countries.lower() == 'iran':
        return Corona.df.iloc[2:3]
    if countries.lower() == 'south korea':
        return Corona.df.iloc[3:4]
    if countries.lower() == 'spain':
        return Corona.df.iloc[4:5]
    if countries.lower() == 'germany':
        return Corona.df.iloc[5:6]
    if countries.lower() == 'france':
        return Corona.df.iloc[6:7]
    if countries.lower() == 'usa':
        return Corona.df.iloc[7:8]
    if countries.lower() == 'switzerland':
        return Corona.df.iloc[8:9]
    if countries.lower() == 'uk':
        return Corona.df.iloc[9:10]
    else:
        return 'Data is not available'

def submit(countries):
    data['text'] = response(countries)
    
root = tk.Tk()

#Backgroung Settings
canvas = tk.Canvas(root, height=600, width=700)
canvas.pack()

background_image = ImageTk.PhotoImage(file='virus.jpg')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1,)

#Title Settings
frame = tk.Frame(root)
frame.place(relx=0.1, rely=0.05, relwidth=.8,relheight=.05)

label = tk.Label(frame, font=('Impact',13), text='Live: Coronavirus Data', bg='red')
label.pack(side='top', fill='both', expand = 'true')

#Text Frame
text_frame = tk.Frame(root)
text_frame.place(relx=.35,rely=.85,relwidth=.3,relheight=.05)

entry = tk.Entry(text_frame, bg = '#d1cef0', font=('Freesans',12), bd=2)
entry.pack(fill='both', expand = 'true')
#Button Frame
button_frame = tk.Frame(root)
button_frame.place(relx=.425,rely=.92,relwidth=.15,relheight=.05)

button = tk.Button(button_frame, font= '18',text ='Gather Data', fg='white', bg='#0d3573', command=lambda: submit(entry.get()))
button.pack(fill='both',expand='true')

#Retured Data
data_frame = tk.Frame(root)
data_frame.place(relx=.2,rely=.3,relwidth=.6,relheight=.4)

data = tk.Label(data_frame,bg = '#d1cef0',font=('Freesans',13),text = Corona.live_data1.text +'\n'+ Corona.live_data2.text +'\n'+ Corona.live_data3.text)
data.pack(fill='both' ,expand = 'true')


root.mainloop()