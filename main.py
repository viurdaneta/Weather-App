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

