# `aw-watcher-netstatus`

An [ActivityWatch](https://activitywatch.net/) monitor for observing the network connection status.

## Purpose

> On the internet, Wonderland is recursive, with rabbit holes opening up to yet more rabbit holes; you never stop falling.
>
> —[Henrik Karlsson](https://escapingflatland.substack.com/p/search-query)

Librar𝘪𝘦𝘴 of Alexandria, brimming with knowledge, promise, culture; an unrelenting, expanding periphery; innumerable collections of untold riches; a source of wonder and awe—all a single keypress away. It's suffocating.


# Installation

1. Install the module with `pip`. This will add `aw-watcher-netstatus` to your `$PATH`.

    ```
    pip install aw-watcher-netstatus
    ```

2. `aw-qt` can now find the module; to start it by default add `aw-watcher-netstatus` to the `aw-qt.toml` configuration file (find the location [here](https://docs.activitywatch.net/en/latest/directories.html)), e.g.
    ```
    $ cat  $AW_DIRECTORY/aw-qt/aw-qt.toml

    [aw-qt]
    autostart_modules = ["aw-server", "aw-watcher-afk", "aw-watcher-window", "aw-watcher-netstatus"]
    ```

# Development

1. Prerequisites: Clone the repository. Install [Poetry](https://python-poetry.org/).
2. Run `poetry install` in the root of the directory. 
3. Start the ActivityWatch server in development mode:

    ```
    $ AW_PATH/aw-server --testing --verbose
    ```

4. Run `aw-watcher-netstatus` in development mode, this will connect to `localhost:8080` by default.

    ```
    $ poetry run aw-watcher-netstatus --testing -v
    ```

5. Open a socket at that port; observe the logs produced by `aw-watcher-netstatus`, view the timeline at `localhost:5666`.

    ```
    nc -l -k 8080
    ```


