import streamlit as st

# アプリのタイトル
st.title("Streamlit ボタンのデモ")

# 4つのボタンを2つずつ縦並びで表示
col1, col2 = st.columns(2)

with col1:
    if st.button("ボタン1", key="btn1"):
        st.success("ボタン1がクリック！")
    
    if st.button("ボタン2", key="btn2"):
        st.info("ボタン2がクリック！")

with col2:
    if st.button("ボタン3", key="btn3"):
        st.warning("ボタン3がクリック！")
    
    if st.button("ボタン4", key="btn4"):
        st.error("ボタン4がクリック！")