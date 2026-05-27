# =====================================================
# AI LANGUAGE TRANSLATION TOOL (FULL WORKING VERSION)
# =====================================================

from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pygame
from datetime import datetime
from unidecode import unidecode
import time
import os
import threading

# ---------------- SETUP ---------------- #

translator = Translator()
pygame.mixer.init()

history_data = []

# ---------------- LANGUAGE MAP (AUTO ALL LANGUAGES) ---------------- #

LANG_MAP = {lang.title(): code for code, lang in LANGUAGES.items()}

# ---------------- MAIN WINDOW ---------------- #

root = Tk()
root.title("AI Translator Tool")
root.state("zoomed")
root.configure(bg="#0f0f0f")

# ---------------- HEADER ---------------- #

header = Frame(root, bg="#1a1a1a", height=60)
header.pack(fill=X)

Label(
    header,
    text="🌍 AI Translator Pro",
    font=("Helvetica", 18, "bold"),
    bg="#1a1a1a",
    fg="#00ffcc"
).pack(pady=15)

# ---------------- INPUT ---------------- #

input_box = Text(root, height=4, bg="#1e1e1e", fg="white",
                 insertbackground="white", font=("Arial", 12))
input_box.pack(padx=10, pady=10, fill=X)

# ---------------- LANGUAGE DROPDOWN ---------------- #

selected_lang = StringVar()
selected_lang.set("English")

lang_box = ttk.Combobox(
    root,
    textvariable=selected_lang,
    values=list(LANG_MAP.keys()),
    state="readonly"
)
lang_box.pack(pady=5)

# ---------------- OUTPUT ---------------- #

Label(root, text="Translated Text (Output)",
      bg="#0f0f0f", fg="white",
      font=("Arial", 11, "bold")).pack()

output_box = Text(root, height=4, bg="#1e1e1e", fg="#00ff99",
                   insertbackground="white", font=("Arial", 12))
output_box.pack(padx=10, pady=5, fill=X)

Label(root, text="Readable (English style)",
      bg="#0f0f0f", fg="gray").pack()

roman_box = Text(root, height=3, bg="#111111", fg="white",
                 insertbackground="white")
roman_box.pack(padx=10, pady=5, fill=X)

# ---------------- STATUS ---------------- #

status = Label(root, text="Ready - Enter text and click Translate",
               bg="#0f0f0f", fg="gray")
status.pack()

def update_status(msg):
    status.config(text=f"{msg} | {datetime.now().strftime('%H:%M:%S')}")

# ---------------- TRANSLATE ---------------- #

def translate_text():
    def run():
        text = input_box.get("1.0", END).strip()

        if not text:
            messagebox.showwarning("Warning", "Enter text")
            return

        lang = LANG_MAP[selected_lang.get()]

        try:
            result = translator.translate(text, dest=lang)

            output_box.delete("1.0", END)
            output_box.insert(END, result.text)

            readable = unidecode(result.text)

            roman_box.delete("1.0", END)
            roman_box.insert(END, readable)

            add_history(text, result.text, readable)
            update_status("Translated")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    threading.Thread(target=run, daemon=True).start()

# ---------------- SPEAK ---------------- #

def speak():
    def run():
        text = output_box.get("1.0", END).strip()

        if not text:
            messagebox.showwarning("Warning", "No text to speak")
            return

        try:
            lang = LANG_MAP[selected_lang.get()]

            filename = "voice.mp3"

            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

            time.sleep(0.2)

            if os.path.exists(filename):
                try:
                    os.remove(filename)
                except:
                    pass

            tts = gTTS(text=text, lang=lang)
            tts.save(filename)

            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            update_status("Speaking")

        except Exception as e:
            messagebox.showerror("Voice Error", str(e))

    threading.Thread(target=run, daemon=True).start()

# ---------------- CLEAR ---------------- #

def clear_all():
    input_box.delete("1.0", END)
    output_box.delete("1.0", END)
    roman_box.delete("1.0", END)
    update_status("Cleared")

# ---------------- HISTORY ---------------- #

def add_history(original, translated, readable):
    history_data.append((original, translated, readable))
    history_listbox.insert(END, f"{original} → {translated}")

def delete_history():
    selected = history_listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select item to delete")
        return

    index = selected[0]
    history_listbox.delete(index)
    history_data.pop(index)

    update_status("History Deleted")

def show_selected(event):
    selected = history_listbox.curselection()
    if not selected:
        return

    i = selected[0]
    original, translated, readable = history_data[i]

    output_box.delete("1.0", END)
    output_box.insert(END, translated)

    roman_box.delete("1.0", END)
    roman_box.insert(END, readable)

# ---------------- BUTTONS ---------------- #

btn_frame = Frame(root, bg="#0f0f0f")
btn_frame.pack(pady=10)

Button(btn_frame, text="Translate", command=translate_text,
       bg="#00c853", fg="white", width=12).grid(row=0, column=0, padx=5)

Button(btn_frame, text="Speak", command=speak,
       bg="#2962ff", fg="white", width=12).grid(row=0, column=1, padx=5)

Button(btn_frame, text="Clear", command=clear_all,
       bg="#d50000", fg="white", width=12).grid(row=0, column=2, padx=5)

Button(btn_frame, text="Delete History", command=delete_history,
       bg="#ff6d00", fg="white", width=15).grid(row=0, column=3, padx=5)

Button(btn_frame, text="Exit", command=root.destroy,
       bg="gray", fg="white", width=10).grid(row=0, column=4, padx=5)

# ---------------- HISTORY ---------------- #

history_frame = Frame(root, bg="#0f0f0f")
history_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

Label(history_frame, text="Translation History",
      fg="white", bg="#0f0f0f",
      font=("Arial", 12, "bold")).pack(anchor="w")

history_listbox = Listbox(
    history_frame,
    bg="#1e1e1e",
    fg="white",
    height=10,
    selectbackground="#00c853",
    font=("Arial", 11)
)

scrollbar = Scrollbar(history_frame)
history_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=history_listbox.yview)

history_listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

history_listbox.bind("<<ListboxSelect>>", show_selected)

# ---------------- RUN ---------------- #

root.mainloop()