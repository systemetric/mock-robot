import rpyc

class Robot:
    def __new__(cls):
        remote_robot = rpyc.connect("localhost", 18861).root
        remote_robot.reset()
        remote_robot.wait_for_start()
        return remote_robot