import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)
# app.secret_key = os.environ.get('SECRET_KEY').encode()


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return facts[0].getText()
    
def get_link(input):
    
    params  = { 'input_text': input}
    
    link_info = requests.post("http://hidden-journey-62459.herokuapp.com/piglatinize/", data = params , allow_redirects=False)

    result = link_info.headers['Location']
    hyperlink_format = '<a href="{link}">{text}</a>'

    return hyperlink_format.format(link= result, text=result) 

@app.route('/')
def home():
    input = get_fact()
    link = get_link(input)
    return link
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

