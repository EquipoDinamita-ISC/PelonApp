from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/abaut')
def about():
    return render_template('abaut.html')
    
@app.route('/calendario')
def calendar():
    return render_template('calendario.html')

if __name__ == '__main__':
    app.run()  