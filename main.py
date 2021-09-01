
# Question-
"""
provide the url. program should featch all content of website from the provided URL.  Content will in not readable form
it might be in HTML format. 
1) we should make it in readble format. 
2) From URL we have find how many <img></img> tags used?
2) From URL we have find how many <a></a> tags used?
"""

import requests
import bs4
import shutil

from requests.api import request


url = input("Enter your URL")
response = requests.get(url)  # response in unformatted format
#print("Response",response)
#print(type(response))
#print(response.text)
filename = "temp.html"
bs = bs4.BeautifulSoup(response.content, "html.parser")
formatted_text = bs.prettify()#.encode('cp1252', errors='replace') # unformatted format changed to formatted form
print(formatted_text)

try:
    with open(filename,'w', encoding='utf-8') as f:
        print('writting data to the file')
        f.write(str(formatted_text))
except Exception as ex:
    print(ex)

img_list = bs.findAll('img')
print('img_list..,',img_list)
a_list = bs.findAll('a')
print('a list..,',a_list)
print('No of img tags in website are ',len(img_list))
print('No of a tags in website are ',len(a_list))


j = 0
for imgTag in img_list:
    try:
        print(imgTag)
        imgLink = imgTag.get('src')
        print(imgLink)
        ext = imgLink[imgLink.rindex('.'):]
        filen = str(j)+ext
        res = requests.get(imgLink, stream=True)

        with open(filen, "wb") as file:
            shutil.copyfileobj(res.raw, file)
    except Exception as ex:
        print(ex)
    j+=1














