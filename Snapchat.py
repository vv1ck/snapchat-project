import os
try:
	import requests
except ModuleNotFoundError:
	os.system("pip install requests")
try:
	import random
except ModuleNotFoundError:
	os.system("pip install random")
try:
	import threading,sys
except ModuleNotFoundError:
	os.system("pip install threading")
try:
	import webbrowser
except ModuleNotFoundError:
	os.system("pip install webbrowser")
try:
	from PyQt5 import QtWidgets,uic
	from PyQt5.QtWidgets import *
	from PyQt5.QtCore import *
	from PyQt5.QtGui import *
except ModuleNotFoundError:
	os.system("pip install PyQt5")
class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        global label1
        super(MainApp, self).__init__()
        uic.loadUi('snap1.ui', self)
        self.form_style()
        self.pushButton_3.clicked.connect(self.chekFIL)
        self.pushButton_5.clicked.connect(self.openEML)
        self.pushButton_2.clicked.connect(self.openEML2)
        self.pushButton.clicked.connect(self.tele)
        label1 = QLabel(self)
        label1.move(229,116)
        self.text = pyqtSignal(str)
    def form_style(self):
        self.setWindowTitle("Snapchat Email @221298")
        self.setFixedSize(532,365)
        self.setWindowIcon(QIcon("snapP.jpeg"))
    def tele(self):
        webbrowser.open("https://t.me/vv1ck")
    def liked(self,emal):
        try:
            yes = "[+] linked:  "+emal
            self.listWidget.addItem(yes)
        except RuntimeError:
            pass
    def Not_liked(self,emal):
        try:
            no = "[-] Not linked:  "+emal
            self.listWidget.addItem(no)
        except RuntimeError:
            pass
    def error_proxy(self):
        try:
            self.listWidget_2.addItem("[-] bad proxy")
        except RuntimeError:
            pass
    def snapchatCK(self):
        global file ,proxy2
        proxyy = open(proxy2, 'r').read().splitlines()
        while True:
            emal = file.readline().split('\n')[0]
            if emal == "":
                break
            else:
                pass
            proxylist = []
            for pro in proxyy:
                proxylist.append(pro)
                run = str(random.choice(proxylist))
            try:
                PROXY = {"https:": run,"http:": run}
                headers = {
                    'Host': 'accounts.snapchat.com',
                    'Cookie': 'xsrf_token=aDpeseUJS0ysikB9nhdNzA; _ga=GA1.2.113171992.1627308862; _scid=f8244bc8-117d-45aa-b1b0-f24ab31edabc; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; sc_at=v2|H4sIAAAAAAAAAE3GwRGAMAgEwIqY4cIJxG6MSBUp3m/2teq4YEOlrEuIWpIfSxbD36fB2bFBveEjTDM991H9AatYyihAAAAA; _sctr=1|1627257600000; web_client_id=e64bb4c8-1a1f-4de7-970d-d637c2e9a642',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Content-Type': 'application/json',
                    'X-Xsrf-Token': 'aDpeseUJS0ysikB9nhdNzA',
                    'Content-Length': '49',
                    'Origin': 'https://accounts.snapchat.com',
                    'Referer': 'https://accounts.snapchat.com/accounts/merlin/login',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Te': 'trailers',
                    'Connection': 'close'}
                data = {
                    "email": emal,
                    "app": "BITMOJI_APP"}
                Send = requests.post('https://accounts.snapchat.com/accounts/merlin/login', headers=headers, json=data,proxies=PROXY)
                if 'hasSnapchat' in Send.text:
                    with open('linked-snap.txt', 'a') as x:
                        x.write(emal + '\n')
                    th2 = threading.Thread(target=self.liked(emal))
                    th2.start()
                elif Send.status_code == 204:
                    th2 = threading.Thread(target=self.Not_liked(emal))
                    th2.start()
                elif Send.status_code == 429:
                    th2 = threading.Thread(target=self.error_proxy)
                    th2.start()
                else:
                    pass
            except requests.exceptions.ConnectionError:
                th2 = threading.Thread(target=self.error_proxy)
                th2.start()
            except KeyboardInterrupt:
                pass
    def TRT(self):
        theards = []
        for i in range(10):
            th1 = threading.Thread(target=self.snapchatCK)
            th1.start()
    def chekFIL2(self):
        try:
            global file,proxy2
            j = open(proxy2,"r")
            self.TRT()
        except NameError:
            QMessageBox.warning(self, "error", "Please enter the proxy file")
    def chekFIL(self):
        try:
            global file
            j = file.readline().split('\n')[0]
            self.chekFIL2()
        except NameError:
            QMessageBox.warning(self, "error", "Please enter the email file")
    def openEML2(self):
        global proxy2,file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        proxy2, _ = QFileDialog.getOpenFileName(self, "Get proxy file", "","All Files (*);;Python Files (*.py)", options=options)
        if proxy2:
            proxy = open(proxy2,"r")
    def openEML(self):
        global file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        email, _ = QFileDialog.getOpenFileName(self, "Get email file", "","All Files (*);;Python Files (*.py)", options=options)
        if email:
            file = open(email,"r")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()
