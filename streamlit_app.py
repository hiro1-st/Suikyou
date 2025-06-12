import streamlit as st

# ページ設定
st.set_page_config(page_title="カスタムボタンサイズ", layout="wide")

st.title("Streamlitでボタンサイズを変更する方法")

# 方法1: カスタムCSS + HTML
st.header("方法1: カスタムCSS + HTML")

# CSSスタイルを定義
st.markdown("""
<style>
    
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


with col3:
    st.markdown('<button class="large-button custom-button">大きいボタン</button>', unsafe_allow_html=True)

