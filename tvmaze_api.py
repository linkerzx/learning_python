import json, requests, datetime

def json_response(myjson):
	return json.loads(''.join(myjson))

def logger(extras):
	return None

class tvmaze_api: 
	def __init__(self):
		self.name = 'Tvmaze_api'
		self.url = "http://api.tvmaze.com"
	def connect(self, endpoint):
		try:
			logger("{'code_path': 'tvmaze_api', 'evt': 'connection_attempt'}")
			t = requests.get(self.url + endpoint)
		except:
			logger("{'code_path': 'tvmaze_api', 'evt': 'connection_exception'}")
			t = None
		return t 			
	def get_updates(self, update_time):
		t = self.connect("/updates/shows")
		parsed_data = json_response(t)
		results = [k for k in parsed_data if parsed_data[k] >= update_time]
		return results
	def get_show(self, tvmaze_showid):
		connect_str = '/shows/{id}'.format(id=tvmaze_showid)
		t = self.connect(connect_str)
		return json_response(t)
	def get_episodes(self, tvmaze_showid):
		connect_str = '/shows/{id}/episodes'.format(id=tvmaze_showid)
		t = self.connect(connect_str)
		return json_response(t)