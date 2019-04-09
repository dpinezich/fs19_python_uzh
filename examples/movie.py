import json
import urllib.request
import urllib.parse
import datetime

API_KEY = 'f9a00520ec2beacdec7f69bf6a20d085'

request = input('Please give me a movie name: ')

url = 'http://api.themoviedb.org/3/search/movie?api_key=' + API_KEY + '&query=' + urllib.parse.quote(request, safe='')
raw_answer = urllib.request.urlopen(url)

answer = json.load(raw_answer)

results = answer['results']
index = 0
for movie in results:
    id = movie['id']
    title = movie['title']
    release_date = movie['release_date']
    original_title = movie['original_title']

    print(str(index) + ': ' + title + ' (' + original_title + ') ' + ' ' + release_date)
    index = index + 1


#####################

index = int(input('Index of the movie you like to have details to: '))

url = 'http://api.themoviedb.org/3/movie/' + str(results[index]['id']) + '?api_key=' + API_KEY

raw_details = urllib.request.urlopen(url)


details = json.load(raw_details)

print(details['overview'])