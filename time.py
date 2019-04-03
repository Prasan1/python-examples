#!/bin/usr/env python

import time

start_time = time.time()

for i in range(1000000):
    print(i)

end_time = time.time()

total_time = (end_time - start_time)

print(total_time)
