import os
import sys
import difflib
import AnimeLinklist
from AnimeLinklist import Anime

anime_search = input()
anime_list = AnimeLinklist.anime_list

matching_Anime = []

for obj in anime_list:
    i = 0
    sim = difflib.SequenceMatcher(None, obj.name, anime_search)
    same = sim.ratio()
    if  same >= 0.5:
        matching_Anime.append(obj)
        i += 1

for obj in matching_Anime:
    if not matching_Anime:
        print("I guess it's not in our library or it the search wasn't specific enough")
    else:
        print(obj.name, obj.link)
        print("if this isn't what you're looking for try to be more specific in the name. Sincerely No_One")