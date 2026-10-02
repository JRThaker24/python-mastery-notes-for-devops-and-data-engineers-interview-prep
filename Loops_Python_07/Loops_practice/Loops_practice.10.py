# Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, 
# starting from 1 second, but stops after 5 retries.

import time

wait_time = 1
attempts = 0
max_reties = 5

while attempts < max_reties:
    print(f"Attempt is {attempts + 1}, waiting time is {wait_time} ")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
    