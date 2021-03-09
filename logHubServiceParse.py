import re

class LogFile:
    def __init__(self, filename):
        self._filename = filename
        self._data = ''
    def parse(self):
        with open(self._filename, 'r') as file:
            self._data = file.read()
    def searchPackage(self):
        self.searchRequest()
    def searchRequest(self):

    def searchResponse(self):
