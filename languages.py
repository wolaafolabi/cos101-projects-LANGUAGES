from struct import pack_into

Yoruba_dictionary={"wa":'come',
                   "Olorun":'God',
                    "eshe":'thank u',
                    "ori":'head',
                    "owo":'money',
                    "aja":'Dog',
                    "oju":'eye',
                    "abo":'plate',
                    "ewa":'Beans',
                    "oba":'King',
                    "ete":'lip',
                    "eru":'load',  
                    "aya":'wife',
                    "ata":'pepper',
                    "ara":'body',
                    "obo":'monkey', 
                    "ilu":'drum',
                    "isu":'yam',
                    "ekun":'tears',
                    "okan":'heart'}
from tkinter import Tk,Entry,Button,Label,StringVar

window=Tk()
window.geometry("600x250")
window.title("Yoruba_dictionary")

word: StringVar = StringVar()
word_entry = Entry(window, textvariable=word, font=('ariel',19))
word_entry.pack()


result = StringVar()
result_label =Label(window , textvariable=result)
result_label.pack()


def search (word):
    if word in Yoruba_dictionary:
            result.set(Yoruba_dictionary[word])
            print(Yoruba_dictionary[word])
    else:
            result.set("not found")

search_btn = Button(window, text="search", command=lambda: search(word.get()))
search_btn.pack()


exit_button=Button(window, text="exit",command=lambda: exit())

word_entry =Entry(window, textvariable=word, font=('ariel',19))
window.mainloop()


from struct import pack_into

Tiv_dictionary={"Dooshima":'love',
                 "Doo tuu":'Good Night',
                    "Tor Tiv":'',
                    "ori":'head',
                    "owo":'money',
                    "aja":'Dog',
                    "oju":'eye',
                    "abo":'plate',
                    "ewa":'Beans',
                    "oba":'King',
                    "ete":'lip',
                    "eru":'load',
                    "aya":'wife',
                    "ata":'pepper',
                    "ara":'body',
                    "obo":'monkey',
                    "ilu":'drum',
                    "isu":'yam',
                    "ekun":'tears',
                    "okan":'heart'}
from tkinter import Tk,Entry,Button,Label,StringVar

window=Tk()
window.geometry("600x250")
window.title("Yoruba_dictionary")

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


from struct import pack_into

Hausa_dictionary={"salamu":'hello',
                 "Na gode":'Thank you',
                    "Ina Kwana":'Goodnight',
                    "Sai":'Goodbye',
                    "Gida":'House',
                    "Rana":'Sun',
                    "Mota":'car',
                    "Uwa":'Mother',
                    "Kanu":'hunger',
                    "Baba":'father',
                    "Yarinya":'Girl',
                    "Yaro":'boy',
                    "Ruwa":'water',
                    "malam":'teacher',
                    "sabu":'patience',
                    "kare":'old',
                    "doki":'horse',
                    "ina yin kwa":'Good morning',
                    "koshi":'thirst',
                    "Alhamdu":'Praise be to God'}
from tkinter import Tk,Entry,Button,Label,StringVar

window=Tk()
window.geometry("600x250")
window.title("Hausa_dictionary")

word: StringVar = StringVar()
word_entry = Entry(window, textvariable=word, font=('ariel',19))
word_entry.pack()


result = StringVar()
result_label =Label(window , textvariable=result)
result_label.pack()


def search (word):
    if word in Hausa_dictionary:
            result.set(Hausa_dictionary[word])
            print(Hausa_dictionary[word])
    else:
            result.set("not found")

search_btn = Button(window, text="search", command=lambda: search(word.get()))
search_btn.pack()


exit_button=Button(window, text="exit",command=lambda: exit())

word_entry =Entry(window, textvariable=word, font=('ariel',19))
window.mainloop()



