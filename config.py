COORD_CITIES = {'Глудио': (929, 651),
                'Дион': (929, 668),
                'Гиран': (929, 685),
                'Орен': (929, 701),
                'Иннадрил': (929, 719),
                'Штудгарт': (929, 737),
                }

COORD_SEEDS = {'1': (742, 464),
               '2': (742, 482),
               '3': (742, 501),
               '4': (742, 518),
               '5': (742, 536),
               }

COORD_STEP = {'change': (712, 688),
              'choose_city': (1049, 618),
              'count_seeds': (960, 640),
              'sell': (1131, 689),
              }


def create_config():
    print('Выберите город, в который будете сдавать семена \nГлудио\nДион\nГиран\nОрен\nАден\nШтудгарт\nГоддарт\nРуна\n')
    city = input()
    print('Выберите номер семян для сдачи: \n')
    seeds = input()
    print('Введите количество семян: \n')
    count_seeds = input()

    try:
        coord_city = COORD_CITIES[city]
        cord_seed = COORD_CITIES[seeds]
    except KeyError:
        print('Выбранного города или номера семян не сушествует, попробуйте ввести заного')
        create_config()
    return coord_city, cord_seed, count_seeds
