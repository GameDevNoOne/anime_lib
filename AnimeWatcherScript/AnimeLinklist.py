import os

class Anime():

    def __init__(self, name, link):
        self.name = name
        self.link = link

    def __repr__(self):
        return self.name
        
Berserk_1997 = Anime("Berserk_1997", "https://9anime.pe/watch/berserk-1997-103?ep=3123")
Berserk_Golden_Age_Arc_1_2012 = Anime("Berserk_Golden_Age_Arc_1", "https://9anime.pe/watch/berserk-the-golden-age-arc-i-the-egg-of-the-king-857?ep=72002")


anime_list = [ Berserk_1997, 
Berserk_Golden_Age_Arc_1_2012 ]