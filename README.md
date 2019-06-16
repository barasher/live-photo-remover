# live-photo-remover

Removes "live photo" movies when retrieving pictures from IPhone.

## Usage

```
$ python3 remover.py  -h
usage: remover.py [-h] -f folder [-d]

optional arguments:
  -h, --help  show this help message and exit
  -f folder   Source folder
  -d          Dry run (simulation)
```

Parameters :
- **f** : Folder to clean (`-f /tmp/pictures/`), **required**
- **d** : Dry run (shows what should be deleted) (`-d`)
