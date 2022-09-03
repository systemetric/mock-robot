# saved as greeting-client.py
import Pyro5.api

class Robot:
    def __init__(self) -> None:
        self.greeting_maker = Pyro5.api.Proxy('PYRO:Greeting@0.0.0.0:9090')
print(greeting_maker.get_fortune("Edwin"))   # call method normally
print(greeting_maker.a)
greeting_maker.a = 10
print(greeting_maker.a)
print(greeting_maker.get_a())