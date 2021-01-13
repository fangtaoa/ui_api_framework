from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class User(Resource):
	def get(self):
		return make_response(jsonify({"msg": "请登录", "status": 1001}))

	def post(self):
		if not request.json:
			return make_response(jsonify({"msg": "请求参数不是JSON字符串, 请检查", "status": 1002}))
		else:
			if request.json.get("name") == "张三" and request.json.get("passwd") == "123456":
				return make_response(jsonify({"msg": "登录成功", "status": 0}))


api.add_resource(User, "/api/user/login/")

if __name__ == '__main__':
	app.run(debug=True)

