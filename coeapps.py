#!/usr/bin/env python3

import csv
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--remote-debugging-pipe")
    #options.add_argument("--headless=new")
    return webdriver.Chrome(options=options)


def write_warnings(date, message):
    full_message = f"{date}: {message}\n"
    print(full_message)
    with open("warnings.txt", "a", encoding="utf8") as warnings:
        warnings.write(full_message)

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

