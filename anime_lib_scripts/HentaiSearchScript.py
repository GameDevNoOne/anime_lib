import os
import sys
import difflib
import HentaiLinkList
from HentaiLinkList import Hentai

def HentaiSearch():

    hentai_search = input
    hentai_list = HentaiLinkList.Hentai_list

    matching_Hentai = []

    for obj in hentai_list:
        sim = difflib.SequenceMatcher(None, obj.name, hentai_search)
        same = sim.ratio()
        if  same >= 0.5:
            matching_Hentai.append(obj)

    for obj in matching_Hentai:
        if not matching_Hentai:
            print("I guess it's not in our library or the search wasn't specific enough")
        else:
            print(obj.name, obj.link, obj.desc, obj.sauce, obj.release, obj.rating)
            print("if this isn't what you're looking for either accept it or try to be more specific in the name. Sincerely No_One")