import gpt_part
import customtkinter
from PIL import ImageTk, Image
import time
#gpt_part.record_and_recognize_audio()

window = customtkinter.CTk()
window.geometry("750x750")
window.title("Voice GPT")
window.resizable(True,True)

def choise_theme(choise):
    if choise == "dark-blue":
        with open("theme.txt", "w+") as f:
            f.write("dark-blue")
            speak_lbl.configure(text="Перезагрузите программу")
    elif choise == "green":

        with open("theme.txt", "w+") as f:
            f.write("green")
            speak_lbl.configure(text="Перезагрузите программу")
with open("theme.txt", "r") as f:
    a = f.read()
    customtkinter.set_default_color_theme(a)
    print(a)

def request():
    gpt_part.record()

gen_btn = customtkinter.CTkButton(window, text="Запрос", text_color="black",command=request)
speak_lbl = customtkinter.CTkLabel(window, text="После того как программа зависнет начните говорить через 2-3 секунды", text_color="White")
frame = customtkinter.CTkFrame(window)
theme = customtkinter.CTkComboBox(frame, values=["dark-blue", "green"], command=choise_theme)
img = customtkinter.CTkImage(Image.open("voice-transformed.png"), size=(100,100))
img_lbl = customtkinter.CTkLabel(window, image=img, text="")


img_lbl.grid(row=3, column=1,padx=10,pady=10)
frame.grid(row=4, column=0, padx=20, pady=(200, 10), sticky="s")
speak_lbl.grid(row=2,column=1, padx=10,pady=10)
gen_btn.grid(row=1,column=1, padx=10, pady=10)
theme.grid(row=4,column=1,padx=0,pady=10)

window.mainloop()