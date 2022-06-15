from functions.function import Function
from functions.flood import Flood

class FloodFunc(Function):
    """Флуд в чат"""

    def execute(self):
        flood = Flood(self.storage, self.settings)

        flood.ask()
        flood.start_processes()

