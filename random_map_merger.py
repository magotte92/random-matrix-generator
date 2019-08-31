import random
import os

def shuffle_string(string):
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)


def tuple_constructor(list_to_fill, inventory, season_x: int, season_y: int):
    counter = 0
    while season_x != 0 and season_y != 0:
        if counter == 0:  # ορίζω την αρχή
            list_to_fill.insert(0, inventory[0])
            season_x -= int(inventory[0].size_gen[0])
            season_y -= int(inventory[0].size_gen[1])
        else:
            r = random.randrange(5, len(inventory))
            season_x -= int(
                inventory[r].size_gen[0])
            if season_x < 0:  # Ελέγχω αν έκανα μλκια
                season_x += int(inventory[r].size_gen[0])  # Αν έκανα μλκια το ξαναβάζω στην θέση του
            else:
                season_y -= int(
                    inventory[r].size_gen[1])  # Εφόσον δεν έκανα μλκια αφαιρώ το μέγεθος του y απο τον χάρτη
                if season_y < 0:  # Υπάρχει ακόμα μια περίπτωση να έκανα μλκια
                    season_y += int(inventory[r].size_gen[1])  # Οπότε ξαναπροσθέτω
                else:  # Αφού αποφύγαμε τις τυχόν μλκιες πάμε να κάνουμε κάτι κουλ
                    print(inventory[r].title_gen)
                    if counter % 2:  # Αν το x διαιρείται τέλεια με το 2 βάζει το μπλοκ στα δεξιά ;)
                        list_to_fill.insert(0, inventory[r])
                    else:  # Αλλιώς το βάζει στα αριστερά(νομίζω σε βλέπω να χαμογελάς)
                        list_to_fill.insert(len(list_to_fill), inventory[r])
        counter += 1
    return list_to_fill


def random_map_maker(mapper):
    setter = []
    directory = os.path.abspath(str(os.path.dirname(__file__)) + '\\mapper.txt')
    if not os.path.exists(directory):
        open('mapper.txt', 'a').close()

    with open('mapper.txt', mode='r+') as source:
        source.truncate()
        source.seek(0)
        for item in range(len(mapper)):
            for line in mapper[item].huge_dic_gen.values():
                for i in range(len(line)):
                    setter.append(str(line[i]) + ',')
                if ',' in setter[-1] and i == len(line) - 1:
                    setter[-1] = setter[-1].replace(',', '\n')
        source.writelines(setter)


def random_map_filler():
    bigger = 0
    with open('mapper.txt', 'r') as f:
        line = f.readlines()
        for i in line:
            space_x = len(i.replace(' ', '').replace('\n', '').replace('@', '3').replace(',', ''))
            if space_x >= bigger:
                bigger = space_x

    with open('mapper.txt', mode='r') as source:
        with open('setter.txt', mode='w') as target:
            for line in source:
                space_x = len(line.replace(' ', '').replace('\n', '').replace('@', '3').replace(',', ''))
                difference = bigger - space_x
                if difference != 0:
                    if difference % 2 == 0:
                        real_factor = difference / 4
                        if real_factor == int(real_factor) and real_factor != 1:
                            fake_factor = difference / 2
                            zero_factor = difference - fake_factor - real_factor
                        else:
                            real_factor = 0
                            fake_factor = difference / 2
                            zero_factor = difference - fake_factor - real_factor
                    elif difference % 3 == 0:
                        real_factor = difference / 6
                        if real_factor == int(real_factor) and real_factor != 1:
                            fake_factor = difference / 3
                            zero_factor = difference - fake_factor - real_factor
                        else:
                            real_factor = 0
                            fake_factor = difference / 3
                            zero_factor = difference - fake_factor - real_factor
                    elif difference % 5 == 0:
                        real_factor = difference / 5
                        if real_factor == int(real_factor) and real_factor != 1:
                            fake_factor = difference / 5
                            zero_factor = difference - fake_factor - real_factor
                        else:
                            real_factor = 0
                            fake_factor = difference / 5
                            zero_factor = difference - fake_factor - real_factor
                    elif difference % 11 == 0:
                        real_factor = difference - 8
                        fake_factor = difference - 4
                        zero_factor = difference - real_factor - fake_factor
                    else:
                        raise ValueError

                    fake_factor = int(fake_factor)
                    real_factor = int(real_factor)
                    zero_factor = int(zero_factor)
                    summarize = fake_factor + real_factor + zero_factor
                    fake = fake_factor * '2'
                    real = real_factor * '1'
                    zero = zero_factor * '0'
                    if summarize != difference:
                        raise ValueError
                    else:

                        str_to_append = fake + zero + real
                        str_to_append = shuffle_string(str_to_append)
                        str_to_append = ',' + ','.join(str_to_append)
                else:
                    str_to_append = ''

                line = line.replace('\n', '')
                line = line + str_to_append + '\n'
                target.write(line)