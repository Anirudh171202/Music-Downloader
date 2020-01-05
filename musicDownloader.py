import requests
from bs4 import BeautifulSoup
import tldextract
import os, subprocess
import tkinter

#command = 'echo 3 | sudo tee /proc/sys/vm/drop_caches'
#subprocess.check_call(shlex.split(command),stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
def downloadTheSong(wind,name,  pic):
	print(wind, name, pic)
	


	x= [i.rstrip(" ").lstrip(' ').replace(' ', '+') for i in name.split(",")]
	

	for i in range(len(x)):

		
		# r = requests.get("http://quotes.toscrape.com/page/1/")
		# linksVids= BeautifulSoup(r.content , 'html.parser')
		# a = linksVids.find("div", {"class" : "container" }).get_text()
		# print(a)

		r=  requests.get(f'https://youtube.com/results?search_query={x[i]}')
		
		linksVids= BeautifulSoup(r.content , 'html.parser')

		divs= linksVids.find_all('img', src = True)
		l = []
		link = ''
		for div in divs :
			link = div["src"]
			if tldextract.extract(link).domain == "ytimg" :
				break
		videoLink = link.split("/", 5)[-2]
		
		songToBeDownloaded = "https://www.youtube.com/watch?v=" + videoLink
		if pic:

			os.system(f"youtube-dl -x --audio-format mp3 --embed-thumbnail {songToBeDownloaded}")
		else:
			os.system(f"youtube-dl -x --audio-format mp3 {songToBeDownloaded}")
		wind.quit()
		# output=subprocess.Popen(f"youtube-dl -x --audio-format mp3 --embed-thumbnail {songToBeDownloaded}", shell=False ,stdout=subprocess.PIPE, stderr=STDOUT)


		


		