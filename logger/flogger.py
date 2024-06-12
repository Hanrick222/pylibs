from core.actime import ACTime

class Logger:
    def __init__(self, instance):
        self.instance = instance
    
    def info(self, message):
        print(f"[INFO - {ACTime.fTime()} - {self.instance}] - {message}")


    def error(self, message):
        print(f"[HIBA - {ACTime.fTime()} - {self.instance}] - {message}")