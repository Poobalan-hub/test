# 問診AI

このアプリケーションは、AIを使用して患者の症状を分析し、適切な診療科を提案する問診システムです。

## 必要なパッケージのインストール

以下のコマンドを実行して、必要なパッケージをインストールしてください：

```bash
pip install streamlit
pip install openai==0.28
pip install numpy
pip install pandas
pip install requests
```

または、requirements.txtを使用して一括インストールすることもできます：

```bash
pip install -r requirements.txt
```

## 使用方法

1. アプリケーションを起動するには、以下のコマンドを実行します：

```bash
streamlit run app.py
```

2. ブラウザで自動的に開かれるStreamlitアプリケーションで、以下の手順で操作してください：
   - サイドバーからAIモデルを選択（GPT-4またはDeepSeek）
   - 選択したモデルに対応するAPIキーを入力
   - 「設定を保存して開始」ボタンをクリック
   - 症状を入力して問診を開始

## 注意事項

- APIキーは必ずご自身のものを使用してください
- このアプリケーションは医療診断の代わりにはなりません
- 緊急時は必ず救急車を呼んでください

## 概要

## 主な機能

### 1. マルチLLMプロバイダー対応
- vLLM（ローカルLLMサーバー - Qwen 2.5 72B）
- OpenAI（GPT-4 Turbo）
- Google Gemini（Gemini 2.0 Flash Lite）
- Anthropic Claude（Claude 3 Opus）
- Deepseek（Deepseek Chat）

### 2. Webインターフェース (`app.py`)
- Streamlitベースの使いやすいUI

## データ形式

## 制限事項
