from flask import Flask

app = Flask(__name__, static_folder='frontend/static')


if __name__ == '__main__':
    app.run(debug=True)
