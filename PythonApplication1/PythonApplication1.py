root = Tk()
root.title("Анкета")
root.geometry("340x700")



name = StringVar()
surname = StringVar()
patronymic = StringVar()
date = StringVar()
another_data=StringVar()
 
name_label = Label(text="Имя")
surname_label = Label(text="Фамилию")
patronymic_label = Label(text="Отчество")
date_label= Label(text="Дата рождения")
header_label = Label(text="                   Пол", padx=15, pady=10)
header_label.grid(row=4, column=0, sticky=W)
header = Label(text="                          Семейный статус", padx=15, pady=10)
header.grid(row=7, column=0, sticky=W)
another_data_label = Label(text="Дополнительная информация")
another_data_label.grid(row=10, column=0, sticky=W)
save = Button(text="Сохранить")
 
lang = IntVar()
 
man_checkbutton = Radiobutton(text="Мужской", value=1, variable=lang, padx=15, pady=10)
man_checkbutton.grid(row=5, column=0, sticky=W)
 
wooman_checkbutton = Radiobutton(text="Женский", value=2, variable=lang, padx=15, pady=10)
wooman_checkbutton.grid(row=6, column=0, sticky=W)
 
selection = Label(textvariable=lang, padx=15, pady=10)
selection.grid(row=4, column=0, sticky=W)

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
patronymic_label.grid(row=2, column=0, sticky="w")
date_label.grid(row=3, column=0, sticky="w")

lang = IntVar()
 
married_checkbutton = Radiobutton(text="Женат(а)", value=1, variable=lang, padx=15, pady=10)
married_checkbutton.grid(row=8, column=0, sticky=W)
 
unmarried_checkbutton = Radiobutton(text="Холост(а)", value=2, variable=lang, padx=15, pady=10)
unmarried_checkbutton.grid(row=9, column=0, sticky=W)
 
selection = Label(textvariable=lang, padx=15, pady=10)
selection.grid(row=4, column=0, sticky=W)

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
patronymic_label.grid(row=2, column=0, sticky="w")
date_label.grid(row=3, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
patronymic_entry = Entry(textvariable=patronymic)
date_entry = Entry(textvariable=date)
another_data_entry = Entry(textvariable=another_data)
 
name_entry.grid(row=0,column=1, padx=5, pady=5)
surname_entry.grid(row=1,column=1, padx=5, pady=5)
patronymic_entry.grid(row=2,column=1, padx=5, pady=5)
date_entry.grid(row=3,column=1, padx=1 , pady=3)
another_data_entry.grid(row=10,column=1,padx=4,pady=5)
save.grid(row=11,column=1,padx=4,pady=5)

def saving():
    str1 = name_entry.get()
    str2 = surname_entry.get()
    str3 = patronymic_entry.get()
    str4 = date_entry.get()
    str5 = another_data_entry.get()

    text = ""
    text += str1 + "\n"
    text += str2 + "\n"
    text += str3 + "\n"
    text += str4 + "\n"
    text += str5 + "\n"
    with open("Анкета.txt", "w") as somefile:
        somefile.write(text)

root.mainloop()