from dataclasses import dataclass


@dataclass
class MusicRecord:
    """Represents one music inventory record."""

    albumuniqueid: int
    bandartist: str
    albumtitle: str
    yearpublished: str
    duration: str
    recordlabel: str

    @classmethod
    def from_dict(cls, data: dict) -> "MusicRecord":
        return cls(
            albumuniqueid=data.get("albumuniqueid", 0),
            bandartist=data.get("bandartist", ""),
            albumtitle=data.get("albumtitle", ""),
            yearpublished=data.get("yearpublished", ""),
            duration=data.get("duration", ""),
            recordlabel=data.get("recordlabel", ""),
        )

    def to_dict(self) -> dict:
        return {
            "albumuniqueid": self.albumuniqueid,
            "bandartist": self.bandartist,
            "albumtitle": self.albumtitle,
            "yearpublished": self.yearpublished,
            "duration": self.duration,
            "recordlabel": self.recordlabel,
        }
