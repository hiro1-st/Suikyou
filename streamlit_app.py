import streamlit as st

# アプリのタイトル
st.title("Streamlit ボタンのデモ")

# 基本的なボタン
if st.button("クリックしてください"):
    st.success("ボタンがクリックされました！")

# カスタムキーを持つボタン
if st.button("別のボタン", key="button2"):
    st.info("2つ目のボタンがクリックされました")

# 無効化されたボタン
if st.button("無効化されたボタン", disabled=True):
    st.warning("このボタンは無効化されています")

# ヘルプテキスト付きボタン
if st.button("ヘルプ付きボタン", help="このボタンをクリックすると何かが起こります"):
    st.balloons()
    st.write("🎉 おめでとうございます！")

# セッション状態を使ったカウンターボタン
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("カウンター"):
    st.session_state.count += 1

st.write(f"カウント: {st.session_state.count}")

# リセットボタン
if st.button("リセット"):
    st.session_state.count = 0
    st.rerun()

# 複数のボタンを並べて表示
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("ボタン1", key="btn1"):
        st.write("ボタン1がクリックされました")

with col2:
    if st.button("ボタン2", key="btn2"):
        st.write("ボタン2がクリックされました")

with col3:
    if st.button("ボタン3", key="btn3"):
        st.write("ボタン3がクリックされました")

# フォームの中のボタン
with st.form("my_form"):
    st.write("フォーム内のボタン")
    name = st.text_input("名前を入力してください")
    
    # フォーム送信ボタン
    submitted = st.form_submit_button("送信")
    
    if submitted:
        if name:
            st.success(f"こんにちは、{name}さん！")
        else:
            st.error("名前を入力してください")

# ダウンロードボタン
data = "これはダウンロードされるテキストファイルの内容です。"
st.download_button(
    label="テキストファイルをダウンロード",
    data=data,
    file_name="sample.txt",
    mime="text/plain"
)