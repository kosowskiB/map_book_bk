

users:list = [
    {'name':'Maciej','location':'łódź','posts':100},
    {'name':'Mateusz','location':'Poznań','posts':200},
    {'name':'Maciej_1','location':'Siedlce','posts':300},
    {'name':'Konrad','location':'Grudziądz','posts':400},
]


def gets_user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów.')

gets_user_info(users)
