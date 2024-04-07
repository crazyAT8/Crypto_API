import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class CoinMarketCapViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('CoinMarketCap Data Viewer')
        self.setGeometry(100, 100, 600, 400)
        
        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Text Edit
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        layout.addWidget(self.textEdit)
        
        # Button
        self.button = QPushButton('Fetch Data')
        self.button.clicked.connect(self.fetchData)
        layout.addWidget(self.button)
    
    def fetchData(self):
        url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
          'start': '1',
          'limit': '5000',
          'convert': 'USD'
        }
        headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': 'your_api_key_here',  # Replace with your actual API key
        }
        
        session = Session()
        session.headers.update(headers)
        
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            self.textEdit.setText(json.dumps(data, indent=4))
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            self.textEdit.setText(str(e))

def main():
    app = QApplication(sys.argv)
    viewer = CoinMarketCapViewer()
    viewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
