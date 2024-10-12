#Главный класс моего онлайн кинотеатра
from code import InteractiveConsole

class List:
    # Конструктор
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    # Запись
    def to_dict(self):
        return {
            "title": self.title,
            "rating": self.rating
        }
#Далее классы наследники
class action(List):
    def __init__(self, title, rating, duration):
        super().__init__(title, rating)
        self.duration = duration

    def to_dict(self):
        action_dict = super().to_dict()
        action_dict.update({
            "duration": self.duration
        })
        return action_dict


class detective(List):
    def __init__(self, title, rating, duration):
        super().__init__(title, rating)
        self.duration = duration


    def to_dict(self):
        Detective_dict = super().to_dict()
        Detective_dict.update({
            "duration": self.duration,
        })
        return Detective_dict

class drama(List):
    def __init__(self, title, rating, duration):
        super().__init__(title, rating)
        self.duration = duration

    def to_dict(self):
        Drama_dict = super().to_dict()
        Drama_dict.update({
            "duration": self.duration
        })
        return Drama_dict



class military(List):
    def __init__(self, title, rating, duration):
        super().__init__(title, rating)
        self.duration = duration


    def to_dict(self):
        Military_dict = super().to_dict()
        Military_dict.update({
            "duration": self.duration,
        })
        return Military_dict

class heroes(List):
    def __init__(self, title, rating, duration):
        super().__init__(title, rating)
        self.duration = duration

    def to_dict(self):
        Heroes_dict = super().to_dict()
        Heroes_dict.update({
            "duration": self.duration
        })
        return Heroes_dict



class animation(List):
    def __init__(self, title, rating, duration):
        super().__init__(title, rating)
        self.duration = duration


    def to_dict(self):
        Animation_dict = super().to_dict()
        Animation_dict.update({
            "duration": self.duration,
        })
        return Animation_dict

class anime(List):
    def __init__(self, title, rating, duration):
        super().__init__(title, rating)
        self.duration = duration

    def to_dict(self):
        Anime_dict = super().to_dict()
        Anime_dict.update({
            "duration": self.duration
        })
        return Anime_dict


class interactive(List):
    def __init__(self, title, rating, director, programmer):
        super().__init__(title, rating)
        self.director = director
        self.programmer = programmer

    def to_dict(self):
        Interactive_dict = super().to_dict()
        Interactive_dict.update({
            "director": self.director,
            "programmer": self.programmer
        })
        return Interactive_dict