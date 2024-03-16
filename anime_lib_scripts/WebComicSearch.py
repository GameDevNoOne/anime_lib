import os
import sys
import WebComicsLinkList
from WebComicsLinkList import WebComics
import difflib

def WebComicSearch():

    webComic_search = input()
    webComic_list = WebComicsLinkList.webcomic_link_list

    matching_WebComic = []

    for obj in webComic_list:
        sim = difflib.SequenceMatcher(None, obj.name, webComic_search)
        same = sim.ratio()
        if  same >= 0.5:
            matching_WebComic.append(obj)

    for obj in matching_WebComic:
        if not matching_WebComic:
            print("I guess it's not in our library or the search wasn't specific enough")
        else:
            print(obj.name, obj.link, obj.desc, obj.author, obj.release, obj.rating)
            print("if this isn't what you're looking for try to be more specific in the name. Sincerely No_One")