from smarthome import SmartHome

home = SmartHome()
home.set_status("hvac", "heating", True)
home.set_status("lights", "bedroom", True)
home.set_status("lights", "dining", False)
home.set_status("lights", "kitchen", True)
home.set_status("lights", "bathroom", False)


home.get_status("hvac", "all")
home.get_status("lights", "bedroom")
home.get_status("lights", "all")





home.toggle_status("hvac", "heating")

home.get_status("hvac", "all")

# change the status of set staus on/off and it will print the history
home.get_history("hvac", "heating")



# hvacObject = SmartThing("hvac")
# hvacObject.set_status("heating", True)
# hvacObject.get_real_status()

# home.set_status("lights", "bedroom", True)

# home.get_status("lights", "all")



