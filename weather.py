from bs4 import BeautifulSoup
import requests

url = 'https://weather.com/weather/today/l/Orlando+FL?canonicalCityId=b1bb64752b9921f0b125e7c5f07df6c368a52eab5db82010fa6a2b3d4e15473c'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

header_div = soup.find('div', id='todayDetails')
header = header_div.find('h2').text

temp_div = soup.find('div', class_='TodayDetailsCard--feelsLikeTemp--2x1SW')
details_div = soup.find('div', class_='TodayDetailsCard--detailsContainer--2yLtL')

temp = temp_div.find('span', class_='TodayDetailsCard--feelsLikeContainer--2bePz').text
wind_speed = [str for str in details_div.find('span', {'data-testid': 'Wind'})][1].text
humidity = details_div.find('span', {'data-testid': 'PercentageValue'}).text
pressure = [str for str in details_div.find('span', {'data-testid': 'PressureValue'})][1]