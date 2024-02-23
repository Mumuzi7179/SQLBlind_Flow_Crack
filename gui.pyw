import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
import threading
import os
from crack import *

selected_file_path = None

def choose_file():
    global selected_file_path
    filepath = filedialog.askopenfilename()
    if filepath:
        filepath_fixed = filepath.replace('\\', '/')
        name = os.path.basename(filepath)
        file_label.config(text=name)
        selected_file_path = filepath_fixed

def drop(event):
    global selected_file_path
    filepath = re.findall(r'{(.*?)}', event.data)
    if filepath:
        filepath_fixed = filepath[0].replace('\\', '/')
    else:
        filepath_fixed = event.data.replace('\\', '/')
    name = os.path.basename(filepath_fixed)
    file_label.config(text=name)
    selected_file_path = filepath_fixed

def run_crack():
    if selected_file_path:
        threading.Thread(target=run_crack_thread, args=(selected_file_path, text_box)).start()
    else:
        text_box.insert(tk.END, "No file selected.\n")

def run_crack_thread(selected_file_path, text_box):
    def gui_update(action, *args, **kwargs):
        if action == 'delete':
            text_box.delete(*args, **kwargs)
        elif action == 'insert':
            text_box.insert(*args, **kwargs)
        elif action == 'config':
            text_box.tag_config(*args, **kwargs)

    text_box.after(0, gui_update, 'delete', "1.0", tk.END)
    text_box.after(0, gui_update, 'insert', tk.END, "正在尝试分析，请稍后...\n")
    output = mains(selected_file_path)
    text_box.after(0, gui_update, 'insert', tk.END, "分析结果如下，以下是可能出现的结果:\n")

    highlight_words = ["flag", "pass", "ctf", "Zmxh",]
    for item in output:
        if len(item) != 0:
            highlight_in_item(item, highlight_words, text_box, gui_update)

def highlight_in_item(item, words, text_box, gui_update):
    start = 0
    while start < len(item):
        matched_word = None
        matched_index = len(item)
        for word in words:
            index = item.find(word, start)
            if index != -1 and index < matched_index:
                matched_word = word
                matched_index = index

        if matched_word:
            text_box.after(0, gui_update, 'insert', tk.END, item[start:matched_index])
            text_box.after(0, gui_update, 'insert', tk.END, matched_word, "highlight")
            start = matched_index + len(matched_word)
        else:
            text_box.after(0, gui_update, 'insert', tk.END, item[start:] + '\n\n')
            break

root = TkinterDnD.Tk()
root.title("SQL流量一把梭 尝鲜版")

root.iconbitmap('./img/myico.ico')
root.configure(background='#F3E5CB')

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

text_box = tk.Text(root, height=10)
text_box.grid(row=1, column=0, columnspan=3, sticky="nsew")
text_box.tag_config("highlight", foreground="red")

choose_file_button = tk.Button(root, text="Choose File", command=choose_file)
choose_file_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

root.grid_columnconfigure(1, weight=1)
file_label = tk.Label(root, text="No file selected", anchor='w')
file_label.grid(row=0, column=1, sticky="w", padx=10, pady=10)

crack_button = tk.Button(root, text="Crack", command=run_crack)
crack_button.grid(row=0, column=2, sticky="ne", padx=10, pady=10)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.geometry("700x400")
root.mainloop()
