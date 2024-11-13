from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# 创建 Flask 应用
app = Flask(__name__)
CORS(app)  # 启用 CORS

# 加载训练好的模型
model = joblib.load('best_rf_model.pkl')

# 定义 API 路由
@app.route('/predict', methods=['POST'])
def predict():
    # 获取请求的 JSON 数据（前端传来的数据）
    data = request.get_json()

    # 将 JSON 数据转换为 DataFrame
    input_data = pd.DataFrame([data])

    # 模型预测
    prediction = model.predict(input_data)

    # 返回预测结果
    response = {
        'prediction': prediction[0]
    }
    return jsonify(response)

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)
