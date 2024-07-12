#!/usr/bin/env python3

import argparse
import csv
from datetime import datetime
import logging

from dateutil.parser import parse as parse_date
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


DAY_FORMAT = "%Y%m%d"


def get_current_last(args):
    if args.date:
        start = end = args.date
    else:
        start = args.start
        end = args.end

    current = parse_date(start)
    if end:
        last = parse_date(end)
    else:
        last = datetime.now()
    return current, last


def configure_logging(filename, level="WARN"):
    """
    Accept filename (file-like object),
    optional level (str, default WARN).
    Configure logging.
    """
    numeric_level = getattr(logging, level.upper())

    logging.basicConfig(
        filename=filename,
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=numeric_level,
        datefmt="%Y%m%dT%H:%M:%S",
    )


def new_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--start",
        help="Start date, in YYYY-M-D format. Default 2013-11-19.",
        default="2013-11-19",
    )
    parser.add_argument(
        "-e",
        "--end",
        help="End date, in YYYY-M-D format. Default today.",
        default=None,
    )
    parser.add_argument(
        "-l",
        "--log-level",
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="""Log at level LOG_LEVEL.
        default: INFO.
        """,
        default="INFO",
    )
    parser.add_argument(
        "-d",
        "--date",
        help="A single date to fetch. Syntactic sugar for -s DATE -e DATE.",
    )

    return parser


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--remote-debugging-pipe")
    options.add_argument("--headless=new")
    return webdriver.Chrome(options=options)


def row_as_list_of_text(row, skip_first_n=False):
    # The first column is a checkbox, which we do not need or want.
    cells = row.find_elements(By.XPATH, ".//td")
    if skip_first_n:
        cells = cells[skip_first_n:]
    return [cell.text for cell in cells]


def write_file(rows, date, prefix, header):
    output = f"{prefix}-{date}.csv"
    with open(output, "w", encoding="utf8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)
