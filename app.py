from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', active_page='index')

@app.route('/qui_suis_je')
def qui_suis_je():
    return render_template('base.html', active_page='qui_suis_je')

@app.route('/competences')
def competences():
    return render_template('base.html', active_page='competences')

@app.route('/portfolio')
def portfolio():
    return render_template('base.html', active_page='portfolio')

@app.route('/experience')
def experience():
    return render_template('base.html', active_page='experience')

if __name__ == '__main__':
    app.run(debug=True)
