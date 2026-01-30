from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/about.html')
def about():
     return render_template('about.html')

@app.route('/room.html')
def room():
     return render_template('room.html')
 
if __name__ == '__main__':
    app.run()
