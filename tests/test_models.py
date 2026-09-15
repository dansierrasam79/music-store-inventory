from music_store_inventory.models import MusicRecord


def test_music_record_to_dict_round_trip():
    record = MusicRecord(
        albumuniqueid=1,
        bandartist="Artist",
        albumtitle="Album",
        yearpublished="1999",
        duration="42",
        recordlabel="Label",
    )

    data = record.to_dict()
    assert data["albumuniqueid"] == 1
    assert data["bandartist"] == "Artist"

    rebuilt = MusicRecord.from_dict(data)
    assert rebuilt.albumuniqueid == 1
    assert rebuilt.bandartist == "Artist"