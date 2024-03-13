from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/analysis', methods=['GET'])
def get_analysis_results():
    # 분석 결과를 가정한 예시
    analysis_results = {'total_sales': 100000, 'top_menu': 'Coffee'}
    return jsonify(analysis_results)

if __name__ == '__main__':
    app.run(debug=True)
