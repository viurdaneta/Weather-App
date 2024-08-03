from bs4 import BeautifulSoup
import requests

url = 'https://www.vavel.com/en/data/uefa-euro-2024/stats/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
div_content = soup.find_all('div', class_='stats')
goalScorers, topAssisters, topPassers = [],[],[]
for i, div in enumerate(div_content):
    print(f"Div {i + 1}:")
    tables = div.find_all('table')
    for table in tables:
        print(f"Table {i + 1} inside Div {i + 1}:\n")
        data = table.find_all('span')
        if i == 0:
            goalScorers = [data[i:i+4] for i in range(0,len(data), 4)]
        elif i == 1:
            topAssisters = [data[i:i+4] for i in range(0,len(data), 4)]
        elif i == 2:
            topPassers = [data[i:i+4] for i in range(0,len(data), 4)]

print(f'Top goal scorer: {goalScorers[0]}\n  '
      f'Top assister {topAssisters[0]}\n'
      f'Top passer {topPassers[0]}\n')

'''
[<span>1</span>, <span>Georges Mikautadze</span>, <span>Georgia</span>, <span>3</span>, 
<span>2</span>, <span>Cody Gakpo</span>, <span>Netherlands</span>, <span>2</span>, 
<span>3</span>, <span>Răzvan Marin</span>, <span>Romania</span>, <span>2</span>, 
<span>4</span>, <span>Niclas Füllkrug</span>, <span>Germany</span>, <span>2</span>, 
<span>5</span>, <span>Jamal Musiala</span>, <span>Germany</span>, <span>2</span>]
'''
