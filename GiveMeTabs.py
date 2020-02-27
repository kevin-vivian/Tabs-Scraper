from bs4 import BeautifulSoup
import requests
import os
import re

def give_me_links(url, regex):
    res = requests.get(url)
    res.raise_for_status()

    html = res.text
    bs = BeautifulSoup(html, 'html.parser')
    possible_links = bs.find_all('a', href=True)

    # creates a list of the link extensions that correspond to their respective URLs
    link_extensions = [link['href'] for link in possible_links if regex.match(link['href'])]
    return link_extensions

#----------main()----------------------------------------------------------------------------------------

path = os.getcwd()
home_page = 'http://www.abysslord.com/megadeth/tabs/'

url_regex = re.compile(r'(\w+)\/')                                        # url extension has a literal '/' unique to album names on the website
song_regex = re.compile(r'(\d\d)\-(\w+)\.(\w+)')                          # convention for the song titles (e.g. 01-Skin_O_My_Teeth.pdf)
album_regex = re.compile(r'(\w)')                                         # album is a single string of alpha-num characters
song_dir_regex = re.compile(r'(\d\d)\-(\w)')                              # create directory named after song and remove file extension. Keep numbers \
                                                                          #    in the beginning of the string to preserve ordering

album_link_extensions = give_me_links(home_page, url_regex)
album_links = [home_page + ext for ext in album_link_extensions]          # Create a list of links to each album using the tacit convention that 
                                                                          # host uses: home_page/tabs/(album)

# We can now scrape the files off the website. Create a local directory that 
# corresponds to each album. Create a subdirectory for each song since there 
# are at most 3 file formats for every song

test_link = album_links[0]                                               # countdown to extinction
test_songs = give_me_links(test_link, song_regex)                        # songs[0] == 01-Skin_O_My_Teeth.pdf. 
                                                                         # This is a list containing every tab for the album in every file format



 res = requests.get(test_link + test_songs[i])
 song_file = open(test_songs[i],'wb')
 print('Processing {}'.format(song_file))

 for chunk in res.iter_content(100000):
     song_file.write(chunk)
 song_file.close()
 os.chdir(album_dir)
