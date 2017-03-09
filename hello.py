from flask import Flask, render_template, url_for


app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/vision')
def vision():
	return render_template('vision.html')

@app.route('/cifar10info')
def cifar10info():
	return render_template('cifar10info.html')

@app.route('/neuralnet')
def neuralnet():
	return render_template('neuralnet.html')

@app.route('/convarch')
def convarch():
	return render_template('convarch.html')

if __name__ == '__main__':
    app.run()