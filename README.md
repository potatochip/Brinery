# Brinery
Brinery, like, binary, get it?

Pickle a site's pages so that you don't have to hit the server multiple times


Usage examples:
'''
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
