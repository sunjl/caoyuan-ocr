# _*_ coding: utf-8 _*_

import datetime

import pytz

import re


def parse_date(date_str, timezone='Asia/Shanghai'):
    tz = pytz.timezone(timezone)
    converted_date = None
    if date_str:
        replaced_date_str = date_str.replace(u'年', '-').replace(u'月', '-').replace(u'日', '').replace('/', '-')
        pattern = re.compile("(\d+)-(\d+)-(\d+)")
        matcher = pattern.search(replaced_date_str)
        if matcher:
            words = matcher.group().split('-')
            converted_date = tz.localize(datetime.datetime(int(words[0]), int(words[1]), int(words[2])))
        return converted_date


def get_birth_date(age, timezone='Asia/Shanghai'):
    tz = pytz.timezone(timezone)
    try:
        age_int = int(age)
        today = datetime.datetime.today()
        return tz.localize(datetime.datetime(today.year - age_int, 1, 1))
    except ValueError:
        return None
