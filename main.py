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
        print(f"Рекорд по очкам пользователя {u_n1}: {rec1}")
        print(f"Рекорд по очкам пользователя {u_n2}: {rec2}")


def comparison_game(rec1, rec2, u_n1, u_n2):
    if rec1 > rec2:
        print(f"Игрок {u_n1}, выиграл он набрал {rec1}:{rec2}")

    elif rec1 < rec2:
        print(f"Игрок {u_n2}, выиграл он набрал {rec2}:{rec1}")

    elif rec1 == rec2:
        print(f"Победила дружба, вы набрали одинаковое количество очков {rec1}:{rec2}")



def games(name1, name2, user_record1, user_record2):
    questions = ("Какой океан самый большой?", "Кто из этих животных умеет летать?",
                 "Как называется спутник Земли?", "Из чего делают гуакамоле?",
                 "Сколько струн у обычной гитары?", "Сколько игроков одной команды одновременно на поле в футболе?",
                 "Какое дерево сбрасывает иголки на зиму?", "Как зовут львёнка в мультфильме «Король Лев»?",
                 "Какой газ люди вдыхают из воздуха?", "В каком городе стоит Колизей?",
                 "Что из этого является антонимом слова «храбрый»?", "Сколько минут в трёх часах?")

    answer = ("a.Атлантический b.Тихий c.Индийский", "a.Пингвин b.Страус c.Летучая мышь",
              "a.Марс b.Луна c.Солнце", "a.Из авокадо b.Из банана c.Из картофеля",
              "a.4 b.6 c.8", "a.9 b.10 c.11",
              "a.Ель b.Сосна c.Лиственница", "a.Симба b.Нала c.Тимон",
              "a.Углекислый газ b.Кислород c.Азот", "a.В Афинах b. В Риме c.В Париже",
              "a.Смелый b.Трусливый c.Сильный", "a.120 b.180 c.240")

    right_answer = ("b", "c", "b", "a", "b", "c",
                    "c", "a", "b", "b", "b", "b")

    points = {name1: user_record1, name2: user_record2}
    players = [name1, name2]
    random.shuffle(players)

    print(f"Первым будет {players[0]}")
    print(f"{players[1]}, ты будешь отвечать вторым")

    for player in players:
        rec = 0

        indices  = random.sample(range(len(questions)), 5)

        selected_questions = [questions[i] for i in indices]
        selected_answer = [answer[i] for i in indices]
        selected_right_answer = [right_answer[i] for i in indices]

        for a in range(0,5):
            print("\nВопрос", a + 1)
            print(selected_questions[a])
            print("\nОтветы:")
            print(selected_answer[a])
            choice_game = input()
            choice_game = choice_game.lower()

            if choice_game == selected_right_answer[a]:
                rec += 1

            points[player] = rec

    comparison_game(points[name1], points[name2], name1, name2)

    record(points[name1], points[name2], name1, name2)

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
                "В эту игра могут играть 2 пользователя. Перед вами будет 5 вопросов каждому, после игры мы подсчитаем сколько набрал каждый из участников"

            if choice_menu2 == "2":

                record(user1_rec, user2_rec, us_name1, us_name2)

            if choice_menu2 == "1":

                if us_name1 == "" and us_name2 == "":
                    us_name1, us_name2 = playrs_name()

                games(us_name1, us_name2, user1_rec, user2_rec)