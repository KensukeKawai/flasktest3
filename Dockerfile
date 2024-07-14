# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコピー
COPY requirements.txt /app/

# 依存関係をインストール
RUN pip install -r requirements.txt

# プロジェクトファイルをコピー
COPY . /app/

# ポートを開放
EXPOSE 5000

# アプリケーションを起動
CMD ["python", "app.py"]