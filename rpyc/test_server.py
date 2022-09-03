import rpyc
import pytest
from rpyc.utils.server import ThreadedServer
import threading

from server import RemoteClass


@pytest.fixture(autouse=True)
def client():
    """A fixture for generating a requests like test client
    Makes sure the usercode is dead
    Set up and tear down can be placed before and after the with
    """
    RemoteClass()


def test_attribute():
    """Test that attributes can be setup and torn down correctly"""
    c = rpyc.connect("localhost", 18861)
    c.root.a = 43
    assert (c.root.a == 43)
    c.root.a = 32
    assert (c.root.a == 32)

