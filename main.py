from tkinter import *
from PIL import ImageTk, Image
from editFunctions import sharpenPic, blurPic, rotateCounter, rotateClock, cropPic, sketchPic, oilPic, pencilPic, foilPic, negativePic



def changeImage(counter):
    img = ImageTk.PhotoImage(Image.open('image' + str(counter) + '.jpg'))
    panel.configure(image=img)
    panel.image = img

def sharpenImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    sharpenPic(curImg, counter)
    changeImage(counter)

def blurImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    blurPic(curImg, counter)
    changeImage(counter)

def rotateCounterFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    rotateCounter(curImg, counter)
    changeImage(counter)

def rotateClockFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    rotateClock(curImg, counter)
    changeImage(counter)

def cropImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    cropPic(curImg, counter)
    changeImage(counter)

def undoFunc():
    global counter
    if counter > 0:
        counter = counter - 1
    changeImage(counter)

def sketchImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    sketchPic(curImg, counter)
    changeImage(counter)

def oilImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    oilPic(curImg, counter)
    changeImage(counter)

def pencilImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    pencilPic(curImg, counter)
    changeImage(counter)

def foilImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    foilPic(curImg, counter)
    changeImage(counter)

def negativeImgFunc():
    global counter
    curImg = 'image' + str(counter) + '.jpg'
    counter = counter + 1
    negativePic(curImg, counter)
    changeImage(counter)

main = Tk()
counter = 0
main.title("Edit Mr. McGarrah!")
main.geometry("1000x505")
var = IntVar()
editingBox = Frame(main)

undoButton = Button(main, text = "Take me back to the last Trevor", command = undoFunc, font = 20)
undoButton.pack(side = BOTTOM, pady = 10)

formatLabel = Label(editingBox, text = "McFormat", font = 16)
formatLabel.pack(side = TOP, pady = 10)

SharpenButton = Button(editingBox, text = "Sharpen Trevor", command = sharpenImgFunc, width = 20)
SharpenButton.pack(side = TOP)

blurButton = Button(editingBox, text = "Blur Trevor",
command = blurImgFunc, width = 20)
blurButton.pack(side = TOP)

cropButton = Button(editingBox, text = "Crop Trevor", 
command = cropImgFunc, width=20)
cropButton.pack(side = TOP)
                
rotateCounterButton = Button(editingBox, text = "Rotate Trevor CCW", command = rotateCounterFunc, width = 20)
rotateCounterButton.pack(side = TOP)

rotateClockButton = Button(editingBox, text= "Rotate Trevor CW", command = 
rotateClockFunc, width = 20)
rotateClockButton.pack(side = TOP)

img = ImageTk.PhotoImage(Image.open('image' + str(counter) + '.jpg'))
panel = Label(main, image = img)
panel.pack(side = LEFT, padx = 20)

negativeButton = Button(editingBox, text = "Trevor negative",
command = negativeImgFunc, width = 20)
negativeButton.pack(side = BOTTOM)

foilButton = Button(editingBox, text = "Foil McGarrah",
command = foilImgFunc, width = 20)
foilButton.pack(side = BOTTOM)

pencilButton = Button(editingBox, text = "Pencil McGarrah", 
command = pencilImgFunc, width = 20)
pencilButton.pack(side = BOTTOM)

oilButton = Button(editingBox, text="Oil McGarrah", 
command=oilImgFunc, width = 20)
oilButton.pack(side = BOTTOM)

sketchButton = Button(editingBox, text = "Sketch light McGarrah", 
command = sketchImgFunc, width = 20)
sketchButton.pack(side = BOTTOM)

filterLabel = Label(editingBox, text = "McFilters", font = 16)
filterLabel.pack(side = BOTTOM, pady = 10)

editingBox.pack()
main.mainloop()