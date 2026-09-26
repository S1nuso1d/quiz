import random


def menu1():
    print("\tДобро пожаловать в игру Викторина")
    print("1. Играть")
    print("2. Выход")


def menu2():
    print("\n1. Играть")
    print("2. Рекорды")
    print("3. Правила")
    print("4. Назад")


def playrs_name():
    username1 = input("\nВведите имя игрока 1: ")
    username2 = input("Введите имя игрока 2: ")
    return username1, username2


def record(rec1, rec2, u_n1, u_n2):
    if rec1 == 0 and rec2 == 0:
        print("\nРекордов пока нет")
    else:
        print(f"\nРекорд по очкам пользователя {u_n1}: {rec1}")
        print(f"Рекорд по очкам пользователя {u_n2}: {rec2}")


def comparison_game(rec1, rec2, u_n1, u_n2):
    if rec1 > rec2:
        print(f"Игрок {u_n1}, выиграл он набрал {rec1}:{rec2}")

    elif rec1 < rec2:
        print(f"Игрок {u_n2}, выиграл он набрал {rec2}:{rec1}")

    elif rec1 == rec2:
        print(f"Победила дружба, вы набрали одинаковое количество очков {rec1}:{rec2}")


def games(name1, name2):
    questions = [
        {"text": "Какой океан самый большой?", "options": "a.Атлантический b.Тихий c.Индийский", "answer": "b"},
        {"text": "Кто из этих животных умеет летать?", "options": "a.Пингвин b.Страус c.Летучая мышь", "answer": "c"},
        {"text": "Как называется спутник Земли?", "options": "a.Марс b.Луна c.Солнце", "answer": "b"},
        {"text": "Из чего делают гуакамоле?", "options": "a.Из авокадо b.Из банана c.Из картофеля", "answer": "a"},
        {"text": "Сколько струн у обычной гитары?", "options": "a.4 b.6 c.8", "answer": "b"},
        {"text": "Сколько игроков одной команды одновременно на поле в футболе?", "options": "a.9 b.10 c.11", "answer": "c"},
        {"text": "Какое дерево сбрасывает иголки на зиму?", "options": "a.Ель b.Сосна c.Лиственница", "answer": "c"},
        {"text": "Как зовут львёнка в мультфильме «Король Лев»?", "options": "a.Симба b.Нала c.Тимон", "answer": "a"},
        {"text": "Какой газ люди вдыхают из воздуха?", "options": "a.Углекислый газ b.Кислород c.Азот", "answer": "b"},
        {"text": "В каком городе стоит Колизей?", "options": "a.В Афинах b.В Риме c.В Париже", "answer": "b"},
        {"text": "Что из этого является антонимом слова «храбрый»?", "options": "a.Смелый b.Трусливый c.Сильный", "answer": "b"},
        {"text": "Сколько минут в трёх часах?", "options": "a.120 b.180 c.240", "answer": "b"},
    ]

    points = {name1: 0, name2: 0}
    players = [name1, name2]
    random.shuffle(players)

    print(f"Первым будет {players[0]}")
    print(f"{players[1]}, ты будешь отвечать вторым")

    for player in players:
        rec = 0
        selected = random.sample(questions, 5)

        for a in range(5):
            question = selected[a]
            print("\nВопрос", a + 1)
            print(question["text"])
            print("\nОтветы:")
            print(question["options"])
            choice_game = input("Ваш ответ: ").lower()

            if choice_game == question["answer"]:
                rec += 1

            print(rec)

        points[player] = rec

    comparison_game(points[name1], points[name2], name1, name2)
    return points[name1], points[name2]


user1_rec = 0
user2_rec = 0

us_name1 = ""
us_name2 = ""

while True:
    menu1()
    choice_menu1 = input("Ваш выбор: ")

    if choice_menu1 == "2":
        break

    if choice_menu1 == "1":

        while True:
            menu2()
            choice_menu2 = input("Ваш выбор: ")

            if choice_menu2 == "4":
                break

            if choice_menu2 == "3":
                print("В эту игра могут играть 2 пользователя. Перед вами будет 5 вопросов каждому, после игры мы подсчитаем сколько набрал каждый из участников")

            if choice_menu2 == "2":
                record(user1_rec, user2_rec, us_name1, us_name2)

            if choice_menu2 == "1":

                if us_name1 == "" and us_name2 == "":
                    us_name1, us_name2 = playrs_name()

                points1, points2 = games(us_name1, us_name2)

                if points1 > user1_rec:
                    user1_rec = points1
                if points2 > user2_rec:
                    user2_rec = points2
