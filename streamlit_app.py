import streamlit as st

# アプリのタイトル
st.title("Streamlit ボタンのデモ")

# 4つのボタンを2つずつ縦並びで表示
col1, col2 = st.columns(2)

import tkinter as tk
import webbrowser

def open_page():
    webbrowser.open("https://suikyou-hzyvkrtvfpqe4dfufv9xym.streamlit.app/page1", new=0)

root = tk.Tk()
button = tk.Button(root, text="ページ1", command=open_page)
button.pack()
root.mainloop()


with col1:
    if st.button("ボタン1", key="btn1"):
        st.success("ボタン1がクリックされました！")
    
    if st.button("ボタン2", key="btn2"):
        st.info("ボタン2がクリックされました！")

with col2:
    if st.button("ボタン3", key="btn3"):
        st.warning("ボタン3がクリックされました！")
    
    if st.button("ボタン4", key="btn4"):
        st.error("ボタン4がクリックされました！")