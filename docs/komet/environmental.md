
# Run Commands & Environment Variables

The basic command to run Komet is as follows:

=== "Windows / Mac / Linux"

    ``` py
    python plex_meta_manager.py
    ```

=== "Docker"

    ``` py
    docker run --rm -it -v "/<ROOT_KOMET_DIRECTORY_HERE>/config:/config:rw" meisnate12/komet
    ```

To customize the running of Komet according to your needs, you can use either run commands or environmental 
variables. Environmental variables take precedence over run command attributes. However, if you encounter a race 
condition where an attribute has been set both via an environmental variable and a shell command, the environmental 
variable will be given priority.

Please note that these instructions assume that you have a basic understanding of Docker concepts. If you need to 
familiarize yourself with Docker, you can check out the official tutorial.

Another way to specify environmental variables is by adding them to a .env file located in your config folder.

Environment variables are expressed as `KEY=VALUE` depending on the context where you are specifying them, you may enter 
those two things in two different fields, or some other way.  The examples below show how you would specify the 
environment variable in a script or a `docker run` command.  Things like Portainer or a NAS Docker UI will have 
different ways to specify these things.

???+ warning "Combining Commands or Variables"

    Some Commands or Variables can be combined in a single run, this is mainly beneficial when you want to run a specific command and have it run immediately rather than waiting until the next scheduled run.

    For example, if I want to run [Collections Only](#collections-only) to only run Collection Files, and [Run Immediately](#run) to skip waiting until my next scheduled run, I can use both commands at the same time:

    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --collections-only --run
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --collections-only --run
            ```

??? blank "Config Location&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-c`/`--config`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_CONFIG`<a class="headerlink" href="#config" title="Permanent link">¶</a>"

    <div id="config" />Specify the location of the configuration YAML file. Will default to `config/config.yml` when not 
    specified.

    <hr style="margin: 0px;">

    **Accepted Values:** Path to YAML config file

    **Shell Flags:** `-c` or `--config` (ex. `--config /data/config.yml`)

    **Environment Variable:** `KOMET_CONFIG` (ex. `KOMET_CONFIG=/data/config.yml`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --config /data/config.yml
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --config /data/config.yml
            ```

??? blank "Time to Run&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-t`/`--times`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_TIMES`<a class="headerlink" href="#times" title="Permanent link">¶</a>"

    <div id="times" />Specify the time of day that Komet will run. Will default to `05:00` when not 
    specified.

    <hr style="margin: 0px;">

    **Accepted Values:** Comma-separated list in `HH:MM` format

    **Shell Flags:** `-t` or `--times` (ex. `--times 06:00,18:00`)

    **Environment Variable:** `KOMET_TIMES` (ex. `KOMET_TIMES=06:00,18:00`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --times 22:00,03:00
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --times 22:00,03:00
            ```

??? blank "Run Immediately&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-r`/`--run`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_RUN`<a class="headerlink" href="#run" title="Permanent link">¶</a>"

    <div id="run" />Perform a run immediately, bypassing the time to run flag.

    <hr style="margin: 0px;">

    **Shell Flags:** `-r` or `--run` (ex. `--run`)

    **Environment Variable:** `KOMET_RUN` (ex. `KOMET_RUN=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --run
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --run
            ```

??? blank "Run Tests&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-ts`/`--tests`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_TESTS`<a class="headerlink" href="#tests" title="Permanent link">¶</a>"

    <div id="tests" />Perform a debug test run immediately, bypassing the time to run flag. **This will only run 
    collections with `test: true` in the definition.**

    <hr style="margin: 0px;">

    **Shell Flags:** `-ts` or `--tests` (ex. `--tests`)

    **Environment Variable:** `KOMET_TESTS` (ex. `KOMET_TESTS=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --tests
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --tests
            ```
        === "Example Collection File"
    
            In my collection YAML file, I would set `true: false` like this:
    
            ```yaml
            collections:
              Marvel Cinematic Universe:
                test: true                  # HERE
                trakt_list: https://trakt.tv/users/jawann2002/lists/marvel-cinematic-universe-movies?sort=rank,asc
                smart_label: release.desc
            ```

??? blank "Debug&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-db`/`--debug`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_DEBUG`<a class="headerlink" href="#debug" title="Permanent link">¶</a>"


    <div id="debug" />Perform a debug test run immediately, bypassing the time to run flag. **This will only run 
    collections with `test: true` in the definition.**

    <hr style="margin: 0px;">

    **Shell Flags:** `-db` or `--debug` (ex. `--debug`)

    **Environment Variable:** `KOMET_DEBUG` (ex. `KOMET_DEBUG=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --debug
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --debug
            ```

??? blank "Trace&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-tr`/`--trace`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_TRACE`<a class="headerlink" href="#trace" title="Permanent link">¶</a>"

    <div id="trace" />Run with extra Trace Debug Logs.

    <hr style="margin: 0px;">

    **Shell Flags:** `-tr` or `--trace` (ex. `--trace`)

    **Environment Variable:** `KOMET_TRACE` (ex. `KOMET_TRACE=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --trace
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --trace
            ```

??? blank "Log Requests&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-lr`/`--log-requests`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_LOG_REQUESTS`<a class="headerlink" href="#log-requests" title="Permanent link">¶</a>"

    <div id="log-requests" />Run with every network request printed to the Logs. **This can potentially have personal 
    information in it.**

    <hr style="margin: 0px;">

    **Shell Flags:** `-lr` or `--log-requests` (ex. `--log-requests`)

    **Environment Variable:** `KOMET_LOG_REQUESTS` (ex. `KOMET_LOG_REQUESTS=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --log-requests
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --log-requests
            ```

??? blank "Timeout&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-ti`/`--timeout`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_TIMEOUT`<a class="headerlink" href="#timeout" title="Permanent link">¶</a>"

    <div id="timeout" />Change the timeout for all non-Plex services (such as TMDb, Radarr, and Trakt). This will default to `180` when not specified and is overwritten by any timeouts mentioned for specific services in the Configuration File.

    <hr style="margin: 0px;">

    **Accepted Values:** Integer Number of Seconds

    **Shell Flags:** `-ti` or `--timeout` (ex. `--timeout 06:00,18:00`)

    **Environment Variable:** `KOMET_TIMEOUT` (ex. `KOMET_TIMEOUT=06:00,18:00`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --timeout 360
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --timeout 360
            ```

??? blank "Collections Only&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-co`/`--collections-only`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_COLLECTIONS_ONLY`<a class="headerlink" href="#collections-only" title="Permanent link">¶</a>"

    <div id="collections-only" />Only run collection YAML files, skip library operations, metadata, overlays, and playlists.

    <hr style="margin: 0px;">

    **Shell Flags:** `-co` or `--collections-only` (ex. `--collections-only`)

    **Environment Variable:** `KOMET_COLLECTIONS_ONLY` (ex. `KOMET_COLLECTIONS_ONLY=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --collections-only
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --collections-only
            ```

??? blank "Metadata Only&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-mo`/`--metadata-only`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_METADATA_ONLY`<a class="headerlink" href="#metadata-only" title="Permanent link">¶</a>"

    <div id="metadata-only" />Only run metadata files, skip library operations, collections, overlays, and playlists.

    <hr style="margin: 0px;">

    **Shell Flags:** `-mo` or `--metadata-only` (ex. `--metadata-only`)

    **Environment Variable:** `KOMET_METADATA_ONLY` (ex. `KOMET_METADATA_ONLY=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --metadata-only
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --metadata-only
            ```

??? blank "Playlists Only&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-po`/`--playlists-only`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_PLAYLISTS_ONLY`<a class="headerlink" href="#playlists-only" title="Permanent link">¶</a>"

    <div id="playlists-only" />Only run playlist YAML files, skip library operations, overlays, collections, and metadata.

    <hr style="margin: 0px;">

    **Shell Flags:** `-po` or `--playlists-only` (ex. `--playlists-only`)

    **Environment Variable:** `KOMET_PLAYLISTS_ONLY` (ex. `KOMET_PLAYLISTS_ONLY=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --playlists-only
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --playlists-only
            ```

??? blank "Operations Only&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-op`/`--operations-only`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_OPERATIONS_ONLY`<a class="headerlink" href="#operations-only" title="Permanent link">¶</a>"

    <div id="operations-only" />Only run library operations skipping collections, metadata, playlists, and overlays.

    <hr style="margin: 0px;">

    **Shell Flags:** `-op` or `--operations-only` (ex. `--operations-only`)

    **Environment Variable:** `KOMET_OPERATIONS_ONLY` (ex. `KOMET_OPERATIONS_ONLY=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --operations-only
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --operations-only
            ```

??? blank "Overlays Only&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-ov`/`--overlays-only`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_OVERLAYS_ONLY`<a class="headerlink" href="#overlays-only" title="Permanent link">¶</a>"

    <div id="overlays-only" />Only run library overlay files skipping collections, metadata, playlists, and operations.

    <hr style="margin: 0px;">

    **Shell Flags:**  `-ov` or `--overlays-only` (ex. `--overlays-only`)

    **Environment Variable:** `KOMET_OVERLAYS_ONLY` (ex. `KOMET_OVERLAYS_ONLY=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --overlays-only
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --overlays-only
            ```

??? blank "Run Collections&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-rc`/`--run-collections`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_RUN_COLLECTIONS`<a class="headerlink" href="#run-collections" title="Permanent link">¶</a>"

    <div id="run-collections" />Perform a collections run immediately to run only the pre-defined collections, bypassing 
    the time to run flag.

    <hr style="margin: 0px;">

    **Accepted Values:** Pipe-separated list of Collection Names to run; the "pipe" character is "|" as shown in the examples below.

    **Shell Flags:** `-rc` or `--run-collections` (ex. `--run-collections "Harry Potter|Star Wars"`)

    **Environment Variable:** `KOMET_RUN_COLLECTIONS` (ex. `KOMET_RUN_COLLECTIONS=Harry Potter|Star Wars`)

    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --run-collections "Harry Potter|Star Wars"
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --run-collections "Harry Potter|Star Wars"
            ```

??? blank "Run Libraries&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-rl`/`--run-libraries`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_RUN_LIBRARIES`<a class="headerlink" href="#run-libraries" title="Permanent link">¶</a>"

    <div id="run-libraries" />Perform a libraries run immediately to run only the pre-defined libraries, bypassing the 
    time to run flag.

    <hr style="margin: 0px;">

    **Accepted Values:** Pipe-separated list of Library Names to run; the "pipe" character is "|" as shown in the examples below.

    **Shell Flags:** `-rl` or `--run-libraries` (ex. `--run-libraries "Movies - 4K|TV Shows - 4K"`)

    **Environment Variable:** `KOMET_RUN_LIBRARIES` (ex. `KOMET_RUN_LIBRARIES=Movies - 4K|TV Shows - 4K`)

    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --run-libraries "Movies - 4K|TV Shows - 4K"
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --run-libraries "Movies - 4K|TV Shows - 4K"
            ```

??? blank "Run Files&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-rf`/`--run-files`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_RUN_FILES`<a class="headerlink" href="#run-files" title="Permanent link">¶</a>"

    <div id="run-files" />Perform a run immediately to run only the pre-defined Collection, Metadata or Playlist files, 
    bypassing the time to run flag. This works for all different paths i.e. `default`, `git`, `url`, `file`, or `repo`.

    ???+ warning
         
         Do not use this to run Overlay files, as Overlay files must run all together or not at all due to their nature.

    <hr style="margin: 0px;">

    **Accepted Values:** Pipe-separated list of Collection, Metadata or Playlist Filenames to run; the "pipe" character is "|" as shown in the examples below.

    **Shell Flags:** `-rf` or `--run-files` (ex. `--run-files "Movies.yml|MovieCharts"`)

    **Environment Variable:** `KOMET_RUN_FILES` (ex. `KOMET_RUN_FILES=Movies.yml|MovieCharts`)

    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --run-files "Movies.yml|MovieCharts"
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --run-files "Movies.yml|MovieCharts"
            ```

??? blank "Ignore Schedules&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-is`/`--ignore-schedules`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_IGNORE_SCHEDULES`<a class="headerlink" href="#ignore-schedules" title="Permanent link">¶</a>"

    <div id="ignore-schedules" />Ignore all schedules for the run. Range Scheduled collections (such as Christmas 
    movies) will still be ignored.

    <hr style="margin: 0px;">

    **Shell Flags:** `-is` or `--ignore-schedules` (ex. `--ignore-schedules`)

    **Environment Variable:** `KOMET_IGNORE_SCHEDULES` (ex. `KOMET_IGNORE_SCHEDULES=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --ignore-schedules
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --ignore-schedules
            ```

??? blank "Ignore Ghost&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-ig`/`--ignore-ghost`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_IGNORE_GHOST`<a class="headerlink" href="#ignore-ghost" title="Permanent link">¶</a>"

    <div id="ignore-ghost" />Ignore all ghost logging for the run. A ghost log is what's printed to the console to show 
    progress during steps.

    <hr style="margin: 0px;">

    **Shell Flags:** `-ig` or `--ignore-ghost` (ex. `--ignore-ghost`)

    **Environment Variable:** `KOMET_IGNORE_GHOST` (ex. `KOMET_IGNORE_GHOST=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --ignore-ghost
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --ignore-ghost
            ```

??? blank "Delete Collections&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-dc`/`--delete-collections`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_DELETE_COLLECTIONS`<a class="headerlink" href="#delete-collections" title="Permanent link">¶</a>"

    <div id="delete-collections" />Delete all collections in a Library prior to running collections/operations.

    ???+ warning
         
        You will lose **all** collections in the library - this will delete all collections, including ones not created 
        or maintained by Komet.

    <hr style="margin: 0px;">

    **Shell Flags:** `-dc` or `--delete-collections` (ex. `--delete-collections`)

    **Environment Variable:** `KOMET_DELETE_COLLECTIONS` (ex. `KOMET_DELETE_COLLECTIONS=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --delete-collections
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --delete-collections
            ```

??? blank "Delete Labels&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-dl`/`--delete-labels`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_DELETE_LABELS`<a class="headerlink" href="#delete-labels" title="Permanent link">¶</a>"

    <div id="delete-labels" />Delete all labels on every item in a Library prior to running collections/operations.

    ???+ warning
    
        To preserve functionality of Komet, this will **not** remove the Overlay label, which is required for Komet to know 
        which items have Overlays applied.
    
        This will impact any [Smart Label Collections](../files/builders/smart.md#smart-label) that you have in your 
        library.
    
        We do not recommend using this on a regular basis if you also use any operations or collections that update 
        labels, as you are effectively deleting and adding labels on each run.

    <hr style="margin: 0px;">

    **Shell Flags:** `-dl` or `--delete-labels` (ex. `--delete-labels`)

    **Environment Variable:** `KOMET_DELETE_LABELS` (ex. `KOMET_DELETE_LABELS=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --delete-labels
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --delete-labels
            ```

??? blank "Resume Run&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-re`/`--resume`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_RESUME`<a class="headerlink" href="#resume" title="Permanent link">¶</a>"

    <div id="resume" />Perform a resume run immediately resuming from the first instance of the specified collection, 
    bypassing the time to run flag.

    <hr style="margin: 0px;">

    **Shell Flags:** `-re` or `--resume` (ex. `--resume "Star Wars"`)

    **Environment Variable:** `KOMET_RESUME` (ex. `KOMET_RESUME=Star Wars`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --resume "Star Wars"
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --resume "Star Wars"
            ```

??? blank "No Countdown&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-nc`/`--no-countdown`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_NO_COUNTDOWN`<a class="headerlink" href="#no-countdown" title="Permanent link">¶</a>"

    <div id="no-countdown" />Run without displaying a countdown to the next scheduled run.

    <hr style="margin: 0px;">

    **Shell Flags:** `-nc` or `--no-countdown` (ex. `--no-countdown`)

    **Environment Variable:** `KOMET_NO_COUNTDOWN` (ex. `KOMET_NO_COUNTDOWN=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --no-countdown
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --no-countdown
            ```

??? blank "No Missing&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-nm`/`--no-missing`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_NO_MISSING`<a class="headerlink" href="#no-missing" title="Permanent link">¶</a>"

    <div id="no-missing" />Run without utilizing the missing movie/show functions.

    <hr style="margin: 0px;">

    **Shell Flags:** `-nm` or `--no-missing` (ex. `--no-missing`)

    **Environment Variable:** `KOMET_NO_MISSING` (ex. `KOMET_NO_MISSING=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --no-missing
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --no-missing
            ```

??? blank "No Report&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-nr`/`--no-report`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_NO_REPORT`<a class="headerlink" href="#no-report" title="Permanent link">¶</a>"

    <div id="no-report" />Run without saving the report.

    <hr style="margin: 0px;">

    **Shell Flags:**  `-nr` or `--no-report` (ex. `--no-report`)

    **Environment Variable:** `KOMET_NO_REPORT` (ex. `KOMET_NO_REPORT=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --no-report
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --no-report
            ```

??? blank "Read Only Config&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-ro`/`--read-only-config`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_READ_ONLY_CONFIG`<a class="headerlink" href="#read-only-config" title="Permanent link">¶</a>"

    <div id="read-only-config" />Run without writing to the configuration file.

    <hr style="margin: 0px;">

    **Shell Flags:**  `-ro` or `--read-only-config` (ex. `--read-only-config`)

    **Environment Variable:** `KOMET_READ_ONLY_CONFIG` (ex. `KOMET_READ_ONLY_CONFIG=true`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --read-only-config
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --read-only-config
            ```

??? blank "Divider Character&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-d`/`--divider`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_DIVIDER`<a class="headerlink" href="#divider" title="Permanent link">¶</a>"

    <div id="divider" />Change the terminal output divider character. Will default to `=` if not specified.

    <hr style="margin: 0px;">

    **Accepted Values:** Any character

    **Shell Flags:** `-d` or `--divider` (ex. `--divider *`)

    **Environment Variable:** `KOMET_DIVIDER` (ex. `KOMET_DIVIDER=*`)
    
    !!! example
        === "Local Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --divider *
            python plex_meta_manager.py --divider *
            ```
        === "Docker Environment"
            ```
            ```

??? blank "Screen Width&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`-w`/`--width`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_WIDTH`<a class="headerlink" href="#width" title="Permanent link">¶</a>"

    <div id="width" />Change the terminal output width. Will default to `100` if not specified.

    <hr style="margin: 0px;">

    **Accepted Values:** Integer between 90 and 300

    **Shell Flags:** `-w` or `--width` (ex. `--width 150`)

    **Environment Variable:** `KOMET_WIDTH` (ex. `KOMET_WIDTH=150`)
    
    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --width 150
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --width 150
            ```

??? blank "Config Secrets&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`--komet-***`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`KOMET_***`<a class="headerlink" href="#komet-vars" title="Permanent link">¶</a>"

    <div id="komet-vars" />All Run Commands that are in the format `--komet-***` and Environment Variables that are in the 
    format `KOMET_***`, where `***` is the name you want to call the variable, will be loaded in as Config Secrets.
    
    These Config Secrets can be loaded into the config by placing `<<***>>` in any field in the config, where `***` is 
    whatever name you called the variable.  

    <hr style="margin: 0px;">

    **Shell Flags:** `--komet-***` (ex. `--komet-mysecret 123456789`)

    **Environment Variable:** `KOMET_***` (ex. `KOMET_MYSECRET=123456789`)

    !!! example
        === "Local Environment"
            ```
            python plex_meta_manager.py --komet-mysecret 123456789
            ```
        === "Docker Environment"
            ```
            docker run -it -v "X:\Media\Komet\config:/config:rw" meisnate12/komet --komet-mysecret 123456789
            ```
    
        **Example Config Usage:**
    
        ```yaml
        tmdb:
          apikey: <<mysecret>>
        ```
