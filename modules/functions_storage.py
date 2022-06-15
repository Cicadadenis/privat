import asyncio
import importlib.util
import inspect
import os

from typing import List, Callable, Awaitable, Union

from .sessions_storage import SessionsStorage
from .settings import Settings

class FunctionsStorage:
    def __init__(
        self,
        directory: str,
        sessions_storage: SessionsStorage,
        settings: Settings
    ):
        self.storage = sessions_storage
        self.settings = settings

        self.functions: List[Union[Callable, Awaitable]] = []

        for file in os.listdir(directory):
            if file.endswith(".py"):
                self.load_function(
                    file[:-3], os.path.join(directory, file)
                )

        self.functions.sort(key=lambda item: item[1].lower())

    def load_function(self, name: str, path: str):
        spec = importlib.util.spec_from_file_location(name, path)
        function = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(function)

        self.register_function(function)

    def register_function(self, module):
        for classname, classobj in inspect.getmembers(module, inspect.isclass):
            if classname.endswith("Func"):
                self.functions.append((
                    classobj(self.storage, self.settings),
                    classobj.__doc__
                ))

    def execute(self, index: int):
        try:
            function_instance = self.functions[index][0]
        except Exception:
            return

        function = function_instance.execute()

        if inspect.isawaitable(function):
            asyncio.get_event_loop().run_until_complete(function)
