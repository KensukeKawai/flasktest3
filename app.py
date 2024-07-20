from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# SQLiteデータベースファイルのパス
db_path = os.path.join(os.path.dirname(__file__), 'app.db')

app = Flask(__name__)

# SQLiteデータベースの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# データベースモデルの定義
class CarData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.Float, nullable=False)
    pitch = db.Column(db.Float, nullable=False)
    yaw = db.Column(db.Float, nullable=False)

# データベースの初期化
with app.app_context():
    db.create_all()

# 関数とURLを結び付け（bind）したいときは、route()デコレータを使用
# 指定したURLのリクエストが来た際に実行される関数を定義
# @app.route('/user/<username>')のように<>を使ってURLを動的に変化させることができる
# routeデコレータは内部的にWerkzeug(ヴェルクツォイク)のRuleクラスのインスタンスを作成
@app.route('/')
def index():
    data = CarData.query.all()
    # テンプレートを変換(Rendering)する場合、render_template()メソッドを使用
    # テンプレートは「templates」フォルダの中に入れる
    return render_template('index.html', data=data)

@app.route('/', methods=['POST'])
def upload_data():
    data = request.get_json()
    roll = data['roll']
    pitch = data['pitch']
    yaw = data['yaw']
    
    # 定義したデータベースモデルの各要素に変数を指定
    new_data = CarData(roll=roll, pitch=pitch, yaw=yaw)
    db.session.add(new_data)
    db.session.commit()
    
    
    # ユーザーを別のエンドポイントへリダイレクトする場合はredirect()関数を使用
    # 特定の関数に対応するURLを構築するには「url_for()」メソッドを使用
    # url_for()メソッドで関数名からURLへ逆変換
    # 引数：index関数、URL：'/'
    return redirect(url_for('index'))
    # もしエラーコードと一緒に異常終了させるには、abort()関数を使用(例：abort(401))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)