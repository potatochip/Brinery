'''
Brinery, like, binary, get it?

Pickle a site's pages so that you don't have to hit the server multiple times


Usage examples:
# pickle 10 pages from a list of urls on boxofficemojo.com
list_of_links = [item['boxofficemojo url'] for item in read_main_dict().values()]
print("\nSour pickle jar: " + str(brine_time(list_of_links, cap=10)))

# debrine a single page
depickled_page = debrine(url)

# debrine all the pages
pickled = grab_pickle()
for item in pickled:
    depickled_page = pickled[url]
'''

import pickle
import urllib2
from random import randint
from time import sleep

def dump_pickle(x, filename):
    with open(filename, "wb") as f:
        pickle.dump(x, f)

def grab_pickle(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

def debrine(url, filename="page_data.pkl"):
    '''
    returns a single urlopen page object given a filename and a url
    '''
    pickledict = grab_pickle(filename)
    return pickledict[url]

def single_pickle(url=None, filename="page_data.pkl"):
    '''
    add a single pickle to the brined mass to try and repair sour pickles
    '''
    if not url: url = input("sour url (in quotes): ")
    temp_dict = grab_pickle(filename)
    try:
        page = urllib2.urlopen(url).read()
        temp_dict[url] = page
        dump_pickle(temp_dict, filename)
        print("Cool as a cucumber!")
    except:
        print("Still sour!")
        #except not working for 'http://www.boxofficemojo.com/movies/?id=elizabeth\xa0.htm'

def brine_time(linklist, filename="page_data.pkl", maxsleep=None, cap=None):
    '''
    pickle ALL THE PAGES. set a maximum amount of seconds to sleep if the site you're pickeling is particularly sour.
    returns a list of sour pickle pages that did not get downloaded. cap to limit the amount of pages pickled.
    saves a dictionary of urlopen objects with the urls as the keys
    '''
    temp_dict = {}
    sour_pickle_jar = []
    for index, url in enumerate(linklist):
        if index == cap: break
        print("Brining "+url)
        try:
            page = urllib2.urlopen(url).read()
            if maxsleep: sleep(randint(1, maxsleep))
            temp_dict.update({url: page})
        except Exception as e:
            print("Sour Pickle! Tastes like a" + str(e))
            sour_pickle_jar.append(url)
            temp_dict.update({url: e}) # comment this out if you don't want pages with download errors included in the dictionary at all
    dump_pickle(temp_dict, filename)
    if sour_pickle_jar:
        with open("sour_pickle_jar.txt", "wb") as f:
            for item in sour_pickle_jar:
                f.write(item)
                f.write("\n")
    return sour_pickle_jar