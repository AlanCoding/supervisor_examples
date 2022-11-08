import os
import sys
import time


sleep_time = int(os.getenv('SLEEP_TIME', 3))

print(f'Going to sleep for {sleep_time} seconds')

time.sleep(sleep_time)

print('Done sleeping, will error now')

sys.exit(2)
