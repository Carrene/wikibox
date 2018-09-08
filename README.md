# wikibox
A WSGI SSR to render markdown to HTML including indexing


# CLI

Change to your markdowns directory and run:
```bash
wikibox
```


```bash
usage: wikibox [-h] [-c CONFIG_FILES] [-b {HOST:}PORT] [-C DIRECTORY] [-V]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_FILES, --config-file CONFIG_FILES
                        This option may be passed multiple times.
  -b {HOST:}PORT, --bind {HOST:}PORT
                        Bind Address. default: 8080
  -C DIRECTORY, --directory DIRECTORY
                        Change to this path before starting the server default
                        is: `.`
  -V, --version         Show the version.
```

