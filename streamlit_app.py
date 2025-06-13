import streamlit as st

# ページの設定
st.set_page_config(
    page_title="カスタムボタンナビゲーション",
    page_icon="🚀",
    layout="wide"
)

# セッション状態の初期化
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'ホーム'

# カスタムCSS
st.markdown("""
<style>
/* ボタンのベーススタイル */
.custom-button {
    display: inline-block;
    padding: 15px 30px;
    margin: 10px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-decoration: none;
    border-radius: 12px;
    font-weight: bold;
    font-size: 16px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
    cursor: pointer;
    border: none;
    min-width: 150px;
}

/* ホバー効果 */
.custom-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
}

/* アクティブ効果 */
.custom-button:active {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
}

/* 各ボタンの個別カラー */
.button-home {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.button-about {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.button-services {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.button-contact {
    background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
}

/* サイズ変更用のクラス */
.button-small {
    padding: 8px 16px;
    font-size: 12px;
    min-width: 100px;
}

.button-medium {
    padding: 12px 24px;
    font-size: 14px;
    min-width: 120px;
}

.button-large {
    padding: 20px 40px;
    font-size: 18px;
    min-width: 180px;
}

.button-extra-large {
    padding: 25px 50px;
    font-size: 20px;
    min-width: 220px;
}

/* ボタンコンテナ */
.button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 15px;
    margin: 30px 0;
}

/* レスポンシブデザイン */
@media (max-width: 768px) {
    .button-container {
        flex-direction: column;
    }
    
    .custom-button {
        width: 80%;
        max-width: 300px;
    }
}

/* ページコンテンツのスタイル */
.page-content {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 30px;
    border-radius: 15px;
    margin: 20px 0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.page-title {
    color: #333;
    font-size: 2.5em;
    text-align: center;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

# JavaScript for button clicks
st.markdown("""
<script>
function setPage(page) {
    // Streamlit の session state を更新するためのハック
    window.parent.postMessage({
        type: 'streamlit:setComponentValue',
        value: page
    }, '*');
}
</script>
""", unsafe_allow_html=True)

def create_navigation_buttons(button_size="medium"):
    """ナビゲーションボタンを作成する関数"""
    size_class = f"button-{button_size}"
    
    button_html = f"""
    <div class="button-container">
        <button class="custom-button button-home {size_class}" onclick="window.location.reload(); window.sessionStorage.setItem('page', 'ホーム');">
            🏠 ホーム
        </button>
        <button class="custom-button button-about {size_class}" onclick="window.location.reload(); window.sessionStorage.setItem('page', 'アバウト');">
            👤 アバウト
        </button>
        <button class="custom-button button-services {size_class}" onclick="window.location.reload(); window.sessionStorage.setItem('page', 'サービス');">
            🛠️ サービス
        </button>
        <button class="custom-button button-contact {size_class}" onclick="window.location.reload(); window.sessionStorage.setItem('page', 'お問い合わせ');">
            📧 お問い合わせ
        </button>
    </div>
    
    <script>
    // ページロード時にsessionStorageから状態を復元
    window.onload = function() {
        const savedPage = window.sessionStorage.getItem('page');
        if (savedPage) {
            // Streamlit のコンポーネントに値を送信
            const event = new CustomEvent('streamlit:componentValue', {
                detail: { value: savedPage }
            });
            window.dispatchEvent(event);
        }
    }
    </script>
    """
    
    st.markdown(button_html, unsafe_allow_html=True)

def display_page_content(page_name):
    """各ページのコンテンツを表示する関数"""
    content_map = {
        'ホーム': {
            'title': '🏠 ホームページへようこそ',
            'content': '''
            ここはホームページです。このサイトでは、カスタマイズされたボタンを使って
            スムーズなナビゲーションを体験できます。
            
            **特徴:**
            - レスポンシブデザイン
            - アニメーション効果
            - カスタマイズ可能なサイズ
            '''
        },
        'アバウト': {
            'title': '👤 私たちについて',
            'content': '''
            私たちは革新的なウェブソリューションを提供する会社です。
            Streamlitを使用したインタラクティブなアプリケーションの開発に特化しています。
            
            **ミッション:**
            - ユーザーフレンドリーなインターフェース
            - 高品質なコード
            - 優れたユーザーエクスペリエンス
            '''
        },
        'サービス': {
            'title': '🛠️ サービス内容',
            'content': '''
            私たちが提供するサービスの一覧です。
            
            **提供サービス:**
            - Streamlitアプリケーション開発
            - データビジュアライゼーション
            - カスタムUI/UXデザイン
            - ウェブアプリケーション最適化
            '''
        },
        'お問い合わせ': {
            'title': '📧 お問い合わせ',
            'content': '''
            ご質問やご相談がございましたら、お気軽にお問い合わせください。
            
            **連絡先:**
            - Email: contact@example.com
            - Phone: 03-1234-5678
            - Address: 東京都渋谷区...
            
            お客様のご要望に合わせたソリューションを提供いたします。
            '''
        }
    }
    
    page_info = content_map.get(page_name, content_map['ホーム'])
    
    # テキストのMarkdownをHTMLに変換
    import re
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', page_info['content'])
    html_content = html_content.replace('\n', '<br>')
    
    st.markdown(f"""
    <div class="page-content">
        <h1 class="page-title">{page_info['title']}</h1>
        <div style="font-size: 16px; line-height: 1.6; color: #555;">
            {html_content}
        </div>
    </div>
    """, unsafe_allow_html=True)

# メイン画面
st.title("🚀 カスタムボタンナビゲーション")

# サイドバーでボタンサイズを選択
st.sidebar.header("⚙️ 設定")
button_size = st.sidebar.selectbox(
    "ボタンサイズを選択:",
    ["small", "medium", "large", "extra-large"],
    index=1
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**使い方:**
1. 上記からボタンサイズを選択
2. メインエリアのボタンをクリック
3. 対応するページに移動

**ボタンの特徴:**
- ホバー効果あり
- クリック時のアニメーション
- レスポンシブデザイン
- カスタムカラー
""")

# ページ選択用の隠しコンポーネント（JavaScriptから値を受け取る）
selected_page = st.selectbox(
    "現在のページ",
    ["ホーム", "アバウト", "サービス", "お問い合わせ"],
    key="page_selector",
    label_visibility="hidden"
)

# セッション状態を更新
if selected_page != st.session_state.current_page:
    st.session_state.current_page = selected_page

# Streamlit標準のボタンでページ切り替え（フォールバック）
st.markdown("### Streamlit標準ボタン（代替手段）")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 ホーム", key="home_btn"):
        st.session_state.current_page = "ホーム"

with col2:
    if st.button("👤 アバウト", key="about_btn"):
        st.session_state.current_page = "アバウト"

with col3:
    if st.button("🛠️ サービス", key="services_btn"):
        st.session_state.current_page = "サービス"

with col4:
    if st.button("📧 お問い合わせ", key="contact_btn"):
        st.session_state.current_page = "お問い合わせ"

st.markdown("---")

# カスタムボタンを表示
st.markdown("### カスタムHTMLボタン")
create_navigation_buttons(button_size)

st.markdown("---")

# 現在のページを表示
st.markdown(f"**現在のページ:** {st.session_state.current_page}")

# ページコンテンツを表示
display_page_content(st.session_state.current_page)