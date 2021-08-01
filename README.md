# FFXIV Character Creation Availability
As FFXIV imposed character creation restrictions on congested worlds (especially during busy times) to reduce stress on the server however the server will eventually open up when the server is less congested. Refer to [Lodestone](https://na.finalfantasyxiv.com/lodestone/news/detail/80cd4583bf743600105b947d6906d0909189e479/).

Since I want to join a specific server, this restriction basically made me constantly check the servers for an opportunity to create a character. Looking around, I could not find a way to notify myself when it is available so I made a simple scraper to retrieve the server's status to check if character creation is possible.

This scraper will collect all server status regardless of its region.

## Usage
Start by declaring the object and just start calling methods.

```python
serverStatus = FFXIVCreationAvailabilityChecker()
updateStatus() # Pull for the latest update
getServerNames() # Returns a list of all server names
checkAllServers() # Returns a dictionary of the server names and its creation availabilty.
checkServer(server_name) # Returns the boolean of the status of the creation availabilty.
```
A simple example of how I used this to check for the availability was...
```python
import time
checker = FFXIVCreationAvailabilityChecker()
foo = False
while (not foo):
	foo = checker.checkServer('tonberry')
	time.sleep(5)
	checker.updateStatus()
print("Server is Available")
```
Remember to call **updateStatus()** so the server status updates after each loop and use **time.sleep()** to slow down and not bombard the servers! (Not my fault if you got blocked!)
