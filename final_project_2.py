# create class
# class SmartHome(object):
# 	# a special method that gets run when you create an instance of a class
# 	# the parameters that go inside init, only values that are necessary to
# 	# create a new instance.
# 	def __init__():
# 		self.all_things = {"hvac":[],
# 							"lights":[],
# 							"security":[],
# 							"appliances":[]}

# 		# self.option1 = hvac
# 		# self.option2 = security
# 		# self.option3 = appliances
# 		# self.option4 = lighting
# 	def new_thing (type, name):
# 		new_thing = SmartThing(type, name)
# 		self.all_things [type].append(new_thing)


from filename import SmartHome

class SmartThing(object):
	def __init__(type, name):
		self.type = type
		self.name = name
		self.status = {"on":False}
		self.schedule = {}
# current status of every object:
	def get_real_status():
		talk_to_smart_obj_get_real_status
		return status

	
	# changing the status of every item in SmartHome?
	def set_status(attr, value):
		self.status[attr] = value
		self.talk_to_smart_obj_get_status



if __name__ == '__main__':
	main()
