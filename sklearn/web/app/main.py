from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

model = joblib.load('models/model.joblib')


@app.route('/')
def home():
    return render_template('home.html', message="Hello World!")


@app.route('/api/v1/predict', methods=['POST'])
def predict():
    json_data = request.json
    result = model.predict([json_data])
    return jsonify({'class': int(result[0])})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=4000)
