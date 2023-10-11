import psutil
import datetime

def get_processes_info():
    info = {}
    for proc in psutil.process_iter():
        if proc.pid is not None:
            info = {"pid": {proc.pid},"name":{proc.name()}}



print(get_processes_info())




