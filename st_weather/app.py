import streamlit as st
import requests
from PIL import Image

DAY_NAME = ['今日','明日','明後日']

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json"
data = requests.get(url).json()

st.markdown("# 天気予報チャンネル")

city = [d['name'] for d in data]

city_name = st.selectbox('場所', city)

image_sun = Image.open('sun.png')
image_rain = Image.open('rain.png')


for d in data:
    if city_name == d["name"]:
        w_l = d["srf"]["timeSeries"][0]["areas"]["weathers"]
        for day,w in zip(DAY_NAME, w_l):
            st.write(day)
            word = w.split()
            if word[0] == "晴れ":
                st.image(image_sun, caption=word[0])
            if word[0] == "雨":
                st.image(image_rain, caption=word[0])
            st.write(w)

