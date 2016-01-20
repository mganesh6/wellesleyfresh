#coding: utf-8
from flask import Flask
app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
from datetime import date



@app.route("/<dininghall>")
def get_menu(dininghall):
	dd = date.today().day
	if dd < 10:
		dd = '0' + str(dd)
	else:
		dd = str(dd)

	mm = date.today().month
	if mm < 10:
		mm = '0' + str(mm)
	else:
		mm = str(mm)

	return menu_of_the_day(dininghall, mm, dd)


#halls = ['pomeroy','bplc','tower','bates','stonedavis']

def menu_of_the_day(hall, mm, dd):
	url = 'http://www.wellesleyfresh.com/menus/'+hall+'/menu_'+mm+dd+'.htm'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	string = soup.body.get_text(' | ')
	string = ' '.join(string.split())
	lines = string.split('| |')

	text = ''
	for line in lines:
		line = line.replace('|', '').replace(u'\x96', '-')
		line = ' '.join(line.split())
		line = line.replace(' -', '-')
		if line:
			#test.append('...' + line + '\n')
			if line.startswith('-') and line.endswith('-'):
				text = text + '\n\n' + line + '\n'
			else:
				text = text + line + '\n'

		
	return text
	#food = tree.xpath('//span[@style=\'font-family:"Trebuchet MS","sans-serif"\']/text()')
	#print food
	

  



#menu_of_the_day('pomeroy', mm, dd)


if __name__ == "__main__":
    app.run(host = '52.89.180.105', port = 80)
