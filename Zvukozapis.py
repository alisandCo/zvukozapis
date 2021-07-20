



genre = ['rock', 'pop', 'classic', 'romance']
disk = {}
genre_singer = {
    'rock' : ['Земфира', 'Чичерина', 'Ночные Снайперы', 'Смысловые Галлюцинации', 'Звери'],
    'pop' : ['Dabro', 'NЮ', 'ANIVAR'],
    'classic' : ['Ólafur Arnalds', 'Fabrizio Paterlini'],
    'romance' : ['Виктория Черенцова', 'Алексей Рыбников']}
disk_singer = {}
singer_traсk = {
    'Земфира' : ['Пальто', 'Жди меня'],
    'Чичерина' : ['Мой рок-н-ролл'],
    'Ночные Снайперы' : ['секунду назад'],
    'Смысловые Галлюцинации' : ['Зачем топтать мою любовь'],
    'Звери' : ['До скорой встречи!'],
    'Dabro' : ['На часах ноль-ноль','На крыше'],
    'NЮ' : ['Я надеюсь'],
    'ANIVAR' : ['Любимый человек'],
    'Ólafur Arnalds' : ['Near Light'],
    'Fabrizio Paterlini' : ['My Misty Mornings'],
    'Виктория Черенцова' : ['Тысячи дорог', 'Мама'],
    'Алексей Рыбников' : ['Я тебя никогда не забуду']
}
disk_track = {}    
track_timing = {'Пальто' : 4.28, 'Жди меня' : 3.15, 'Мой рок-н-ролл' : 6.16, 'секунду назад' : 3.51, 
          'Зачем топтать мою любовь' : 4.23, 'До скорой встречи!' : 4.15, 'На часах ноль-ноль' : 3.26, 
          'Я надеюсь' : 2.59, 'Любимый человек' : 3, 'На крыше' : 3.18, 'Near Light' : 3.24,
          'My Misty Mornings' : 3.22, 'Тысячи дорог' : 3.49, 'Мама' : 3.32, 'Я тебя никогда не забуду' : 2.45
         }

song_long = [
    ['Земфира','Пальто', 4.28, 'rock'],
    ['Земфира','Жди меня', 3.15, 'rock'],
    ['Чичерина','Мой рок-н-ролл', 6.16, 'rock'],
    ['Ночные Снайперы','секунду назад', 3.51, 'rock'],
    ['Смысловые Галлюцинации', 'Зачем топтать мою любовь', 4.23, 'rock'],
    ['Звери','До скорой встречи!', 4.15, ['pop', 'rock']],
    ['Dabro','На часах ноль-ноль', 3.26, 'pop'],
    ['NЮ','Я надеюсь', 2.59, 'pop'],
    ['ANIVAR','Любимый человек', 3, 'pop'],
    ['Dabro','На крыше', 3.18, 'pop'],
    ['Ólafur Arnalds','Near Light', 3.24, 'classic'],
    ['Fabrizio Paterlini','My Misty Mornings',  3.22, 'classic'],
    ['Виктория Черенцова','Тысячи дорог',  3.49, ['romance', 'pop']],
    ['Виктория Черенцова','Мама', 3.32, ['romance', 'pop']],
    ['Алексей Рыбников','Я тебя никогда не забуду',  2.45, 'romance']]

#иерархия по жанру
print("\nИерархия композиций по  жанрам:\n")
for value in sorted(genre_singer.values()):
    for key in genre_singer.keys():
        if genre_singer[key] == value:
            print(key, "-", value)

#иерархия по длительности композиции
print("\nИерархия по длительности композиции:\n")
for value in sorted(track_timing.values()):
     for key in track_timing.keys():
        if track_timing[key] == value:
            print (key,'-' , value)
#иерархия по исполнителю
print("\nИерархия по исполнителю:\n")
for value in sorted(singer_traсk.values()):
     for key in singer_traсk.keys():
        if singer_traсk[key] == value:
            print (key,'-' , value)
