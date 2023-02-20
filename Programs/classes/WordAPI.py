import time

import requests


class WordAPI:
    def __init__(self):
        self.apiToken = "https://api.datamuse.com/words?sp="
        self.freq = "&md=f&max=1"

    def GetFrequency(self, word):
        word = str(word)
        while True:
            try:
                response = requests.get(self.apiToken + word + self.freq).json()
            except:
                print("Call Failed: Retrying")
                time.sleep(.05)
                continue
            break
        return 0.0 if len(response) == 0 else float(response[0]['tags'][0][2:])
