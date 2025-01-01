from struct import pack_into

Tiv_dictionary={"Dooshima":'love',
                 "Doo tuu":'Good Night',
                    "Tor Tiv":'king',
                    "Aondo Ter":'God Father',
                    "etiou":'head',
                    "toxo":'ear',
                    "Ci":'egg',
                    "hinga":'nose',
                    "ido":'good',
                    "orili":'black',
                    "tuwu":'night',
                    "su":'fire',
                    "indohore":'cold',
                    "popo":'white',
                    "la":'rain',
                    "ngolem":'water',
                    "Ele":'moon',
                    "mva":'come',
                    "ngua":'hear',
                    "nange":'see'}
from tkinter import Tk,Entry,Button,Label,StringVar

window=Tk()
window.geometry("600x250")
window.title("Tiv_dictionary")

word: StringVar = StringVar()
word_entry = Entry(window, textvariable=word, font=('ariel',19))
word_entry.pack()


result = StringVar()
result_label =Label(window , textvariable=result)
result_label.pack()


def search (word):
    if word in Tiv_dictionary:
            result.set(Tiv_dictionary[word])
            print(Tiv_dictionary[word])
    else:
            result.set("not found")

search_btn = Button(window, text="search", command=lambda: search(word.get()))
search_btn.pack()


exit_button=Button(window, text="exit",command=lambda: exit())

word_entry =Entry(window, textvariable=word, font=('ariel',19))
window.mainloop()

