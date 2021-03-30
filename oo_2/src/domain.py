from random import choice


class Media:
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


class Playlist:
    def __init__(self, name: str, medias: list):
        self._name = name.title()
        self._medias = medias

    def __getitem__(self, item):
        return self._medias[item]

    def __len__(self):
        return len(self._medias)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    @property
    def list(self):
        return self._medias

    @property
    def length(self):
        return len(self._medias)


avengers = Movie('avengers - infinity war', 2018, 160)
wandavision = Series('wanda vision', 2021, 1)
falquinho = Series('falcão e o soldado invernal', 2021, 1)
filme_do_lol = Movie('league of lol', 2040, 340)
danca_das_cadeiras = Series('brincadeira dos popo', 2011, 11)

media_list = [avengers, wandavision, falquinho, filme_do_lol, danca_das_cadeiras]


def choose():
    return choice(["like"] * 10 + ["dislike"] * 1 + [""] * 15)


for media in media_list:
    for x in range(1000):
        if choose() == "like":
            media.give_like()
        if choose() == "dislike":
            media.give_dislike()

playlist = Playlist("playlistzinha", [avengers, wandavision, falquinho, filme_do_lol, danca_das_cadeiras])

print(playlist.name)
for media in playlist:
    print("-" * 33)
    print(media)

print("-" * 33)
print(f"The Playlist Size is: {len(playlist)}")
