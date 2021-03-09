import re

class functionDeclare:
    def __init__(self, source):
        self._source = source
        self.name =""
        self.variable =[]
        self.parse()
    def parse(self):
        self.name = re.findall(r'\s[a-zA-Z_]*.+?(?=\()', self._source, re.I)
        self.variable = re.findall(r'\((.*)\)', self._source, re.I)

class procedureDeclare:
    def __init__(self, source):
        self._source = source
        self.name =""
        self.variable =[]
        self.parse()
    def parse(self):
        self.name = re.findall(r'\s[a-zA-Z_]*.+?(?=\()', self._source, re.I)
        self.variable = re.findall(r'\((.*)\)', self._source, re.I)
class FileParser:
    def __init__(self, filename):

        self._fileName = filename
        self._fileData = ""
        self._procedureDeclare = []
        self._procedureCalling = []
        self._functionDeclare = []
        self._functionCalling = []
        self._TableCalling = []

    def search_procedure_declare(self):
        result = re.findall(r'PROCEDURE\s+[a-zA-Z_]*\([a-zA-Z0-9_,:=\n+\s.]+\)', self._fileData, re.I)
        self._procedureDeclare = [procedureDeclare(re.sub(r'^\s+|\n|\r|\s+$', ' ', line)) for line in result]
        return self._procedureDeclare

    def search_procedure_calling(self):
        return self._procedureCalling

    def search_function_declare(self):
        result = re.findall(r'FUNCTION\s+[a-zA-Z_]*\([a-zA-Z0-9_,:=\n+\s.]+\)', self._fileData, re.I)
        self._functionDeclare = [functionDeclare(re.sub('^\s+|\n|\r|\s+$', ' ', line)) for line in result]
        return self._functionDeclare

    def search_function_calling(self):
        #([a-zA-Z_.0-9]*\([a-zA-Z0-9_.*,'\s]*\))
        result = re.findall(r'([a-zA-Z_.0-9]*\([a-zA-Z0-9_.*,\'\s]*\))', self._fileData, re.I)
        self._functionCalling = [line for line in result]
        return self._functionCalling

    def search_table_calling(self):
        return self._TableCalling

    def start_parse(self):
        with open(self._fileName, mode='r') as file:
            self._fileData = file.read()
            return True
        return False

