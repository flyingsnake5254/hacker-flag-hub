from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/learn')
def learn_page():
    return render_template('learn.html')    


@app.route('/problems')
def problems_page():
    return render_template('problems.html')   

@app.route('/scoreboard')
def scoreboard_page():
    return render_template('scoreboard.html')   


if __name__ == '__main__':
    app.run(debug=True)
