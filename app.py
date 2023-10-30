from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mensaje = '¡Hola desde tu página web hecha con Python y Flask! 💋'
    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
