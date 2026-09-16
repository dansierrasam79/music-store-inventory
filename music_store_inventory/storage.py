import os
import sqlite3
from typing import List

from .models import MusicRecord

DATA_FILE = os.path.join(os.path.dirname(__file__), "music_store_inventory.db")


def _connect() -> sqlite3.Connection:
    connection = sqlite3.connect(DATA_FILE)
    connection.row_factory = sqlite3.Row
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS music_records (
            albumuniqueid INTEGER PRIMARY KEY,
            bandartist TEXT NOT NULL,
            albumtitle TEXT NOT NULL,
            yearpublished TEXT NOT NULL,
            duration TEXT NOT NULL,
            recordlabel TEXT NOT NULL
        )
        """
    )
    connection.commit()
    return connection


def load_records() -> List[MusicRecord]:
    """Load all records from the SQLite database."""
    with _connect() as connection:
        rows = connection.execute(
            """
            SELECT albumuniqueid, bandartist, albumtitle,
                   yearpublished, duration, recordlabel
            FROM music_records
            ORDER BY albumuniqueid
            """
        ).fetchall()

    return [MusicRecord.from_dict(dict(row)) for row in rows]


def save_records(records: List[MusicRecord]) -> None:
    """Replace the stored records with the supplied records."""
    with _connect() as connection:
        connection.execute("DELETE FROM music_records")
        connection.executemany(
            """
            INSERT INTO music_records (
                albumuniqueid, bandartist, albumtitle,
                yearpublished, duration, recordlabel
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    record.albumuniqueid,
                    record.bandartist,
                    record.albumtitle,
                    record.yearpublished,
                    record.duration,
                    record.recordlabel,
                )
                for record in records
            ],
        )


def next_album_id(records: List[MusicRecord]) -> int:
    if not records:
        return 1
    return max(record.albumuniqueid for record in records) + 1
