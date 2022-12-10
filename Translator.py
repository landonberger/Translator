from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox 

#root for tkniter allowing the gui to activate
root = Tk()


def translate_it():

	translated_text.delete(1.0, END)
	
	try:
		# get lang from dictionary keys
		# get the from language key
		for key, value in languages.items():
			if (value == original_combo.get()):
				from_language_key = key
		# get the to language key
		for key, value in languages.items():
			if (value == translated_combo.get()):
				to_language_key = key
		
		# trun orig text into text blob
		words = textblob.TextBlob(original_text.get(1.0, END))
		
		words = words.translate(from_lang=from_language_key , to=to_language_key)
		# trans text
		translated_text.insert(1.0, words)
	
	except Exception as e:
			messagebox.showerror("Translator", e)
	
def clear():
# clear the tex boxes
	original_text.delete(1.0,END)
	translated_text.delete(1.0,END)
# this will grab langauages from goodlge translate
languages = googletrans.LANGUAGES

language_list = list(languages.values())

	
# text box for the content that is inout
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)
# text box for the content that is outoput
translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)
translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)


# combo box
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(30)
translated_combo.grid(row=1, column=2)

# clear button allowing the deletion of text
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()
