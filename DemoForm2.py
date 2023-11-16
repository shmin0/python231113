# DemoForm2.py (로직단)
# DemoForm2.ui(화면단) 

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup


form_class = uic.loadUiType('DemoForm2.ui')[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        url='http://www.daangn.com/fleamarket/'
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'html.parser')
        f=open('dangn.txt','wt',encoding='utf-8')
        posts=soup.find_all('div',attrs={'class':'card-desc'})
        
        for post in posts:
              title=post.find('h2',attrs={'class':'card-title'})
              price=post.find('div',attrs={'class':'card-price'})
              addr=post.find('div',attrs={'class':'card-region-name'})
              title=title.text.replace('\n',"")
              price = price.text.replace('\n',"")
              addr=addr.text.replace('\n',"")
              print('{0},{1},{2}'.format(title, price, addr))
              f.write(f"{title},{price},{addr}\n")
        f.close()
        self.label.setText('첫번째 버튼') 
    def secondClick(self):
        self.label.setText('두번째 버튼') 
    def thirdClick(self):
        self.label.setText('세번째 버튼') 

if __name__=='__main__':
    app =QApplication(sys.argv)
    DemoForm=DemoForm()
    DemoForm.show()
    app.exec_()
