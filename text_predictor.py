import numpy as np
import tkinter as tk
from tkinter import ttk as ttk
from time import sleep
from tkinter import font


com_words = np.loadtxt("google-10000-english-usa-no-swears.txt", dtype=str, delimiter='\n')
print(com_words)
cur_word = ''

root = tk.Tk()
root.title("Text Predictor")
appFont = font.Font(family='menlo', size=12)

txt = tk.Text(root,highlightthickness=0 , font = appFont)
txt.pack(fill=tk.BOTH,side='left', expand=1)
txt.tag_configure('gray', foreground='#bfbfbf')

def key(event):
    global cur_word
    txt.delete('insert',tk.END)
    print("pressed", repr(event.char))
    typed_char = event.char
    if typed_char.isalnum():
        cur_word+=typed_char
        cur_index =  txt.index('insert')
        word_bool_arr = np.char.startswith(com_words,cur_word)
        found_list = com_words[word_bool_arr]
        try:
            txt.insert(tk.END,found_list[0][len(cur_word):],'gray')
        except:
            pass
        print(txt.index('insert'))
        txt.mark_set("insert", cur_index)
        print(cur_word)
    else:
        cur_word = ''



txt.bind("<KeyRelease>", key)
# # apply the tag "red" 
# txt.highlight_pattern("word", "gray")
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side='right',fill='y')
txt.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview)
root.mainloop()