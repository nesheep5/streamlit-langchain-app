# streamlit-lngchain-app
ChatGPT APIを利用したAIチャットWebアプリ。 自身の学習用に作成。

- Agentを使って必要に応じて外部情報を検索 (dackdack-go, Wikipedia)
- 会話履歴を踏まえた応答

参考書籍 : [ChatGPT/LangChainによるチャットシステム構築［実践］入門](https://amzn.to/3Otp6Gk)

<img width="1134" alt="スクリーンショット 2024-11-28 11 07 54" src="https://github.com/user-attachments/assets/cf343674-1d94-4f11-8f3c-c5a2e18b5fcb">


## Usage
### 環境変数
```env
OPENAI_API_KEY=<自身で発行したChatGPT API Key>
OPENAI_API_MODEL=gpt-3.5-turbo
OPENAI_API_TEMPERATURE=0.5
```

### 環境構築
#### (Optional) 仮想環境
参考 : [pip と venv を使って仮想環境にパッケージをインストールする](https://packaging.python.org/ja/latest/guides/installing-using-pip-and-virtual-environments/)
```sh
python3 -m venv .venv
source .venv/bin/activate
```

#### pip install
```sh
pip install -r requirements.txt
```
### 起動
```sh
streamlit run app.py
```
