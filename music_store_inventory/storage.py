import os
import pickle
from typing import List

from .models import MusicRecord

DATA_FILE = os.path.join(os.path.dirname(__file__), "musicRecord.pkl")


def load_records() -> List[MusicRecord]:
    """Load records from the pickle data file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "rb") as music_record:
            raw_records = pickle.load(music_record)
    except (EOFError, pickle.UnpicklingError):
        return []

    return [MusicRecord.from_dict(item) for item in raw_records]


def save_records(records: List[MusicRecord]) -> None:
    """Persist records to the pickle data file."""
    with open(DATA_FILE, "wb") as music_record:
        pickle.dump([record.to_dict() for record in records], music_record)


def next_album_id(records: List[MusicRecord]) -> int:
    if not records:
        return 1
    return max(record.albumuniqueid for record in records) + 1
