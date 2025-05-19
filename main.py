from tkinter import *

import tkintermapview

root = Tk()
root.geometry("1200x760")
root.title("Map Book BK")



ramka_lista_obiektow=Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0,columnspan=2)
ramka_mapa.grid(row=2, column=0,columnspan=2)

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista użytkowników")
label_lista_obiektow.grid(row=0, column=0,columnspan=3)
listbox_lista_obiektow=Listbox(ramka_lista_obiektow, width=50, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż szczegóły')
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_edytuj_obiekt.grid(row=2, column=2)
# ramka_formularz
ramka_formularz=Label(ramka_formularz, text="Formularz")
ramka_formularz.grid(row=0, column=0)
label_name = Label(ramka_formularz, text="Imię:")
label_name.grid(row=1, column=0)
label_surname = Label(ramka_formularz, text="Nazwisko:")
label_surname.grid(row=2, column=0)
label_location = Label(ramka_formularz, text="Miejscowość:")
label_location.grid(row=3, column=0)
label_posts=Label(ramka_formularz, text="Postów:")
label_posts.grid(row=4, column=0)

entry_name = Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
entry_surname = Entry(ramka_formularz)
entry_surname.grid(row=2, column=1)
entry_location = Entry(ramka_formularz)
entry_location.grid(row=3, column=1)
entr_posts = Entry(ramka_formularz)
entr_posts.grid(row=4, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text='Dodaj obiekt')
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

#ramka_szczegoly_obiekow
label_szczegoly_obiektow=Label(ramka_szczegoly_obiektow, text="Szczegóły obiektu")
label_szczegoly_obiektow.grid(row=0, column=0)
label_szczegoly_name=Label(ramka_szczegoly_obiektow, text="Imię:")
label_szczegoly_name.grid(row=1, column=0)
label_szczegoly_name_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_name_wartosc.grid(row=1, column=1)

label_szczegoly_surname=Label(ramka_szczegoly_obiektow, text="Nazwisko:")
label_szczegoly_surname.grid(row=1, column=2)
label_szczegoly_surname_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_surname_wartosc.grid(row=1, column=3)

label_szczegoly_location=Label(ramka_szczegoly_obiektow, text="Miejscowość:")
label_szczegoly_location.grid(row=1, column=4)
label_szczegoly_location_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location_wartosc.grid(row=1, column=5)

label_szczegoly_posts=Label(ramka_szczegoly_obiektow, text="Posty:")
label_szczegoly_posts.grid(row=1, column=6)
label_szczegoly_posts_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_posts_wartosc.grid(row=1, column=7)

# ramka_mapa
map_widget=tkintermapview.TkinterMapView(ramka_mapa, width=800, height=400, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.position([52.23,21.0])















root.mainloop()



