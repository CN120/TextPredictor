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
menubar = tk.Menu(root)

appFont = font.Font(family='menlo', size=12)




txt = tk.Text(root,highlightthickness=0 , font = appFont, wrap=tk.WORD)
txt.pack(fill=tk.BOTH,side='left', expand=1)
txt.tag_configure('gray', foreground='#bfbfbf')

def alpha(event):
    global cur_word, rel_words
    print(event)
    # print("pressed", repr(event.char))
    typed_char = event.char
    if typed_char.isalnum():
        #delete previous guess
        txt.delete('insert',tk.END)
        #add le
        cur_word+=typed_char
        cur_index =  txt.index('insert')
        rel_words = rel_words[np.char.startswith(rel_words,cur_word)]
        try:
            idx=0
            guess_word = rel_words[0]    
            while(len(guess_word)==len(cur_word)):
                idx+=1
                guess_word = rel_words[idx]
            txt.insert(tk.END,guess_word[len(cur_word):],'gray')
        except:
            pass
        print(txt.index('insert'))
        txt.mark_set("insert", cur_index)
        print("word:",cur_word)
    elif typed_char == '\t':
        txt.tag_remove("gray",  "1.0", tk.END)
        txt.mark_set("insert", tk.END)
        txt.insert(tk.END,' ')
        cur_word = ''
        rel_words = com_words
    elif typed_char == '\x7f':  #backspace
        # if(event.state=='8'):
        print(event.state)
        # if event.state==Mod1:
        txt.delete('insert',tk.END)
        cur_word = cur_word[:-1]
        cur_index =  txt.index('insert')
        rel_words = com_words[np.char.startswith(com_words,cur_word)]
        try:
            txt.insert(tk.END,rel_words[0][len(cur_word):],'gray')
        except:
            pass
        txt.mark_set("insert", cur_index)
        print("word:",cur_word)
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