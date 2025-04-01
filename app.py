# test

# 問診AI

import streamlit as st
import openai
import json
import numpy as np
import pandas as pd
import time
import requests
import sys
from PIL import Image
import os

# セッション状態の初期化
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# API keys
openai.api_key = "openai"
DEEPSEEK_API_KEY = "deepseek"  # Replace with your DeepSeek API key

# 医者のアイコンを表示（画像が存在する場合のみ表示）
icon_path = "images/doctor_icon.png"
if os.path.exists(icon_path):
    doctor_icon = Image.open(icon_path)
    st.image(doctor_icon, width=100)  # 幅を100ピクセルに設定

# タイトルを追加
st.title("こんにちは")

# サイドバーに赤い終了ボタンを追加
st.sidebar.markdown(
    """
    <style>
    .stButton button {
        background-color: #ff0000;
        color: white;
    }
    .stButton button:hover {
        background-color: #cc0000;
        color: white;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

if st.sidebar.button("アプリを終了"):
    st.sidebar.success("アプリケーションを終了します")
    time.sleep(1)  # メッセージを表示するための短い待機
    sys.exit()

###医学知識###
