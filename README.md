# MusicStoreInventory
An inventory that maintains music record information
Music record information is stored in a SQLite database.

The application uses a small package structure:

- `music_store_inventory/models.py` defines the music record model.
- `music_store_inventory/storage.py` manages SQLite persistence.
- `music_store_inventory/services.py` contains inventory operations.
- `musicStoreMain.py` provides the command-line entry point.

Run the application with:

```sh
python musicStoreMain.py
```

Run the tests with:

```sh
python -m pytest -q
```
