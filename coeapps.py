#!/usr/bin/env python3

import argparse
import csv
from datetime import datetime, timedelta
import logging

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


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


def new_parser(**kwargs) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--start",
        help="Start date, in YYYY-M-D format. Default 2013-11-18.",
        default="2013-11-18",
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