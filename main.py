from tkinter import *

import tkintermapview


users:list=[]

class Users():
    def __init__(self,name,surname,location,posts,coordinates):
        self.name = name
        self.surname = surname
        self.location = location
        self.posts = posts
        self.coordinates = self.get_coordinates()
        self.marker=map_widget.set_marker(self.user.coordinates[0],self.user.coordinates[1])
def get_coordinates(self)->list:
    import requests
    from bs4 import BeautifulSoup
    url=f"https://pl.wikipedia.org/wiki/{self.location}"
    response=requests.get(url).text
    response_html=BeautifulSoup(response,"html.parser")
    longitude=float(response_html.select(".longitude")[1].text.replace(",","."))
    latitude=float(response_html.select(".latitude")[1].text.replace(",","."))
    print(longitude)
    print(latitude)
    return [latitude, longitude]



def add_user():
    zmienna_imie=entry_name.get()
    zmienna_nazwisko=entry_surname.get()
    zmienna_miejscowosc=entry_location.get()
    zmienna_posts=entry_posts.get()
    user={'name':zmienna_imie,'surname':zmienna_nazwisko,'location':zmienna_miejscowosc,'posts':zmienna_posts}
    user=Users(name=zmienna_imie, surname=zmienna_nazwisko, location=zmienna_miejscowosc, posts=zmienna_posts)
    users.append(user)


    entry_name.delete(0,END)
    entry_surname.delete(0,END)
    entry_location.delete(0,END)
    entry_posts.delete(0,END)

    entry_name.focus()



    print(user)
    show_users()



def show_users():
    listbox_lista_obiektow.delete(0,END)
    for idx,user in enumerate(users):
        listbox_lista_obiektow.insert(idx,f'{idx+1}. {user.name} {user.surname}')



def remove_user():
    i=listbox_lista_obiektow.index(ACTIVE)
    users[i].marker.delete()
    users.pop(i)
    show_users()

def edit_user():
    i=listbox_lista_obiektow.index(ACTIVE)
    name=users[i].name
    surname=users[i].surname
    location=users[i].location
    posts=users[i].posts

    entry_name.insert(0,name)
    entry_surname.insert(0,surname)
    entry_location.insert(0,location)
    entry_posts.insert(0,posts)

    button_dodaj_obiekt.config(text='zapisz',command=lambda: update_user(i))


def update_user(i):
    new_name=entry_name.get()
    new_surname=entry_surname.get()
    new_location=entry_location.get()
    new_posts=entry_posts.get()

    users[i].name=new_name
    users[i].surname=new_surname
    users[i].location=new_location
    users[i].posts=new_posts

    users[i].marker.delete()
    users[i].coordinates =self.get_coordinates()

    entry_name.delete(0,END)
    entry_surname.delete(0,END)
    entry_location.delete(0,END)
    entry_posts.delete(0,END)

    button_dodaj_obiekt.config(text='Dodaj obiekt',command=add_user)


def show_user_details():
    i=listbox_lista_obiektow.index(ACTIVE)
    name=users[i].name
    surname=users[i].surname
    location=users[i].location
    posts=users[i].posts
    label_szczegoly_name_wartosc.config(text=name)
    label_szczegoly_surname_wartosc.config(text=surname)
    label_szczegoly_location_wartosc.config(text=location)
    label_szczegoly_posts_wartosc.config(text=posts)
    map_widget.set_position(users[i].coordinates[0],users[i].coordinates[1])
    map_widget.set_zoom(15)



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
entry_posts = Entry(ramka_formularz)
entry_posts.grid(row=4, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text='Dodaj obiekt', command=add_user)
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
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)















root.mainloop()



