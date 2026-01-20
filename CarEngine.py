class Petrol:
    def tank(self):
        print('Tank is filled!!')

class Engine:
    def __init__(self,petrol):
        self.petrol = petrol
    def start_engine(self):
        self.petrol.tank()
        print('Engine Started')

petrol = Petrol()
motor = Engine(petrol)

motor.start_engine()