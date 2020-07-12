from handler import RequestHandler
 
class Router:

	requestHandler = {
		'/' : RequestHandler.home,
		'/home' : RequestHandler.home,
		'/list' : RequestHandler.display
	}

	@classmethod
	def route(cls, path):
		for k,v in cls.requestHandler.items():
			if k == path:
				v("hello")


Router.route("/")
'''
d = {'k':f}
d['k']("Hello")
''' 