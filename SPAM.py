from tkinter import *
from PIL import Image, ImageTk

app = Tk()
photo = Image.open(r"C:/Users/abdul/Downloads/images.jpg")
photo = photo.resize((200  200))
img = ImageTk.PhotoImage(photo)

for i in range(50):
    fenetre = Toplevel(app)
    fenetre.geometry("+"+ str(50 + i * 60)+ "+" + str(50 + i * 40))
    Label(fenetre, image=img).pack()

app.mainloop()
