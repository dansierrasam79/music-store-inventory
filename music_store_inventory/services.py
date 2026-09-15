from . import storage
from .models import MusicRecord


def add_music_record_service():
    """Collect one record from the terminal and save it."""
    records = storage.load_records()

    artist = input("Enter the band or artist: ").strip()
    title = input("Enter the album title: ").strip()
    year = input("Enter the year published: ").strip()
    duration = input("Enter the duration (in minutes): ").strip()
    label = input("Enter the record label: ").strip()

    record = MusicRecord(
        albumuniqueid=storage.next_album_id(records),
        bandartist=artist,
        albumtitle=title,
        yearpublished=year,
        duration=duration,
        recordlabel=label,
    )

    records.append(record)
    storage.save_records(records)
    print("Music record added successfully.")


def search_music_records_service():
    """Search records by the selected menu field."""
    print("Search Music Records Menu")
    print("1. By Album Unique ID")
    print("2. By Band or Artist")
    print("3. By Album Title")
    print("4. By Year Published")
    print("5. By Record Label")

    try:
        choice = int(input("Enter a choice (1-5): "))
    except ValueError:
        print("Please enter a valid menu option.")
        return

    records = storage.load_records()
    found = []

    if choice == 1:
        target = int(input("Enter a unique album ID: "))
        found = [r for r in records if r.albumuniqueid == target]
    elif choice == 2:
        target = input("Enter a band or artist: ").strip()
        found = [r for r in records if r.bandartist.lower() == target.lower()]
    elif choice == 3:
        target = input("Enter the album title: ").strip()
        found = [r for r in records if r.albumtitle.lower() == target.lower()]
    elif choice == 4:
        target = input("Enter the year published: ").strip()
        found = [r for r in records if r.yearpublished == target]
    elif choice == 5:
        target = input("Enter the record label: ").strip()
        found = [r for r in records if r.recordlabel.lower() == target.lower()]
    else:
        print("Invalid choice.")
        return

    if not found:
        print("Music Record Not Found!")
        return

    for record in found:
        print_record(record)


def print_record(record: MusicRecord) -> None:
    print("Album ID: ", record.albumuniqueid)
    print("Band or Artist: ", record.bandartist)
    print("Album Title: ", record.albumtitle)
    print("Year Published: ", record.yearpublished)
    print("Duration: ", record.duration)
    print("Record Label: ", record.recordlabel)
    print()


def view_music_records_service():
    records = storage.load_records()
    for record in records:
        print_record(record)


def change_music_records_service():
    records = storage.load_records()
    band = input("Enter a band or artist name: ").strip()
    album = input("Enter an album title: ").strip()

    target = None
    for record in records:
        if record.bandartist.lower() == band.lower() and record.albumtitle.lower() == album.lower():
            target = record
            break

    if target is None:
        print("Music Record not found!")
        return

    print("Record Information")
    print("Band/Artist: ", target.bandartist)
    print("Album Title: ", target.albumtitle)
    print("Year Published: ", target.yearpublished)
    print("Record Duration: ", target.duration)
    print("Record Label Name: ", target.recordlabel)

    print("Which item in the record would you like to change?")
    print("Menu Selection")
    print("1. Year Published")
    print("2. Duration")
    print("3. Record Label")

    try:
        choice = int(input("Enter a menu selection: "))
    except ValueError:
        print("Please enter a valid menu option.")
        return

    if choice == 1:
        target.yearpublished = input("Enter the new year published: ").strip()
    elif choice == 2:
        target.duration = input("Enter the new record duration: ").strip()
    elif choice == 3:
        target.recordlabel = input("Enter the new record label: ").strip()
    else:
        print("Invalid choice.")
        return

    storage.save_records(records)
    print("Music record updated successfully.")
