import random


class PythonPredictor:
    def __init__(self, config):
        pass
    
    def predict(self, payload):
        """Returns random positive integers"""
        return random.randint(0, 100)
