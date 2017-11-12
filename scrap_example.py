
import bs4
import requests
import pickle
response = requests.get(r'http://www.reuters.com/resources/archive/us/20171029.html')
soup = bs4.BeautifulSoup(response.content, 'html.parser')
targets = soup.find_all('div', {'class': 'headlineMed'})

output = []
for target in targets:
    try:
        timestamp = '20171029'  # + str(target.contents[1])
    except:
        timestamp = None
    title = str(target.contents[0].contents[0].encode('ascii', errors='ignore'))
    href = str(target.contents[0].attrs['href'])
    output.append({'ts': timestamp, 'title': title, 'href': href})

with open(r'C:\1.pkl', mode='wb') as w:
    pickle.dump(output, w)

with open(r'C:\1.pkl', mode='rb') as f:
    data = pickle.load(f)

for datum in data:
    print(datum['ts'])
    print datum['title']
    print datum['href']
