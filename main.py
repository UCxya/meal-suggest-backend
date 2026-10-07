from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # フロントエンドからの通信を許可

@app.route('/')
def home():
    return jsonify({"message": "食事提案APIサーバー起動中！"})

@app.route('/api/suggest', methods=['POST'])
def suggest_meal():
    data = request.get_json() or {}
    category = data.get('category', '指定なし')
    
    meals = {
        '和食': ['豚の生姜焼き', '肉じゃが', '鮭の塩焼き', 'うどん'],
        '洋食': ['ハンバーグ', 'オムライス', 'カルボナーラ', 'カレー'],
        '中華': ['麻婆豆腐', 'チャーハン', '餃子', '回鍋肉']
    }
    
    if category in meals:
        suggested = random.choice(meals[category])
    else:
        all_meals = [m for sublist in meals.values() for m in sublist]
        suggested = random.choice(all_meals)
        
    return jsonify({
        "status": "success",
        "requested_category": category,
        "suggested_meal": suggested
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)