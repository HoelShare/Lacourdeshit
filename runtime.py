import time

start_time = time.time()

def get_runtime():
    global start_time
    return time.time() - start_time
