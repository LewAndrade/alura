from abc import ABCMeta, abstractmethod
from collections.abc import MutableSequence
from random import choice, randint


# Extensão é você herdar uma classe inteira virando uma relação 'é um', aumentando acoplamento
class Media(metaclass=ABCMeta):
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0
        self._dislikes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    @property
    def dislikes(self):
        return self._dislikes

    def give_dislike(self):
        self._dislikes += 1

    @abstractmethod
    def __str__(self) -> str:
        return f"Name: {self._name}\n" \
               f"Year: {self.year}\n" \
               f"Likes: {self._likes}\n" \
               f"Dislikes: {self._dislikes}"


class Movie(Media):

    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    def __str__(self) -> str:
        return f"{super().__str__()}\n" \
               f"Length: {self.length}"


class Series(Media):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self) -> str:
        return f"{super().__str__()}\n" \
               f"Seasons: {self.seasons}"


class Documentary(Media):
    def __init__(self, name, year, category):
        super().__init__(name, year)
        self.category = category.title()

    def __str__(self) -> str:
        return f'{super().__str__()}\n' \
               f'category: {self.category}'


# Composição é o uso de DuckTyping pra ter uma relação 'tem um', tirando acoplamento
class Playlist(MutableSequence):
    def __init__(self, name: str, medias: [Media]):
        self._name = name.title()
        self._medias = medias

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    @property
    def list(self):
        media_list = []
        val = ""
        biggest_name = 0
        for media in self._medias:
            if len(media.name) > biggest_name:
                biggest_name = len(media.name)
            media_list.append(str(media))

        biggest_name += 6

        for item in media_list:
            val += "-" * biggest_name + "\n"
            val += item + "\n"
            val += "-" * biggest_name + "\n"
        return val

    def rate(self):
        for media in self._medias:
            for x in range(1000):
                rate = self.__ratio_seed(randint(1, 10), randint(1, 10), randint(1, 20))
                if rate == "like":
                    media.give_like()

                if rate == "dislike":
                    media.give_dislike()

    @staticmethod
    def __ratio_seed(like=1, dislike=1, none=1):
        return choice(["like"] * like + ["dislike"] * dislike + [""] * none)

    def __str__(self) -> str:
        val = f"Playlist: {self._name} \n" \
              f"Size: {len(self)}\n" \
              f"{self.list}"
        return val

    def insert(self, index: int, value) -> None:
        self._medias.insert(index, value)

    def __getitem__(self, i: int) -> Media:
        return self._medias[i]

    def __setitem__(self, i: int, o: Media) -> None:
        self._medias[i] = o

    def __delitem__(self, i: int) -> None:
        self._medias.pop(i)

    def __len__(self) -> int:
        return len(self._medias)


avengers = Movie('GUERRA DEMORADA', 2018, 160)
wandavision = Series('wanda vision', 2021, 1)
falquinho = Series('GALO E VELHA', 2021, 1)
filme_do_lol = Movie('league of lol', 2040, 340)
danca_das_cadeiras = Series('GOTY', 2011, 11)
doczin = Documentary('dococo', 1099, "sanitário")

list_of_medias = [avengers, wandavision, falquinho, filme_do_lol, danca_das_cadeiras, doczin]

playlist = Playlist("playlistzinha", list_of_medias)
playlist.rate()
print(playlist)
