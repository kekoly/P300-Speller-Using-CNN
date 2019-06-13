from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from os import path
import numpy as np
import GUI_Handler as feeder
def predictions(Model,File_Name):
    if Model == 1:
        cnn_model = 'Subject_A_CNN.h5'
    elif Model == 2:
        cnn_model = 'Subject_B_CNN.h5'
    elif Model == 3:
        cnn_model = 'Subject_AB_CNN.h5'

    return feeder.feedMe(cnn_model, File_Name)

 

window = Tk()
window.title('P300 Classification App')
window.geometry('725x300')
window.file_path = ' '
data_path = 'C:/Users/Greg/OneDrive - Salem State University/2018 Fall CSC521/P300 Speller Using CNN/P300 Speller Using CNN/Test Data/'
# add empty label in row 0 and column 0
l0 = Label(window, text='     ')
l0.grid(column=0, row=0)

lbl = Label(window, 
            text = 'Welcome to P300 Speller Using Convolutional Neural Networks',
            font = ('Arial Bold', 14),                       
            )
lbl.grid(column = 1, row = 1, sticky=E, columnspan=3)

# add empty label in row 0 and column 0
l0 = Label(window, text='     ')
l0.grid(column=1, row=2)

lbl1 = Label(window, 
            text = 'Choose Model: ',
            font = ('Arial Bold', 12),
            justify = 'center')
lbl1.grid(column = 1, row = 3,sticky = W )

selected = IntVar()

rad1 = Radiobutton(window,text='Subject A CNN', value=1, variable = selected)
 
rad2 = Radiobutton(window,text='Subject B CNN', value=2, variable = selected)
 
rad3 = Radiobutton(window,text='Both A + B CNN', value=3, variable = selected)


rad1.grid(column=1, row=4, sticky=W)
 
rad2.grid(column=1, row=5, sticky=W)
 
rad3.grid(column=1, row=6, sticky=W)

# add empty label in row 1 and column 7
l0 = Label(window, text='     ')
l0.grid(column=1, row=7)

def clicked():
    window.file_path = askopenfilename(initialdir = path.dirname(data_path),
                               filetypes = (("Numpy","*.npy"),("all files","*.*")),
                               title = 'Select character to load') # show an "Open" dialog box and return the path to the selected file

btn = Button(window, text='Load Data', command=clicked)
btn.grid(column = 1, row = 8, sticky=W)

lbl2 = Label(window, 
            text = 'Model Predictions: ',
            font = ('Arial Bold', 12))
            
lbl2.grid(column = 3, row = 3,sticky = W )


def predict():

    model = selected.get()
    
    lc = Label(window, text='  ')
    lc.grid(column=3, row=4, sticky = W+E, columnspan=2)

    lc1 = Label(window, text=' ')
    lc1.grid(column=3, row=5, sticky = W+E, columnspan=2)
    
    lc2 = Label(window, text=' ')
    lc2.grid(column=3, row=6, sticky = W+E, columnspan=2)

    lc3 = Label(window, text=' ')
    lc3.grid(column=3, row=7, sticky = W+E, columnspan=2)
  
    
    if model == 0:
        lble1 = Label(window, 
                    text = 'Please Choose Model!',
                    font = ('Arial ', 11))
        lble1.grid(column = 3, row = 5,sticky = W)
    elif window.file_path == ' ':
        lble2 = Label(window, 
                    text = 'Please Load a File!',
                    font = ('Arial ', 11))
        lble2.grid(column = 3, row = 5,sticky = W)
    else:
        
        p, w, i = feeder.feedMe(model,window.file_path)
        lbl5 = Label(window, 
                    text = 'You Loaded Character #: ' + str(i),
                    font = ('Arial ', 11))
        lbl5.grid(column = 3, row = 4,sticky = W)

        lbl3 = Label(window, 
                    text = 'Predicted: ' + p,
                    font = ('Arial ', 11))
            
        lbl3.grid(column = 3, row = 5,sticky = W)

        lbl4 = Label(window, 
                    text = 'Was: '+ w,
                    font = ('Arial ', 11))
            
        lbl4.grid(column = 3, row = 6,sticky = W )


btn = Button(window, text='Predict', command=predict)
btn.grid(column = 3, row = 8, sticky=W)


window.mainloop()

   