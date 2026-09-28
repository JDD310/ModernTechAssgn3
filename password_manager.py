from dataclasses import dataclass, field
from typing import List

from cryptography.fernet import Fernet


@dataclass
class PasswordEntry:
    entry_id: int
    title: str
    username: str
    password: str


class PasswordManagerStore:
    def __init__(self):
        self._entries: List[PasswordEntry] = []
        self._next_id = 1
        self._cipher = Fernet(Fernet.generate_key())

    def add_entry(self, title: str, username: str, password: str) -> PasswordEntry:
        encrypted_password = self._cipher.encrypt(password.encode()).decode()
        entry = PasswordEntry(
            entry_id=self._next_id,
            title=title,
            username=username,
            password=encrypted_password,
        )
        self._entries.append(entry)
        self._next_id += 1
        return entry

    def list_entries(self):
        return [
            {
                'id': entry.entry_id,
                'title': entry.title,
                'username': entry.username,
                'password': self._cipher.decrypt(entry.password.encode()).decode(),
            }
            for entry in self._entries
        ]

    def delete_entry(self, entry_id: int) -> bool:
        for index, entry in enumerate(self._entries):
            if entry.entry_id == entry_id:
                del self._entries[index]
                return True
        return False
