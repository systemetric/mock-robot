# saved as greeting-server.py
import Pyro5.api

@Pyro5.api.expose
class RemoteRobot(object):
    def __init__(self) -> None:
        self._a = 5

    def get_fortune(self, name):
        return "Hello, {0}. Here is your fortune message:\n" \
               "Behold the warranty -- the bold print giveth and the fine print taketh away.".format(name)

    @property
    def a(self):
        return self._a

    def get_a(self):
        return self._a

Pyro5.api.Daemon.serveSimple({
    RemoteRobot: 'Greeting',
}, host="0.0.0.0", port=9090, ns=False, verbose=True)

print("end")