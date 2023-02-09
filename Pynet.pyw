from PyQt6.QtWidgets import *
import sys
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MainWindow(QMainWindow):

    def search (self):
        self.browser.setUrl(QUrl('https://www.google.com.br'))

    def aurl (self):
        url, done1 = QInputDialog.getText(
		self, 'Input Dialog', 'Digite o URL: ')
        protocolo = "https://"
        realurl = protocolo + url

        self.browser.setUrl(QUrl(realurl))

    def go_to_home (self):
        self.browser.setUrl(QUrl('https://sites.google.com/view/home-pynet/in%C3%ADcio'))
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://sites.google.com/view/home-pynet/in%C3%ADcio"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.layout = QVBoxLayout(self)
        
        #navegation bar
        navbar =  QToolBar()
        self.addToolBar(navbar)

        #back button-action
        
        backbuttn = QAction ('<', self)
        backbuttn.triggered.connect(self.browser.back)
        navbar.addAction(backbuttn)
        
        #refresh button-action

        refreshbuttn = QAction('Recarregar', self)
        refreshbuttn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshbuttn)
        
        #home button-action

        homebuttn = QAction('Home', self)
        homebuttn.triggered.connect(self.go_to_home)
        navbar.addAction(homebuttn)

        #enter url-action

        urlbuttn = QAction('URL', self)
        urlbuttn.triggered.connect(self.aurl)
        navbar.addAction(urlbuttn)

        #search-google action
        
        searchbttn = QAction('Pesquisar', self)
        searchbttn.triggered.connect(self.search)
        navbar.addAction(searchbttn)

        
 
        


        
app = QApplication(sys.argv)
app.setWindowIcon(QIcon('./icon/app-icon.ico'));
QApplication.setApplicationName("Pynet")
window = MainWindow()
app.exec()