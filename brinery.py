'''
Brinery, like, binary, get it?

Pickle a site's pages so that you don't have to hit the server multiple times


Usage examples:
# pickle 10 pages with a maximum sleep time of 2 seconds from a list of urls on boxofficemojo.com
list_of_links = [item['boxofficemojo url'] for item in read_main_dict().values()]
print("\nSour pickle jar: " + str(brine_time(list_of_links, maxsleep=2 cap=10)))

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

def debrine(url, filename):
    '''
    returns a single urlopen page object given a filename and a url
    '''
    pickledict = grab_pickle(filename)
    return pickledict[url]

def single_pickle(filename, url=None):
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

def brine_time(linklist, filename, maxsleep=None, cap=None):
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
            print("Sour Pickle! Tastes like a " + str(e))
            sour_pickle_jar.append(url)
            #temp_dict.update({url: str(e)}) uncomment this if you want pages with download errors included in the pickle
    dump_pickle(temp_dict, filename)
    if sour_pickle_jar:
        with open("sour_pickle_jar.txt", "wb") as f:
            for item in sour_pickle_jar:
                f.write(item)
                f.write("\n")
    return sour_pickle_jar

def refine_brine(linklist, filename, maxsleep=2, cap=None):
    '''
    when you get blocked, try-try again. but slower this time. builds on previously succesfully pickled data
    '''
    already_pickled_pages = grab_pickle(filename)
    for url in linklist:
        if url not in already_pickled_pages:
            try:
                page = urllib2.urlopen(url).read()
                already_pickled_pages[url] = page
                print("{0} is cool as a cucumber!".format(url))
            except:
                print("{0} is still sour!".format(url))
    dump_pickle(already_pickled_pages, filename)