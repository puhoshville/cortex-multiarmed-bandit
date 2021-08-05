import random


class PythonPredictor:
    def __init__(self, config):
        pass
    
    def predict(self, payload):
        """Returns random negative integers"""
        return random.randint(-100, 0)
