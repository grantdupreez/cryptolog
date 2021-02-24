#Import the libraries 
from bs4 import BeautifulSoup 
import requests 
import time
import streamlit as st

st.title("Crypto Value Report")

select_currency = st.selectbox('Currency?', ('bitcoin','BTC-GBP','BTC-USD', 'ETH-GBP','ETH-USD', 'ADA-GBP','ADA-USD'))

#Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
#Get the URL
    url = "https://www.google.com/search?q="+coin+"+price"
    
    #Make a request to the website
    HTML = requests.get(url) 
  
    #Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser') 
  
    #Find the current price 
    #text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
#Return the text 
    return text

#Create a main function to consistently show the price of the cryptocurrency
def main():
    crypto = select_currency 
    price = get_crypto_price(crypto)
    st.write(crypto+' price: ',price)

main()
