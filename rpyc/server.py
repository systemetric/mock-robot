from audioop import mul
from glob import glob
import rpyc
from rpyc.utils.server import ThreadedServer
import threading
import logging
import multiprocessing

class MockRobot:
    """A robot which mocks the robot interface runs on x86 for shepherd dev"""
    def __init__(self) -> None:
        print("init'd a mock robot")
        self.wait_for_start()

    def wait_for_start(self):
        """The old robot still needs to wait for start through a fifo so that
        shepherd-1 still works
        """
        print("MockRobot.wait_for_start called")


class RemoteClass(MockRobot, rpyc.Service):
    """The underlying class which is actually responsible for the hardware"""

    def __init__(self) -> None:
        """Create a threaded server to handle multiple clients.
        Does not block on creation of the server
        """
        super().__init__()

    def on_connect(self, conn):
        """When a client connects"""
        logging.info("New connection to Remote Object")

    def on_disconnect(self, conn):
        """When a client disconnects"""
        logging.info("Connection to Remote Object destroyed")

    def _rpyc_setattr(self, name, value):
        """Set the default behaviour of setattr remotely to be settattr locally"""
        setattr(self, name, value)

    def _rpyc_delattr(self, name):
        """Set the default behaviour of delattr remotely to be delattr locally"""
        delattr(self, name)

    def wait_for_start(self):
        """Override the Robot's wait for start to do the wait for start within
        the confines of shepherd"""
        print("RemoteServer wait for start called")
        start_signal.wait()
        print("Remote start signal set")


def run_remote_object():
    global remote_class
    remote_class = RemoteClass()
    server = ThreadedServer(remote_class, port=18861, protocol_config={
        "allow_all_attrs": True,
        "allow_setattr": True,
    })
    server.start()


if __name__ == "__main__":
    start_signal = multiprocessing.Event()
    proc = multiprocessing.Process(target=run_remote_object)
    try:
        proc.start()
        start_signal.set()
    finally:
        proc.join()
