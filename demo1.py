import requests
import bs4

url = 'http://sangolacollege.org/'

response = requests.get(url)
#print(response.text)  #unparsed response

soup = bs4.BeautifulSoup(response.text, 'html.parser')
#print(soup)   #parsed text content of html


for para in soup.find_all('p'):  #find() for single tag and find_all() for all tags
    #print(para)
    pass

for tag in soup.find_all('a'):
    link = tag.get('href')
    #print(type(link))
    if link == '#':
        pass
    else:
        link= 'http://sangolacollege.org/'+link #Customized the link which was not proper
    #print(link)


url2 = 'https://www.youtube.com/channel/UCRd6kZIO8EQ_D1026zLzI2Q/videos'
data = requests.get(url2)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
for tag in soup.find_all('a'):
    #print(tag,type(tag))
    link = tag.get('href')
    if link[0:3] == '/wa':
        print('https://www.youtube.com/'+link)


    
