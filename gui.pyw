import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from crack import *
import threading
import re,os

def choose_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        filepath_fixed = filepath.replace('\\', '/')
        name = os.path.basename(filepath)
        file_label.config(text=name)
        global selected_file_path
        selected_file_path = filepath_fixed

def drop(event):
    filepath = re.findall(r'{(.*?)}', event.data)
    if filepath:
        filepath_fixed = filepath[0].replace('\\', '/')
    else:
        filepath_fixed = event.data.replace('\\', '/')
    name = os.path.basename(filepath_fixed)
    file_label.config(text=name)
    global selected_file_path
    selected_file_path = filepath_fixed


def run_crack():
    if selected_file_path:
        threading.Thread(target=run_crack_thread, args=(selected_file_path,)).start()
    else:
        text_box.insert(tk.END, "No file selected.\n")

def run_crack_thread(selected_file_path):
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, "正在尝试分析，请稍后...\n")
    output = mains(selected_file_path)
    text_box.insert(tk.END, "分析结果如下，以下是可能出现的结果:\n")

    text_box.tag_config("highlight", foreground="red")

    highlight_words = ["flag", "pass", "ctf", "Zmxh"]
    for item in output:
        if len(item) != 0:
            highlight_in_item(item, highlight_words)

def highlight_in_item(item, words):
    start = 0
    while start < len(item):
        end = len(item)
        for word in words:
            index = item.find(word, start)
            if index != -1:
                end = min(end, index)

        if end != len(item):
            text_box.insert(tk.END, item[start:end])
            word = next(word for word in words if item.startswith(word, end))
            text_box.insert(tk.END, word, "highlight")
            start = end + len(word)
        else:
            text_box.insert(tk.END, item[start:] + '\n\n')
            break

root = TkinterDnD.Tk()
root.title("SQL流量一把梭 尝鲜版")

root.iconbitmap('./img/myico.ico')
root.configure(background='#F3E5CB')


selected_file_path = None

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

text_box = tk.Text(root, height=10)
text_box.grid(row=1, column=0, columnspan=3, sticky="nsew")

choose_file_button = tk.Button(root, text="Choose File", command=choose_file)
choose_file_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

root.grid_columnconfigure(1, weight=1)
file_label = tk.Label(root, text="No file selected",anchor='w')
file_label.grid(row=0, column=1, sticky="w", padx=10, pady=10)

crack_button = tk.Button(root, text="Crack", command=run_crack)
crack_button.grid(row=0, column=2, sticky="ne", padx=10, pady=10)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.geometry("700x400")
root.mainloop()
