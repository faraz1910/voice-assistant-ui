
from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")



root = ctk.CTk()
root.geometry("500x500")


#Replace button images file w.r.t your system

image_not_press = ctk.CTkImage(Image.open("D:/Pragramming Languages/Python/tkinter/Project_Voice_Recognition/assets/bb2.png"), size=(200, 200))
image_pressed = ctk.CTkImage(Image.open("D:/Pragramming Languages/Python/tkinter/Project_Voice_Recognition/assets/ba.png"), size=(200, 200))


# Changing button image to white
def btn_not_pressed():
    button.configure(image=image_not_press)

# Changing button image to green
def btn_pressed():
    button.configure(image=image_pressed)


def functioning():
    btn_pressed()

    """
    Code to be executed
    """

    btn_not_pressed()



frame = ctk.CTkFrame(root)
frame.pack(padx=10, pady=10, fill='both', expand='True')

label = ctk.CTkLabel(frame, text="Voice Assistant", font=ctk.CTkFont(size=30))
label.pack(pady=(40,10))

button = ctk.CTkButton(frame, text="", image=image_not_press, border_width=0, command= lambda: functioning(), fg_color="#2a2b2a", hover_color="#2a2b2a")
button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)



root.mainloop()