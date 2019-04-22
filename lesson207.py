from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen('http://finance.naver.com/marketindex/')
soup = BeautifulSoup(target,'html.parser')

for tag in soup.select('.data_lst li'):
	print(tag.select_one('.blind').string.split(' ')[-1],':',tag.select_one('.value').string)