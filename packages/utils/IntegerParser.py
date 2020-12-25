
class IntegerParser:
    def __init__(self):
        pass
    
    def is_int(self, value):
        try:
            return int(value), True
        except ValueError:
            pass
        return False
