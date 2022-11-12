'''
IMPORTING ESSENTIAL MODULES 

PYGAME : FOR ALERT SOUND 
CV2 : FOR FACE RECOGNITION
TKINTER : FOR UI DESIGN 

'''
import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Driver Cam')
frame.config(background='light blue')
label = Label(frame, text="Driver Cam",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="C:\Projects\Drowsy Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\driver-icon-clipart-1.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)


''' FUNCTION DEFINITIONS FOR WHEN CERTAIN BUTTONS ARE CLICKED 
HELP GIVES OPEN CV DOCUMENTATION WHEN WE CLICK A BUTTON
CONTRI TELL ABOUT THE CONTRIBUTORS OF THE PROJECT THROUGH A MESSAGE BOX
ANOTHER WIN IS ABOUT SECTION THAT SAYS WHAT THIS PROJECT IS ABOUT
'''
def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributors","Vaibhav , Tanvi , Disha , Shardul\n")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Driver Cam version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
                                    
   
#DROP DOWN MENU DESIGN 
menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Driver Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)

'''' following is the list of functions that also perform task when a button is clicked on the ui '''

def exitt():
   exit()

''''---------------------------------------------------------------------------'''
def web():
   capture =cv2.VideoCapture(0) #start webcam
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#converting color to grayscale 
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'): #as soon as 'q' is pressed the webcam stops recording and control return to the Original GUI 
         break
   capture.release()
   cv2.destroyAllWindows()
'''-------------------------------------------------------------------------'''
def webrec():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') #writing video feature 
   op=cv2.VideoWriter('Sample1.avi',fourcc,11.0,(640,480)) #records , and saves with name sample in 640x480 p in the folder location 
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      op.write(frame) 
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   
'''-----------------------------------------------------------------'''
def webdet():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('C:\Projects\Drowsy Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\lbpcascade_frontalface.xml') #cascade classifier is used to detect and eyes (inbuilt in opencv2)
   eye_glass = cv2.CascadeClassifier('C:\Projects\Drowsy Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\haarcascade_eye_tree_eyeglasses.xml')
   

   while True:  #infinite loop in order to capture video and detect face 
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray) #FACES variable stores instances of faces for recognition 
    
      # for loops to mark face area and  eye area with boxes and marking showing what is face and eye 
       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          
           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

       
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   capture.release()
   cv2.destroyAllWindows()

'''---------------------------------this fuinction does same as above but also has a provision to save the video file -----------------------------------------------'''
def webdetRec():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('C:\Projects\Drowsy Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('C:\Projects\Drowsy Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.avi',fourcc,9.0,(640,480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          

           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       op.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   op.release()      
   capture.release()
   cv2.destroyAllWindows()

'''---------------------------this function is used to give sound after interval of 0.1 sec------------------------------------------------'''
def alert():
   mixer.init()
   alert=mixer.Sound('C:\Projects\Drowsy Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\sound.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()   

'''---------------------------blink is detected in same way as face and eye , but using blinkcascade xml file ----------------------------------------------'''
   
def blink():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('C:\Projects\Drowsy Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('C:\Projects\Drowsy Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\haarcascade_eye.xml')
   blink_cascade = cv2.CascadeClassifier('C:\Projects\Drowsy Driver\Drowsiness-monitoring-Using-OpenCV-Python-master\CustomBlinkCascade.xml')

   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         font = cv2.FONT_HERSHEY_COMPLEX
         cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

         blink = blink_cascade.detectMultiScale(roi_gray)
         for(eyx,eyy,eyw,eyh) in blink:
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            alert()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
         
  
   capture.release()
   cv2.destroyAllWindows()
'''------------------------these here are buttons gui desgin and where they are placed on the UI ------------------------------------------------------------'''

   
but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=web,text='Open Cam',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webrec,text='Open Cam & Record',font=('helvetica 15 bold'))
but2.place(x=5,y=176)

but3=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdet,text='Open Cam & Detect',font=('helvetica 15 bold'))
but3.place(x=5,y=250)

but4=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdetRec,text='Detect & Record',font=('helvetica 15 bold'))
but4.place(x=5,y=322)

but5=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=blink,text='Detect Eye Blink & Record With Sound',font=('helvetica 15 bold'))
but5.place(x=5,y=400)

but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but5.place(x=210,y=478)


root.mainloop()

