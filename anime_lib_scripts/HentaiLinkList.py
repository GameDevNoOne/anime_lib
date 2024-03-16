import os

class Hentai():

    def __init__(self, name, link, desc, number, date_Of_Release, rating):
        self.name = name
        self.link = link
        self.desc = desc
        self.sauce = number
        self.release = date_Of_Release
        self.rating = rating

    def __repr__(self):
        return self.name

Hentai_list = []