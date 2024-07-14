from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# データベース設定
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'mysql+pymysql://user:password@db:3306/myflaskapp')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# データベースモデルの定義
class CarData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.Float, nullable=False)
    pitch = db.Column(db.Float, nullable=False)
    yaw = db.Column(db.Float, nullable=False)

# データベースの初期化
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    data = CarData.query.all()
    return render_template('index.html', data=data)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    roll = data['roll']
    pitch = data['pitch']
    yaw = data['yaw']
    
    new_data = CarData(roll=roll, pitch=pitch, yaw=yaw)
    db.session.add(new_data)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
