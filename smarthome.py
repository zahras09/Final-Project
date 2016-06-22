from SmartThing import SmartThing

# create class
class SmartHome(object):
	# a special method that gets run when you create an instance of a class
	# the parameters that go inside init, only values that are necessary to
	# create a new instance.
	def __init__(self):
		self.all_things = {"hvac": SmartThing("hvac"),
							"lights": SmartThing("lights"),
							"security": SmartThing("security"),
							"appliances": SmartThing("appliances")}

	# always call key of dict.
	def set_status(self, category, name, status):
		self.all_things[category].set_status(name, status)

# more general, bc each smart thing can print of specific item or all.
	def get_status(self, category, name):
		if name == "all":
			self.all_things[category].get_all_status()
		else:
			self.all_things[category].get_specific_status(name)


	def toggle_status(self, category, name):
		self.all_things[category].toggle_status(name)

	def get_history(self, category, name):
		self.all_things[category].print_history(name)



	# Methods:
	# add hvac component (heating, cooling)
	# add light  (different rooms) (to populate the dictionary in SmartThing)
	# add security (camera 1, camera 2)
	# add appliance 

	# get status method takes in category, prints status of everything

	# how many lights are on? would have to modify SmartThing i think

# home = SmartHome()
# home.all_things["lights"].set_status("bedroom", True)
# home.all_things["lights"].set_status("dinning", False)
# # finish the rest of the rooms
# home.all_things["lights"].get_real_status()


# home.all_things["hvac"].set_status("heating", True)
# home.all_things["hvac"].get_real_status()

# home.all_things["hvac"].toggle_status("heating")
# home.all_things["hvac"].get_real_status()