#для того чтобы вывести в виде таблицы всю иеррархию
#entries = ['исполнитель','трек', 'время', 'жанр']
#playlist = pd.DataFrame(data = song_long, columns = entries)
#print(playlist)

#запись диска
answer = input("Хотите записать диск?(y/n): ")
while True:
    if answer.lower() == "y":
        print("Выберите жанр в иерархии!")
        while True:
            answer_genre = input("Введите  название жанра\nЕсли хотите закончить то введите n\n ")
            print(disk)
            if answer_genre.lower() != "n":
                if answer_genre in genre_singer:
                    disk[answer_genre] = genre_singer[answer_genre]
                    while True:
                        answer_singer = input("Введите исполнителя\nЕсли хотите закончить то введите n\n ")
                        print(disk_singer)
                        
                        if answer_singer.lower() != "n":
                            if answer_singer in singer_traсk:
                                disk_singer[answer_singer] = singer_traсk[answer_singer]
                                while True:
                                    answer_track = input("Введите название композиции\nЕсли хотите закончить то введите n\n ")
                                    print(disk_track)
                                    if answer_track.lower() != "n":
                                        if answer_track in track_timing:
                                            if answer_track not in disk_track:
                                                disk_track[answer_track] = track_timing[answer_track]
                                            elif  answer_track in disk_track:
                                                print("Эта композиция уже есть, добавьте другую!")
                                        else:
                                            print("Такой композиции к сожалению нет!")
                                            continue
                                    elif answer_track.lower() == "n":
                                        if len(disk_track) > 0:
                                            print("Перечень сохраненных композиций:")
                                            for key in disk_track:
                                                print(disk_track)
                                        if len(disk_track) != 0:
                                            sum_disk_track = sum(disk_track.values())
                                            print('длительность всех песен ''{}' +str(sum_disk_track))
                                                        
                                            print('Сортировка музыки на основе принадлежности к жанру:')
                                            for value in sorted(disk.values()):
                                                for key in disk.keys():
                                                    if disk[key] == value:
                                                        print (key,'-' ,disk[key])
                                                      
                                    break
                                break
                            else:
                                print("Такого исполнителя к сожалению нет!")
                                continue
                        elif answer_singer.lower() == "n":
                            print('Побробуйте еще раз!')
                            break
                      
                elif len(disk) == 0:
                    print('Вы не записали диск! В следующий раз обязательно получится!')
                    break
                                
                else:
                    print("Такого жанра нет в иерархии!")
                    break
            elif answer_genre.lower() == "n":
                if len(disk_track) > 0:
                    print("Перечень сохраненных композиций:")
                    for key in disk_track:
                        print(key)
                if len(disk_track) != 0:
                    sum_disk_track = sum(disk_track.values())
                    print('длительность всех песен ''{}' +str(sum_disk_track))
                                                        
                    print('Сортировка музыки на основе принадлежности к жанру:')
                    for value in sorted(disk.values()):
                        for key in disk.keys():
                            if disk[key] == value:
                                print (key,'-' ,disk[key])                        
                    break
                elif len(disk_track) == 0:
                    print('В следующий раз обязательно получится!')
                    break
        break
            
    else:
        print("До встречи!")
        break
if len(disk_track) != 0:
    while True:
        my_answer = input("Хочешь найти композицию, соответствующую заданному диапазону продолжительности(y/n)?")
        if my_answer.lower() == "y":
            print("Композиции из какого диапазона вам интересны")
            length_1 = input("Нижний диапазон")
            length_1 = input("Верхний диапазон")
            count = 0
            for value_length in disk_track.values():
                if int(length_1) <= value_length >= int(length_2):
                    for key in disk:
                        if disk_track[key] == value_length:
                            print("Композиция", key, ", вошедшая", disk_track[key], "длительностью, "
                                  "лежит в вашем диапазоне от", length_1, "до", length_2)
                            count += 1
            if count == 0:
                print("Композиция "
                      "в вашем диапазоне от", length_1, "до", length_2,
                      "отсутствует на вашем диске!")
        else:
            print("До встречи!")
            break   




