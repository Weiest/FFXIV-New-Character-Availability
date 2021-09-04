import requests
from bs4 import BeautifulSoup

class FFXIVCreationAvailabilityChecker:
    URL = 'https://na.finalfantasyxiv.com/lodestone/worldstatus/'
    status = {}

    def __init__(this):
        this.updateStatus()

    def __request_page__(this):
        results = {}
        response = requests.get(this.URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.findAll('div', {'class': 'world-list__item'})
        for item in data:
            try:
                world_name = item.find('div', {'class': 'world-list__world_name'}).text.strip()
                world_availability = True if item.find('div', {'class': 'world-list__create_character'}).find('i')['class'][0] == 'world-ic__available' else False
                results[world_name.lower()] = world_availability
            except:
                continue
        return results

    def updateStatus(this):
        this.status = this.__request_page__()

    def getServerNames(this):
        return this.status.keys()

    def checkAllServers(this):
        return this.status

    def checkServer(this, server_name):
        if server_name in this.status:
            return this.status[server_name.lower()]
        return None

if __name__ == "__main__":
    checker = FFXIVCreationAvailabilityChecker()
    print(checker.checkAllServers())
