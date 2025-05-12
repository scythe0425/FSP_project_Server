from flask import Flask
from search import search_bp
from db import db_bp
from chrome import chrome_bp

app = Flask(__name__)

# 블루프린트 등록
app.register_blueprint(search_bp, url_prefix='/search')
app.register_blueprint(db_bp, url_prefix='/db')
app.register_blueprint(chrome_bp, url_prefix='/chrome')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    