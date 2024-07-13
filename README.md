# City of Eugene Police, Fire, and EMS Call Logs

The city of Eugene, Oregon makes its police dispatch logs available at
https://coeapps.eugene-or.gov/EPDDispatchLog/Search.
Similarly, its Fire & EMS CAD calls are available at 
https://coeapps.eugene-or.gov/ruralfirecad.
Data goes back to November 19, 2013.

Sadly, there is no public API for these services,
and the ability to customize a search is quite limited. 
The EPD page also limits requests to 250 calls per page.

This project automates scraping these two pages.
Output is to CSV files, one per day of records.

You can download the zipped CSV files from the releases page.

## Setup

If you want to run the code yourself, be warned that it is a slow process.
At a few seconds per day of records, expect around a full day to scrape
the entire dataset.

You will need:

* python3
* chrome browser

Preferably use a virtual environment:

```
    python3 -m venv venv
    . venv/bin/activate
```

Python package requirements are minimal:

```
    pip install -r requirements.txt
```

## Running

### EPD

```
    usage: fetch-epd-dispatch-log [-h] [-s START] [-e END]
                                  [-l {NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                                  [-d DATE] [-D] [--no-recurse]

    options:
      -h, --help            show this help message and exit
      -s START, --start START
                            Start date, in any reasonable format, as understood by
                            dateutil. Default 2013-11-19.
      -e END, --end END     End date, in any reasonable format, as understood by
                            dateutil. Default today.
      -d DATE, --date DATE  A single date to fetch. Syntactic sugar for -s DATE -e
                            DATE.
      -l {NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL}
                            Log at level LOG_LEVEL. default: INFO.
      -D, --dry-run         Do not fetch results, but merely print filenames which
                            would be saved to
      --no-recurse          Do not recurse on result-limited pages.
```

### Fire and EMS

```
    usage: fetch-fire-ems-cad-calls [-h] [-s START] [-e END]
                                    [-l {NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                                    [-d DATE] [-D]

    options:
      -h, --help            show this help message and exit
      -s START, --start START
                            Start date, in any reasonable format, as understood by
                            dateutil. Default 2013-11-19.
      -e END, --end END     End date, in any reasonable format, as understood by
                            dateutil. Default today.
      -d DATE, --date DATE  A single date to fetch. Syntactic sugar for -s DATE -e
                            DATE.
      -l {NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL}
                            Log at level LOG_LEVEL. default: INFO.
      -D, --dry-run         Do not fetch results, but merely print filenames which
                            would be saved to
```
