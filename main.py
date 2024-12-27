from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
scores = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_score():
    data = request.json
    username = data.get('username')
    speed = data.get('speed')

    if not username or not speed:
        return jsonify({'error': 'Invalid data'}), 400

    score = {'username': username, 'speed': speed, 'timestamp': datetime.now()}
    scores.append(score)

    return jsonify({'message': 'Score submitted successfully!', 'score': score}), 200

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    sorted_scores = sorted(scores, key=lambda x: x['speed'], reverse=True)[:10]
    return jsonify(sorted_scores), 200

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", ssl_context='adhoc')
