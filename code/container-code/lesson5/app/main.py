import time
import math
from fastapi import FastAPI
from multiprocessing import cpu_count
from multiprocessing import Process

app = FastAPI()

@app.get('/')
def get_root():
    return "Hello World!"

def runner(x):
    while True:
        x * x

# Referenced and modified from https://qxf2.com/blog/generate-cpu-load/
def generate_load(utilization):
    interval = 30

    start_time = time.time()
    for i in range(0,int(interval)):
        print("About to do some arithmetic")
        while time.time()-start_time < utilization/100.0:
            a = math.sqrt(64*64*64*64*64)
        print(str(i) + ". About to sleep")
        time.sleep(1-utilization/100.0)
        start_time += 1

@app.get('/intense/{utilization}')
def get_intense(utilization: int):
    start_time = time.time()
    processes = []
    for _ in range (cpu_count()):
        p = Process(target = generate_load, args=(utilization,))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

    end_time = time.time()

    return f"Ran for {end_time - start_time}s"