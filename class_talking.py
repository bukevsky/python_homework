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
            return f"Тема сейчас: {self.theme_now}"
        else:
            return f"Нету темы для разговора"


if __name__ == "__main__":
    Talk1 = Talking()
    # Talk1.add_talk_theme('School')
    # Talk1.add_talk_theme('Дом')
    # print(Talk1)
    # Talk1.mix_themes()
    # Talk1.mix_themes()
    # print(Talk1)
    # Talk1.take_theme()
    # print(Talk1)
    # Talk1.next_theme()
    # Talk1.replace_theme()
    # print(Talk1)
    # print(Talk1)
    # # Talk1.next_theme()
    # # print(Talk1.themes)
    # Talk1.replace_theme()
    # print(Talk1.themes)
    # print(Talk1)
    # print(Talk1)
    # print(Talk1.themes)
    # Talk1.take_theme()
    # print(Talk1)
    # Talk1.mix_themes()
    # Talk1.mix_themes()
    # print(Talk1)
    # Talk1.next_theme()
    # print(Talk1)
    # Talk1.take_theme()
    # print(Talk1)


    