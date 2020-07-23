import numpy as np
import tkinter as tk
from tkinter import ttk as ttk
# from time import sleep
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
txt.tag_configure('prediction', foreground='#bfbfbf')


def alpha(event):
    global cur_word, rel_words
    print(event)
    # print("pressed", repr(event.char))
    typed_key = event.char
    if typed_key.isalnum():
        #delete previous guess
        txt.delete('insert',tk.END)
        cur_word+=typed_key.lower()
        cur_index =  txt.index('insert')
        rel_words = rel_words[np.char.startswith(rel_words,cur_word)]
        try:
            idx=0
            guess_word = rel_words[0]    
            while(len(guess_word)==len(cur_word)):
                idx+=1
                guess_word = rel_words[idx]
            txt.insert(tk.END,guess_word[len(cur_word):],'prediction')
        except:
            pass
        print(txt.index('insert'))
        txt.mark_set("insert", cur_index)
        print("word:",cur_word)
    
    elif typed_key == '\t':
        txt.tag_remove("prediction",  "1.0", tk.END)
        txt.mark_set("insert", tk.END)
        if len(cur_word)>0:
            txt.insert(tk.END,' ')
        else:
            txt.insert(tk.END,'\t')
        cur_word = ''
        rel_words = com_words

    elif event.keysym == 'BackSpace':  
        # if(event.state=='8'):
        # print(event.state)
        txt.delete('insert',tk.END)
        cur_index =  txt.index('insert') 
           
        if txt.get('insert-1c',tk.INSERT).isalnum():
            cur_word = txt.get('1.0',tk.END).split()[-1].lower()
            rel_words = com_words[np.char.startswith(com_words,cur_word)]
            try:
                txt.insert(tk.END,rel_words[0][len(cur_word):],'prediction')
            except:
                pass
        else:
            cur_word = ''
        txt.mark_set("insert", cur_index)
        print("word:",cur_word)

    elif event.keysym == 'space':
        txt.delete('insert',tk.END)
        cur_word = ''
        rel_words = com_words
    # else:
    #     txt.delete('insert',tk.END)
    #     cur_word = ''
    #     rel_words = com_words


#disable normal tab function
def tabdown(event):
    return ("break")


txt.bind("<KeyRelease>", alpha)
txt.bind("<Tab>", tabdown)
# txt.bind("<Meta_L-s>", lambda: print("SAVE"))

scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side='right',fill='y')
txt.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview)
root.mainloop()