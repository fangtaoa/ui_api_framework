import requests


class HTTPRequests:
	def request(self, url, method="get", is_session=False, **kwargs):
		if is_session:
			requester = requests.Session().request
		else:
			requester = requests.request
		if method.lower() == "get".lower():
			return requester(url=url, method=method, **kwargs)
		elif method.lower() == "post".lower():
			return requester(url=url, method=method, **kwargs)
		elif method.lower() == "put".lower():
			return requester(url=url, method=method, **kwargs)
		elif method.lower() == "delete".lower():
			return requester(url=url, method=method, **kwargs)

	def get(self, url, **kwargs):
		return self.request(url, **kwargs)

	def post(self, url, **kwargs):
		return self.request(url, method="post", **kwargs)

	def put(self, url, **kwargs):
		return self.request(url, method="put", **kwargs)

	def delete(self, url, **kwargs):
		return self.request(url, method="delete", **kwargs)
