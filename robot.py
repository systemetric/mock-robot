from typing import Any
import xmlrpc.client

class Robot:
    remote_robot: Any
    def __init__(self) -> None:
        self.remote_robot = xmlrpc.client.ServerProxy('http://localhost:8001')

    def __getattr__(self, __name: str):
        return getattr(self.remote_robot, __name)
        # if __name in self.remote_robot.system.listMethods():
        # else:
        #     raise AttributeError("Unknown attribute")

    def __setattr__(self, __name: str, __value) -> None:
        super().__setattr__(__name, __value)
        if __name in self.remote_robot.system.listMethods():
            setattr(self.remote_robot, __name, __value)
            return

if __name__ == "__main__":
    # Print list of available methods
    R = Robot()
    print(R.see())
    print(R.foo)
