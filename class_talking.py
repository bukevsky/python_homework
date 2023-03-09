import random


def count(func):
    counters = {}
    def wrapper(*args, **kwargs):
        counters[func] = counters.get(func, 0) + 1
        print(f'Функция {func.__name__} вызвана {counters[func]} раз')
        return func(*args, **kwargs)
    return wrapper


class Talking:
    @count
    def __init__(self):
        self.themes = ["Семья", "Дом", "ЕГЭ", "Прогулка"]
        self.theme_now = "Нету темы для разговора"

    @count
    def add_talk_theme(self, additional_theme):
        self.themes.append(additional_theme)
        print("Добавил тему для разговора: " + additional_theme)

    @count
    def take_theme(self):
        try:
            self.theme_now = self.themes[random.randint(0, len(self.themes) - 1)]
            print("Выбрал тему для разговора: " + self.theme_now)
        except ValueError:
            print("Тем для разговора нету, добавьте темы.")

    @count
    def mix_themes(self):
        random.shuffle(self.themes)
        print("Перемешал темы для разговора:")
        print(self.themes)

    @count
    def next_theme(self):
        try:
            self.themes.remove(self.theme_now)
            self.theme_now = self.themes[random.randint(0, len(self.themes) - 1)]
            print("Тема для разговора: " + self.theme_now)
        except ValueError:
            print("Темы закончились!")

    @count
    def replace_theme(self):
        try:
            self.theme_now = self.themes[random.randint(0, len(self.themes) - 1)]
            print("Поменял тему разговора: " + self.theme_now)
        except ValueError:
            print("Чтобы заменить тему для разговора, её сначала нужно выбрать!")

    @count
    def __str__(self):
        if self.theme_now in self.themes:
            return f"Тема разговора: {self.theme_now}"
        else:
            return f"Нету темы для разговора"


class Discussion(Talking):
    @count
    def __init__(self):
        self.people = []
        super().__init__()

    @count
    def add_people_talk(self, name):
        self.people.append(name)
        print("Добавил человека в разговор: " + name)

    @count
    def remove_people_talk(self, name):
        try:
            self.people.remove(name)
            print("Убрал человека из разговора: " + name)
        except ValueError:
            print("Такого человека в разговоре нету")

    @count
    def __str__(self):
        if len(self.people) >= 2:
            return f"Сейчас в беседе учавствуют: {self.people}, Тема разговора: {self.theme_now}"
        elif len(self.people) == 1:
            return f"Сейчас {self.people[0]} один/одна, добавьте ему/ей собеседника в беседу!"
        else:
            return f"Сейчас в беседе никто не участвует"

if __name__ == "__main__":
    talk1 = Talking()
    talk1.take_theme()
    talk1.replace_theme()
    print(talk1.themes)
    talk1.next_theme()
    talk1.next_theme()
    talk1.next_theme()
    talk1.next_theme()
    talk1.next_theme()
    parent = Discussion()
    parent.take_theme()
    parent.add_talk_theme("Школа")
    print(parent)
    parent.add_people_talk("Кирилл")
    print(parent)
    parent.add_people_talk("Дарья")
    print(parent.themes)
    print(parent)
    parent.next_theme()
    print(parent)