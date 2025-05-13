#!/usr/bin/env python3

import time
from datetime import datetime

# Number of seconds (including milliseconds) since January 1, 1970 at midnight
timestamp = time.time()

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")

current_date = datetime.today()
formatted_date = current_date.strftime("%b %d %Y")

print(formatted_date)
