import random


class Talking:
    def __init__(self):
        self.themes = ["Семья", "Родной город", "Будущее"]
        self.theme_now = "Нету темы для разговора"

    def add_talk_theme(self, additional_theme):
        self.themes.append(additional_theme)
        print("Добавил тему для разговора: " + additional_theme)

    def take_theme(self):
        self.theme_now = self.themes[random.randint(0, len(self.themes) - 1)]
        print("Выбрал тему для разговора: " + self.theme_now)

    def mix_themes(self):
        random.shuffle(self.themes)
        print("Перемешал темы для разговора:")
        print(self.themes)

    def next_theme(self):
        try:
            self.themes.remove(self.theme_now)
            self.theme_now = self.themes[random.randint(0, len(self.themes) - 1)]
            print("Тема для разговора: " + self.theme_now)
        except ValueError:
            print("Чтобы поменять тему для разговора, её сначала нужно выбрать!")

    def replace_theme(self):
        try:
            self.themes.remove(self.theme_now)
            self.theme_now = self.themes[random.randint(0, len(self.themes) - 1)]
            print("Поменял тему разговора: " + self.theme_now)
        except ValueError:
            print("Чтобы заменить тему для разговора, её сначала нужно выбрать!")

    def __str__(self):
        if self.theme_now in self.themes:
            return f"Тема разговора: {self.theme_now}"
        else:
            return f"Нету темы для разговора"


class Discussion(Talking):
    def __init__(self):
        self.people = []
        super().__init__()

    def add_people_talk(self, name):
        self.people.append(name)
        print("Добавил человека в разговор: " + name)

    def remove_people_talk(self, name):
        try:
            self.people.remove(name)
            print("Убрал человека из разговора: " + name)
        except ValueError:
            print("Такого человека в разговоре нету")

    def __str__(self):
        if len(self.people) >= 2:
            return f"Сейчас в беседе учавствуют: {self.people}, Тема разговора: {self.theme_now}"
        elif len(self.people) == 1:
            return f"Сейчас {self.people[0]} один/одна, добавьте ему/ей собеседника в беседу!"
        else:
            return f"Сейчас в беседе никто не участвует"

if __name__ == "__main__":
    parent = Discussion()
    parent.add_talk_theme("Школа")
    parent.add_talk_theme("Отношения")
    print(parent)
    parent.add_people_talk("Кирилл")
    print(parent)
    parent.add_people_talk("Дарья")
    print(parent)
    parent.take_theme()
    print(parent.themes)
    parent.next_theme()
    parent.add_people_talk("Илья")
    print(parent)