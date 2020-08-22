#!/usr/bin/env python

import json
import sys

from gigamonkeys.spreadsheets import spreadsheets

spreadsheet_id = sys.argv[1]
ranges = sys.argv[2:]

data = spreadsheets().get(spreadsheet_id, include_grid_data=bool(ranges), ranges=ranges)

json.dump(data, sys.stdout, indent=2)
