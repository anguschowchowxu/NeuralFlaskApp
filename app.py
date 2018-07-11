#-*- encoding: utf8 -*-

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
	message = request.get_json(force=True)
	name = message['name']
	response = {
				'greeting': 'Hello' + name + '!'
	}

	return jsonify(response)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)