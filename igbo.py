from struct import pack_into

Igbo_dictionary={"abali":'night',
                   "abuo":'two',
                    "ahia":'market',
                    "afa":'name',
                    "bata":'enter',
                    "biko":'please',
                    "bia":'come',
                    "chere":'wait',
                    "chukwu":'God',
                    "chineke":'lord',
                    "di":'husband',
                    "ebe":'place',
                    "ofe":'soup',
                    "e-e":'yes',
                    "echi":'tomorrow',
                    "ego":'money',
                    "ehi":'cow',
                    "oka":'corn',
                    "enu":'top',
                    "olu":'work'}
from tkinter import Tk,Entry,Button,Label,StringVar

window=Tk()
window.geometry("600x250")
window.title("Igbo_dictionary")

word: StringVar = StringVar()
word_entry = Entry(window, textvariable=word, font=('ariel',19))
word_entry.pack()


result = StringVar()
result_label =Label(window , textvariable=result)
result_label.pack()


def search (word):
    if word in Igbo_dictionary:
            result.set(Igbo_dictionary[word])
            print(Igbo_dictionary[word])
    else:
            result.set("not found")

search_btn = Button(window, text="search", command=lambda: search(word.get()))
search_btn.pack()


exit_button=Button(window, text="exit",command=lambda: exit())

word_entry =Entry(window, textvariable=word, font=('ariel',19))
window.mainloop()

