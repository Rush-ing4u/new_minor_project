import streamlit as st
import requests
import os
from bs4 import BeautifulSoup


st.set_page_config(\
    page_title="NEW(s)",
    page_icon="📊",
    layout= "centered"
    )

def extract_news(soup):
    news= []
    elements = soup.find_all('div', class_='element')

    for title in elements:
        link= title.find('a').get('href')
        headline= title.find('h3').text
        try: img = title.find('img').get('src')
        except: img=''
        news.append({
            'headline': headline,
            'link': link,
            'img': img
        })
    return news

st.title("भारत का समय")
st.subheader("  In one click!")

col1, col2 = st.columns([1,1])
with col1:
    state = st.selectbox("Enter your State", ['andhra-pradesh','karnataka','kerala','tamil-nadu','telangana','other-states'])
    btn1 = st.button('get news by state')
with col2: 
    category = st.selectbox('Choose a category',('Politics','Technology','Business','Sports'))
    btn2 = st.button('get news by category')

if btn1:
    url = f"https://www.thehindu.com/news/national/{state}/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data = extract_news(soup)        
    for i in data:
        if i['img'] != '':
            st.image(i['img'])
        st.write(i['headline'])
        st.write(i['link'])
        st.write('---')
elif btn2:
    if category == 'Politics':
        url = "https://www.thehindu.com/elections/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        data = extract_news(soup)        
        for i in data:
            if i['img'] != '':
                st.image(i['img'])
            st.write(i['headline'])
            st.write(i['link'])
            st.write('---')
        
    elif category =='Technology':
        url = "https://www.thehindu.com/sci-tech/technology/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        data = extract_news(soup)        
        for i in data:
            if i['img'] != '':
                st.image(i['img'])
            st.write(i['headline'])
            st.write(i['link'])
            st.write('---')
    elif category =='Business':
        url = "https://www.thehindu.com/business/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        data = extract_news(soup)        
        for i in data:
            if i['img'] != '':
                st.image(i['img'])
            st.write(i['headline'])
            st.write(i['link'])
            st.write('---')
    elif category =='Sports':
        url = "https://www.thehindu.com/sport/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        data = extract_news(soup)        
        for i in data:
            if i['img'] != '':
                st.image(i['img'])
            st.write(i['headline'])
            st.write(i['link'])
            st.write('---')
    
    
    