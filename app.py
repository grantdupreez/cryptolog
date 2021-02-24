from bs4 import BeautifulSoup 
import requests 
import time
import streamlit as st
from money import Money
import re

st.title("Crypto Value Report")

select_currency = st.selectbox('Currency?', ('bitcoin','ethereum','cardano', 'ravencoin','the graph', 'nervos','1inch'))
select_holding = st.number_input('Holding?')

def get_crypto_price(coin):
    url = "https://www.google.com/search?q="+coin+"+price"    
    HTML = requests.get(url) 
    soup = BeautifulSoup(HTML.text, 'html.parser') 
  
    #Find the current price 
    #text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    return text

if st.button('Calculate'):
    crypto = select_currency 
    price = get_crypto_price(crypto)
#    holding_price = price.split(' ')[0]
#    holding_price = holding_price.replace((",", "")
    holding_price = re.sub("[^\d\.]", "", price)
    holding_val = holding_price * select_holding
    st.write(crypto+' price: ',price)
    st.write(value+' price: ',holding_val)
    
