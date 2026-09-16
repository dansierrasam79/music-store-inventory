from music_store_inventory import storage
from music_store_inventory.models import MusicRecord


def test_sqlite_storage_round_trip(tmp_path, monkeypatch):
    database_path = tmp_path / "music_store_inventory.db"
    monkeypatch.setattr(storage, "DATA_FILE", str(database_path))

    records = [
        MusicRecord(
            albumuniqueid=2,
            bandartist="Artist B",
            albumtitle="Second Album",
            yearpublished="2002",
            duration="44",
            recordlabel="Label B",
        ),
        MusicRecord(
            albumuniqueid=1,
            bandartist="Artist A",
            albumtitle="First Album",
            yearpublished="2001",
            duration="40",
            recordlabel="Label A",
        ),
    ]

    storage.save_records(records)

    assert storage.load_records() == [records[1], records[0]]
    assert storage.next_album_id(storage.load_records()) == 3
