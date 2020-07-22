import tkinter as tk
from tkinter import ttk as ttk
from time import sleep
from tkinter import font

cur_word = ''

root = tk.Tk()
root.title("Text Predictor")
appFont = font.Font(family='menlo', size=12)

txt = tk.Text(root,highlightthickness=0 , font = appFont)
txt.pack(fill=tk.BOTH,side='left', expand=1)
def key(event):
    typed_char = eval(repr(event.char))
    print(repr(event.char))
    if typed_char.isalnum():
        print("pressed", repr(event.char))
        cur_index =  txt.index('insert')
        txt.insert(tk.END,'a')
        print(txt.index('insert'))
        txt.mark_set("insert", cur_index)
        # txt.mark_set("%s-4c" % tk.INSERT, tk.INSERT)
        # txt.icursor(tk.END-1)


txt.bind("<KeyRelease>", key)
# txt.tag_configure("gray", foreground="gray")
# # apply the tag "red" 
# txt.highlight_pattern("word", "gray")
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side='right',fill='y')
txt.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview)
root.mainloop()