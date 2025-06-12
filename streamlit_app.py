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

# 方法2: st.buttonのCSSセレクタをカスタマイズ
st.header("方法2: 標準ボタンのCSSカスタマイズ")

st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: #ffd93d;
        color: black;
        width: 250px;
        height: 60px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 20px;
        border: 3px solid #ffb700;
    }
    
    div.stButton > button:hover {
        background-color: #ffb700;
        border-color: #ff8f00;
        transform: scale(1.05);
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

if st.button("カスタマイズされた標準ボタン"):
    st.success("ボタンがクリックされました！")

# 方法3: st.columnsで幅を調整
st.header("方法3: カラムレイアウトで間接的にサイズ調整")

col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 3, 1])

with col2:
    if st.button("狭いボタン", key="narrow"):
        st.info("狭いボタンがクリックされました")

with col4:
    if st.button("広いボタン", key="wide"):
        st.info("広いボタンがクリックされました")

# 方法4: 複数の異なるサイズのボタン例
st.header("方法4: 様々なサイズの実用例")

# 異なるサイズのボタンを定義
st.markdown("""
<style>
    .action-button {
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        font-weight: bold;
        margin: 5px;
        transition: all 0.3s ease;
    }
    
    .btn-small { width: 80px; height: 35px; font-size: 12px; }
    .btn-medium { width: 150px; height: 45px; font-size: 14px; }
    .btn-large { width: 220px; height: 55px; font-size: 16px; }
    .btn-xl { width: 300px; height: 70px; font-size: 20px; }
    
    .action-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# 4つの異なるサイズのボタン
cols = st.columns(4)
button_sizes = [
    ("Small", "btn-small"),
    ("Medium", "btn-medium"), 
    ("Large", "btn-large"),
    ("XL", "btn-xl")
]

for i, (text, class_name) in enumerate(button_sizes):
    with cols[i]:
        st.markdown(f'<button class="action-button {class_name}">{text}</button>', 
                   unsafe_allow_html=True)

# 実用的なTips
st.header("💡 実用的なTips")

st.markdown("""
**ボタンサイズ調整のポイント:**

1. **CSS優先度**: `!important` を使用して確実にスタイルを適用
2. **レスポンシブ対応**: `max-width: 100%` でモバイル対応
3. **ホバー効果**: ユーザビリティ向上のためのインタラクション
4. **統一性**: アプリ全体で一貫したデザイン

**推奨サイズ:**
- 小: 80-120px × 30-40px
- 中: 150-200px × 45-55px  
- 大: 250-350px × 60-80px
""")

# 注意事項
st.warning("""
⚠️ **注意**: HTMLボタンはクリックイベントを直接処理できません。
実際のクリック処理が必要な場合は、JavaScriptとの組み合わせか、
標準の `st.button()` にCSSを適用する方法を使用してください。
""")