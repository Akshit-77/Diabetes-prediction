from flask import Flask , render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def glucose_calculator():
    age = request.form.get('age')
    gender = request.form.get('gender')
    bmi = request.form.get('bmi')
    bp = request.form.get('bp')
    s1 = request.form.get('s1')
    s2 = request.form.get('s2')
    s3 = request.form.get('s3')
    s4 = request.form.get('s4')
    s5 = request.form.get('s5')
    s6 = request.form.get('s6')

    result = model.predict(np.array([age, gender, bmi, bp, s1, s2, s3, s4, s5, s6]).reshape(1,10))
    result = str(result.item())
    return render_template('index.html', result = result)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)