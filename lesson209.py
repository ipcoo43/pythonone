from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

# flask 프로그램 - > lesson209.py
# 모듈 -> 우리가 만든 코드를 호출 : 프레임워크