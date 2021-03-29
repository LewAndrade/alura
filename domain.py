# oioioi feeeee
class Media:
    def __init__(self, name, year):
        self._name = name
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1


class Movie(Media):

    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length


class Series(Media):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


avengers = Movie('avengers - inifinity war', 2018, 160)

wandavision = Series('wanda vision', 2021, 1)

avengers.give_like()
avengers.give_like()
avengers.give_like()
wandavision.give_like()

print(f'name: {avengers.name}\n'
      f'year: {avengers.year}\n'
      f'length: {avengers.length}\n'
      f'likes: {avengers.likes}')

print("-" * 30)

print(f'Name: {wandavision.name}\n'
      f'Year: {wandavision.year}\n'
      f'Seasons: {wandavision.seasons}\n'
      f'Like: {wandavision.likes}')
