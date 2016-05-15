from Tkinter import *
from tkFileDialog import askopenfilename
import Image, ImageTk

Data = [];

if __name__ == "__main__":
    i = 0; clf = 1; s = "apple"
    root = Tk()
    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)

    #adding the image
    File = file("/home/noureldin/Desktop/College/Data Mining/project 2/img.jpg","r");
    #img = ImageTk.PhotoImage(Image.open(File))
    im  = Image.open(File);
    img = ImageTk.PhotoImage(im)
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    #function to be called when mouse is clicked
    def printcoords(event):
	global im,i,s,clf
        #outputting x and y coords to console
        Data.append(list(im.getpixel((event.x,event.y))) + [clf])
        print (event.x,event.y,im.getpixel((event.x,event.y)))
     	i += 1;
        if i == 30: 
		print "============================================";
		s = "leaf";
		clf = 2;
	if i == 50: 
                print "=============================================";
		s = "background";
		clf = 3;
      	print "next one is " + s;
    #mouseclick event
    canvas.bind("<Button 1>",printcoords)
    
    root.mainloop()
    F = file("data.csv","w");
    for d in Data:
	F.write(",".join([str(x) for x in d]) + "\n");
