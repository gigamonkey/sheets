#!/usr/bin/env python

import json
import sys

from gigamonkeys.spreadsheets import spreadsheets

json.dump(spreadsheets().get(sys.argv[1], include_grid_data = len(sys.argv) > 2, ranges = sys.argv[2:]), sys.stdout, indent=2)
