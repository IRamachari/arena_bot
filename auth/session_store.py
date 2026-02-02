import json
from pathlib import Path

SESSION_PATH = Path("storage/session.json")

class SessionStore:
    @staticmethod
    def save(storage_state: dict):
        SESSION_PATH.parent.mkdir(parents=True, exist_ok=True)
        SESSION_PATH.write_text(json.dumps(storage_state))

    @staticmethod
    def load():
        if SESSION_PATH.exists():
            return json.loads(SESSION_PATH.read_text())
        return None
