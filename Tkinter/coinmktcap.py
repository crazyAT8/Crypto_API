from tkinter import Tk, Text, Button, Scrollbar, END
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def fetch_data():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'5000',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
    }
    
    session = Session()
    session.headers.update(headers)
    
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        # Clear previous data
        text_area.delete('1.0', END)
        # Pretty print the JSON data to the text area
        text_area.insert(END, json.dumps(data, indent=4))
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        text_area.delete('1.0', END)
        text_area.insert(END, str(e))

app = Tk()
app.title("CoinMarketCap Data Fetcher")

# Text area with a scrollbar
text_area = Text(app, height=25, width=100)
scroll = Scrollbar(app, command=text_area.yview)
text_area.configure(yscrollcommand=scroll.set)
text_area.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

fetch_button = Button(app, text="Fetch Data", command=fetch_data)
fetch_button.pack()

app.mainloop()
