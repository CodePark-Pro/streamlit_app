# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as path_effects

# sidemenu
#st.sidebar.markdown(
st.markdown(
   "# タイトル画像作成ツール"
)
in_text = st.text_input('文字を入力',max_chars=100)
word_size = st.slider('大きさ', min_value=50, max_value=80)
line_w = st.slider('ふちの厚さ', min_value=1, max_value=10)
in_color = st.color_picker('ふち中の色')
out_color = st.color_picker('ふち外の色')

#フォント一覧取得
fonts = fm.findSystemFonts()
print(fonts)
names = [fm.FontProperties(fname=fname).get_name() for fname in fonts]
#names = sorted(names)

#print(names)
# selectbox
select_font_name = st.selectbox(
    'フォント:',
    names
)

fig = plt.figure(figsize=(7, 1))
fig.patch.set_alpha(0.0)
text = fig.text(0.5, 0.5, (in_text), color=(in_color),
                         ha='center', va='center', size=(word_size) ,fontname=select_font_name)
text.set_path_effects([path_effects.Stroke(linewidth=(line_w), foreground=(out_color)),
                      path_effects.Normal()])
st.write("テキスト出力")
st.pyplot(fig)
