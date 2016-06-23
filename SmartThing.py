
class SmartThing(object):
	def __init__(self, category):
		
		self.category = category
		
		self.status = {}
		# self.schedule = {}
		self.history = {}

# current status of every object:
	def get_all_status(self):
		# return status
		print ("Status of " + self.category + ":" )
		for name in self.status:
			if self.status[name] == True:
				print "  " + name + ":" + "on"
			else:
				print "  " + name + ":" + "off"

# current status of specific objects
	def get_specific_status(self, name):
		print ("Status of " + name + ":" )
		# self.status[name]. dict. pass name 
		if self.status[name] == True:
			print "  " + name + ":" + "on"
		else:
			print "  " + name + ":" + "off"
	
	# changing the status of every item in SmartHome
	def set_status(self, name, value):
		self.status[name] = value
		self.history[name] = [value]

# change the status from on/off to on/off
	def toggle_status(self, name):
		if self.status[name] == True:
			self.status[name] = False
			self.history[name] += [False]
		else:
			self.status[name] = True
			self.history[name] += [True]

	def print_history(self, name):
		print ("history of " + name + ":" )
		h = self.history[name]
		for condition in h:
			if condition == True:
				print "on"
			else:
				print "off"









