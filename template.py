from jinja2 import Environment, FileSystemLoader, select_autoescape
import random
import os


CLASSES_BASE = {
        'Охотник': {
            'skills': ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
            'strength': random.randint(1, 3),
            'agility': 15,
            'intelligence': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'temper': random.randint(1, 3),
            'image': '../images/archer.png'
        },
        'Маг': {
            'skills': ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
            'strength': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'intelligence': 15,
            'luck': random.randint(1, 3),
            'temper': random.randint(1, 3),
            'image': '../images/wizard.png'
        },
        'Ассасин': {
            'skills': ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
            'strength': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'intelligence': random.randint(1, 3),
            'luck': 15,
            'temper': random.randint(1, 3),
            'image': '../images/assasin.png'
        },
        'Бард': {
            'skills': ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
            'strength': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'intelligence': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'temper': 15,
            'image': '../images/bard.webp'
        },
        'Воин': {
            'skills': ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
            'strength': 15,
            'agility': random.randint(1, 3),
            'intelligence': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'temper': random.randint(1, 3),
            'image': '../images/warrior.png'
        },
    }

def main():
    folder = 'characters'
    if not os.path.exists(folder):
        os.makedirs(folder)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    character_class_list = ['Охотник', 'Ассасин', 'Бард', 'Воин', 'Маг'] 
    race_list = ['Человек', 'Орк', 'Эльф', 'Дварф']
     
    quality_page = int(input('Сколько вам нужно карточек(цифрой): '))

    for page in range(quality_page):
        name_hero = input('Введите имя героя: ')

        for number, race in enumerate(race_list, 1):
            print(f'{number}. {race}')

        race_hero = int(input('Выберите расу: '))

        for number, character_class in enumerate(character_class_list, 1):
            print(f'{number}. {character_class}')

        character_class_hero = int(input('Выберите класс: '))

        hero_class = character_class_list[character_class_hero-1]

        skills = random.sample(CLASSES_BASE[hero_class]['skills'], 3)

        rendered_page = template.render(
            name=name_hero,
            race=race_list[race_hero-1],
            character_class=hero_class,
            strength=CLASSES_BASE[hero_class]['strength'],
            agility=CLASSES_BASE[hero_class]['agility'],
            intelligence=CLASSES_BASE[hero_class]['intelligence'],
            luck=CLASSES_BASE[hero_class]['luck'],
            temper=CLASSES_BASE[hero_class]['temper'],
            image=CLASSES_BASE[hero_class]['image'],
            first_skill=skills[0],
            second_skill=skills[1],
            third_skill=skills[2]
        )

        with open(os.path.join(folder, f'index{page+1}.html'), 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    main()