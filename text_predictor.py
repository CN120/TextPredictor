import numpy as np
import tkinter as tk
from tkinter import ttk as ttk
from time import sleep
from tkinter import font

#common words
com_words = np.loadtxt("google-10000-english-usa-no-swears.txt", dtype=str, delimiter='\n')
rel_words = com_words 
#relavant words

cur_word = ''

root = tk.Tk()
root.unbind_all("<Tab>")
root.title("Text Predictor")
appFont = font.Font(family='menlo', size=12)

txt = tk.Text(root,highlightthickness=0 , font = appFont)
txt.pack(fill=tk.BOTH,side='left', expand=1)
txt.tag_configure('gray', foreground='#bfbfbf')

def alpha(event):
    global cur_word, rel_words
    print(event)
    print("pressed", repr(event.char))
    typed_char = event.char
    if typed_char.isalnum():
        txt.delete('insert',tk.END)
        cur_word+=typed_char
        cur_index =  txt.index('insert')
        rel_words = rel_words[np.char.startswith(rel_words,cur_word)]
        try:
            txt.insert(tk.END,rel_words[0][len(cur_word):],'gray')
        except:
            pass
        print(txt.index('insert'))
        txt.mark_set("insert", cur_index)
        print(cur_word)
    elif typed_char == '\t':
        txt.tag_remove("gray",  "1.0", tk.END)
        txt.mark_set("insert", tk.END)
        txt.insert(tk.END,' ')
        cur_word = ''
        rel_words = com_words
    elif typed_char == '\x7f':
        cur_word = cur_word[:-1]
    else:
        txt.delete('insert',tk.END)
        cur_word = ''
        rel_words = com_words

def tabdown(event):
    return ("break")
    # global cur_word, rel_words
    # txt.delete('insert',tk.END)
    # root.update()
    # txt.insert(tk.END,rel_words[0][len(cur_word):])
    # rel_words = com_words
    # print("yes")


txt.bind("<KeyRelease>", alpha)
txt.bind("<Tab>", tabdown)
# # apply the tag "red" 
# txt.highlight_pattern("word", "gray")
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side='right',fill='y')
txt.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview)
root.mainloop()