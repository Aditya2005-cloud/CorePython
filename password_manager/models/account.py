"""Account data and JSON persistence for the password manager."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


STORAGE_PATH = Path(__file__).resolve().parents[1] / "storage" / "json_storage.json"


def load_accounts(path: Path | str = STORAGE_PATH) -> list[dict[str, str]]:
    """Load saved accounts, returning an empty list on first run."""
    storage_path = Path(path)
    if not storage_path.exists():
        return []

    try:
        with storage_path.open("r", encoding="utf-8") as file:
            accounts: Any = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in account file: {storage_path}") from exc

    if not isinstance(accounts, list) or any(
        not isinstance(account, dict)
        or not all(isinstance(account.get(key), str) for key in ("service", "username", "password"))
        for account in accounts
    ):
        raise ValueError("Account file must contain a list of service, username, and password records")
    return accounts


def save_accounts(accounts: list[dict[str, str]], path: Path | str = STORAGE_PATH) -> None:
    """Save account records as formatted JSON."""
    storage_path = Path(path)
    storage_path.parent.mkdir(parents=True, exist_ok=True)
    with storage_path.open("w", encoding="utf-8") as file:
        json.dump(accounts, file, indent=2, ensure_ascii=False)
        file.write("\n")
