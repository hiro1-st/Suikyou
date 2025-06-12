import streamlit as st

# ページ設定
st.set_page_config(page_title="カスタムボタンサイズ", layout="wide")

st.title("Streamlitでボタンサイズを変更する方法")

# 方法1: カスタムCSS + HTML
st.header("方法1: カスタムCSS + HTML")

# CSSスタイルを定義
st.markdown("""
<style>
    .small-button {
        background-color: #ff6b6b;
        color: white;
        padding: 5px 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 12px;
        width: 100px;
        height: 30px;
    }
    
    .medium-button {
        background-color: #4ecdc4;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        font-size: 16px;
        width: 200px;
        height: 50px;
    }
    
    .large-button {
        background-color: #45b7d1;
        color: white;
        padding: 15px 30px;
        border: none;
        border-radius: 15px;
        cursor: pointer;
        font-size: 20px;
        width: 300px;
        height: 80px;
    }
    
    .custom-button:hover {
        opacity: 0.8;
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# HTMLボタンを作成
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<button class="small-button custom-button">小さいボタン</button>', unsafe_allow_html=True)

with col2:
    st.markdown('<button class="medium-button custom-button">中くらいボタン</button>', unsafe_allow_html=True)

with col3:
    st.markdown('<button class="large-button custom-button">大きいボタン</button>', unsafe_allow_html=True)

