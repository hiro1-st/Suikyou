import streamlit as st
from streamlit.components.v1 import html

# ページ設定
st.set_page_config(
    page_title="HTMLボタンでページ遷移",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚀 HTMLマークダウンを使用したページ遷移ボタン")

# セッション状態の初期化
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# 方法1: JavaScriptを使用したStreamlit内ページ遷移
st.header("方法1: JavaScript + Streamlit内ページ遷移")

# CSSとJavaScriptを含むHTMLコンポーネント
navigation_html = """
<style>
    .nav-button {
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        margin: 8px;
        border-radius: 25px;
        cursor: pointer;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
        min-width: 150px;
    }
    
    .nav-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        background: linear-gradient(45deg, #764ba2 0%, #667eea 100%);
    }
    
    .nav-button:active {
        transform: translateY(-1px);
    }
    
    .nav-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
        margin: 20px 0;
    }
    
    .home-btn { background: linear-gradient(45deg, #FF6B6B, #FF8E53); }
    .about-btn { background: linear-gradient(45deg, #4ECDC4, #44A08D); }
    .contact-btn { background: linear-gradient(45deg, #45B7D1, #96C93D); }
    .services-btn { background: linear-gradient(45deg, #F093FB, #F5576C); }
</style>

<div class="nav-container">
    <button class="nav-button home-btn" onclick="navigateTo('home')">🏠 ホーム</button>
    <button class="nav-button about-btn" onclick="navigateTo('about')">👥 About</button>
    <button class="nav-button services-btn" onclick="navigateTo('services')">⚙️ サービス</button>
    <button class="nav-button contact-btn" onclick="navigateTo('contact')">📞 お問い合わせ</button>
</div>

<script>
    function navigateTo(page) {
        // Streamlitにメッセージを送信
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: page
        }, '*');
    }
</script>
"""

# HTMLコンポーネントを表示
selected_page = html(navigation_html, height=100)

# ページ選択の處理
if selected_page:
    st.session_state.current_page = selected_page

# 現在のページに基づいてコンテンツを表示
def display_page_content(page):
    if page == 'home':
        st.markdown("## 🏠 ホームページ")
        st.markdown("""
        **ようこそ！** 
        
        これはHTMLボタンを使用したページ遷移のデモです。
        上のボタンをクリックして他のページに移動できます。
        """)
        
    elif page == 'about':
        st.markdown("## 👥 Aboutページ")
        st.markdown("""
        **会社概要**
        
        - 設立: 2024年
        - 事業内容: Streamlitアプリケーション開発
        - 所在地: 東京都
        """)
        
    elif page == 'services':
        st.markdown("## ⚙️ サービスページ")
        st.markdown("""
        **提供サービス**
        
        1. **Webアプリケーション開発**
        2. **データ分析ダッシュボード**
        3. **機械学習モデルデプロイ**
        4. **コンサルティング**
        """)
        
    elif page == 'contact':
        st.markdown("## 📞 お問い合わせページ")
        st.markdown("""
        **連絡先情報**
        
        - Email: contact@example.com
        - Phone: 03-1234-5678
        - 営業時間: 平日 9:00-18:00
        """)

# ページコンテンツを表示
display_page_content(st.session_state.current_page)

st.divider()

# 方法2: 外部リンクへの遷移
st.header("方法2: 外部サイトへのリンクボタン")

external_links_html = """
<style>
    .external-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-decoration: none;
        display: inline-block;
        padding: 15px 30px;
        margin: 10px;
        border-radius: 30px;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        min-width: 180px;
        text-align: center;
    }
    
    .external-button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        text-decoration: none;
        color: white;
    }
    
    .github-btn {
        background: linear-gradient(135deg, #333 0%, #24292e 100%);
    }
    
    .google-btn {
        background: linear-gradient(135deg, #4285f4 0%, #34a853 50%, #fbbc05 75%, #ea4335 100%);
    }
    
    .youtube-btn {
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
    }
    
    .stackoverflow-btn {
        background: linear-gradient(135deg, #f48024 0%, #f2740d 100%);
    }
    
    .links-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        margin: 20px 0;
    }
</style>

<div class="links-container">
    <a href="https://github.com" target="_blank" class="external-button github-btn">
        🐙 GitHub
    </a>
    <a href="https://www.google.com" target="_blank" class="external-button google-btn">
        🔍 Google
    </a>
    <a href="https://www.youtube.com" target="_blank" class="external-button youtube-btn">
        📺 YouTube
    </a>
    <a href="https://stackoverflow.com" target="_blank" class="external-button stackoverflow-btn">
        💡 Stack Overflow
    </a>
</div>
"""

st.markdown(external_links_html, unsafe_allow_html=True)

st.divider()

# 方法3: 条件付きナビゲーション
st.header("方法3: 条件付きナビゲーション")

# ユーザー認証シミュレーション
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("ログインが必要です")
    
    login_html = """
    <style>
        .login-button {
            background: linear-gradient(45deg, #56ab2f 0%, #a8e6cf 100%);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .login-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        }
    </style>
    
    <button class="login-button" onclick="login()">🔐 ログイン</button>
    
    <script>
        function login() {
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                value: 'login'
            }, '*');
        }
    </script>
    """
    
    login_result = html(login_html, height=80)
    
    if login_result == 'login':
        st.session_state.logged_in = True
        st.rerun()
        
else:
    st.success("ログイン中")
    
    protected_nav_html = """
    <style>
        .protected-button {
            background: linear-gradient(45deg, #ffeaa7 0%, #fab1a0 100%);
            color: #2d3436;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .protected-button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .logout-btn {
            background: linear-gradient(45deg, #e17055 0%, #d63031 100%);
            color: white;
        }
    </style>
    
    <div style="text-align: center;">
        <button class="protected-button" onclick="navigate('dashboard')">📊 ダッシュボード</button>
        <button class="protected-button" onclick="navigate('profile')">👤 プロフィール</button>
        <button class="protected-button" onclick="navigate('settings')">⚙️ 設定</button>
        <button class="protected-button logout-btn" onclick="navigate('logout')">🚪 ログアウト</button>
    </div>
    
    <script>
        function navigate(action) {
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                value: action
            }, '*');
        }
    </script>
    """
    
    protected_result = html(protected_nav_html, height=80)
    
    if protected_result == 'logout':
        st.session_state.logged_in = False
        st.rerun()
    elif protected_result:
        st.info(f"選択されたページ: {protected_result}")

# 技術的な説明
st.divider()
st.header("🔧 技術的な詳細")

with st.expander("コードの詳細解説を見る"):
    st.markdown("""
    ### HTMLマークダウンでのページ遷移の仕組み
    
    **1. JavaScript PostMessage API**
    ```javascript
    window.parent.postMessage({
        type: 'streamlit:setComponentValue',
        value: 'page_name'
    }, '*');
    ```
    
    **2. Streamlit Components HTML**
    ```python
    from streamlit.components.v1 import html
    result = html(html_string, height=100)
    ```
    
    **3. セッション状態管理**
    ```python
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    ```
    
    **4. 条件分岐でページ表示**
    ```python
    if st.session_state.current_page == 'home':
        display_home_page()
    ```
    """)

st.markdown("---")
st.markdown("**📝 Note**: このデモは教育目的で作成されています。")