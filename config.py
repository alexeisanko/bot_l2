COORD_CITIES = {'Глудио': (1, 2),
                'Дион': (1, 2),
                'Гиран': (1, 2),
                'Орен': (1, 2),
                'Аден': (1, 2),
                'Штудгарт': (1, 2),
                'Годдарт': (1, 2),
                'Руна': (1, 2)
                }

COORD_SEEDS = {'1': (1, 2),
               '2': (1, 2),
               '3': (1, 2),
               '4': (1, 2),
               '5': (1, 2),
               }

COORD_STEP = {'change': (1, 2),


}


def create_config():
    print('Выберите город, в который будете сдавать семена \nГлудио\nДион\nГиран\nОрен\nАден\nШтудгарт\nГоддарт\nРуна')
    city = input()
    print('Выберите номер семян для сдачи: \n')
    seeds = input()
    try:
        coord_city = COORD_CITIES[city]
        cord_seed = COORD_CITIES[seeds]
    except KeyError:
        print('Выбранного города или номера семян не сушествует, попробуйте ввести заного')
        create_config()
    return coord_city, cord_seed
