import os
import sys
import difflib
import MangaList
from MangaList import Manga

def MangaSearch():

    manga_Search = input()
    manga_list = MangaList.mangaList

    matching_Manga = []

    for obj in manga_list:
        sim = difflib.SequenceMatcher(None, obj.name, manga_Search)
        same = sim.ratio()
        if  same >= 0.5:
            matching_Manga.append(obj)
            i += 1

    for obj in matching_Manga:
        if not matching_Manga:
            print("I guess it's not in our library. You can add it on Github if you know the necessary Manga")
        else:
            print(obj.name, obj.link, obj.desc, obj.author, obj.release)
            print("if this isn't what you're looking for try to be more specific in the name. Sincerely No_One")