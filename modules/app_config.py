import json

class Config():

    def __init__(self):
        self.config = self.loadJson("config.json")
        self.wording = self.wording()
        self.langTitle = self.wording['title']
        self.appName = self.config['name']
        self.appDescription = self.config['description']
        
    def lang(self, lang: str):
        return self.loadJson(f"lang/{lang}.json")

    def loadJson(self, filename: str):
        f = open(filename).read()
        return json.loads(f)

    def wording(self) :
        return self.lang(self.config['lang'])




