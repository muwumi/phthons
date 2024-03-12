# Flask를 사용한 간단한 RESTful API 예시

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/analysis_result', methods=['GET'])
def get_analysis_result():
    # 여기에 데이터 분석 결과를 얻는 로직을 구현
    analysis_result = {
        'result': '파이썬에서 분석한 결과입니다.',
        'data': [1, 2, 3, 4, 5]
    }
    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)
