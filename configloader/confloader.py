import json

class Configuration:
    def __init__(self):
        with open("/home/linux/SCMS/api_scms/api_scms/config.json", "r") as f:
            self.cfg = json.load(f)
    
    def getCFG(self, seta, setb=None):
        if not setb:
            return self.cfg[seta]
        else:
            return self.cfg[seta][setb]