from flask import session

class Api(object):
	
	def error(self,error):
		fullError = {}
		fullError["result"] = error

		return fullError

	def get(self):
		if ('wall' not in session):
			session['wall'] = []

		return {
			"result":"OK",
			"messages": session['wall']
		}

	def set(self, msg):
		if ('wall' not in session):
			session['wall'] = []

		wallDict = {}
		wallDict["message"] = msg

		session['wall'].append(wallDict);

		result = self.get()
		result["result"] = "Message Received"

		return result

	def __init__(self):
		pass