import psutil
for p in psutil.process_iter():
    proc={process_iter.pid},{process_iter.name}
    print (proc)
