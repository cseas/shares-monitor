# Web crawler to extract target shares information of all the companies from a seed webpage
# This web crawler follows depth first search for finding links.
# Created by Abhijeet Singh. 15-June-2018.
# Testcase: 'https://www.moneyam.com/share-list_T.html'

maxPages = 100 # Maximum number of pages that the crawler should crawl
maxDepth = 10 # Max depth that the crawler should search for a particular link
seed = 'https://www.moneyam.com/share-list_T.html'

# get source text url as return value
def get_page(url): 
	try: 
		import urllib.request
		return urllib.request.urlopen(url).read().decode("utf8")
	except: return

# return link url and get its ending position
def get_next_target(page):
	if page is None:
		return None, 0

	start_link = page.find('<a href=')

	# If link sequence is not found
	if start_link == -1:
		return None, 0

	start_quote = page.find('"', start_link)
	start_quote += 1 # Since we don't want to include the quote
	end_quote = page.find('"', start_quote)
	url = page[start_quote : end_quote]
	# [a:b] returns index a to b-1
	return url, end_quote

# return all links in a webpage as list
def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

# add disjoint elements of q to p
def union(p,q):
	for i in q:
		if i not in p:
			p.append(i)

# crawl seed page for links recursively
def crawl_web(seed, maxPages, maxDepth):
	tocrawl = [seed] # list of pages left to crawl
	crawled = [] # list of pages crawled
	nextDepth = [] # to keep track of depth
	depth = 0 # initial depth

	# we crawl till there's nothing left to crawl or till we've reached a specified depth
	while tocrawl and depth <= maxDepth:
		page = tocrawl.pop()
		# we only crawl the page if we haven't already and if we haven't reached the limit specified
		if page not in crawled and len(crawled) < maxPages:
			union(nextDepth, get_all_links(get_page(page)))
			crawled.append(page)
		# once tocrawl is empty, we transfer the elements of nextDepth to tocrawl and empty nextDepth for next iteration
		if not tocrawl:
			tocrawl, nextDepth = nextDepth, []
			depth += 1
			print("Processing depth", depth)
	
	return crawled

# Main program
print("\nReachable links:")
crawled = crawl_web(seed, maxPages, maxDepth)
for i in crawled:
	print(i)