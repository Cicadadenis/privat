from functions.edit_message import ReportFunc
from modules.settings import Settings
from modules.sessions_storage import SessionsStorage
from modules.functions_storage import FunctionsStorage
settings = Settings()

sessions_storage = SessionsStorage(
    "sessions",
    settings.api_id,
    settings.api_hash
)    
functions_storage = FunctionsStorage(
                "functions",
                sessions_storage,
                settings
            )
print("go")
storage=functions_storage
ReportFunc(storage, settings)