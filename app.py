from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('form.html')

@app.route('/response', methods = ['POST'])
def response():
    return render_template('response.html', user = request.form['data'], method = request.method)

if __name__ == '__main__':
    app.debug = True
    app.run()
