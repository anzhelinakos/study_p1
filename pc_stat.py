import psutil
import datetime


def get_boottime_info():
    boottime=psutil.boot_time()
    info = datetime.datetime.fromtimestamp(boottime).strftime("%Y-%m-%d %H:%M:%S")
    info1=(f"\nLast boot of this PC was {info}\n")
    return info1
def get_cputime_info():
    cputime = psutil.cpu_times()
    info = f"Current values of system CPU times for:\n   -user is {cputime.user} s; \n   -nice is {cputime.nice} s; \n   -system is {cputime.system} s; \n   -idle is {cputime.idle} s.\n"
    return info
def get_cpupercent_info():
    cpupercent = psutil.cpu_percent()
    info = f"CPU utilization is {cpupercent} %\n"
    return info
def get_cpucount_info():
    cpucount=psutil.cpu_count()
    info=f"Number of logical CPUs is {cpucount}\n"
    return info
def get_cpustats_info():
    cpustats=psutil.cpu_stats()
    info = f"CPU statts is {cpustats}"
    return info
def get_cpufreq_info():
    cpufreq=psutil.cpu_freq()
    info=f"Min CPU frequency = {cpufreq.min}, Max CPU frequency = {cpufreq.max}\n"
    return info
def get_virtualmemory_info():
    virtualmemory=psutil.virtual_memory()
    info=f"System memory usage:\n    -total: {round(virtualmemory.total/(2**30),3)} Gb\n    -available: {round(virtualmemory.available/(2**30),3)} Gb\n    -used: {round(virtualmemory.used/(2**30),3)} Gb\n    -free: {round(virtualmemory.free/(2**30),3)} Gb\n    -active: {round(virtualmemory.active/(2**30),3)} Gb\n    -inactive: {round(virtualmemory.inactive/(2**30),3)} Gb\n"
    return info
def get_diskpartitions_info():
    diskpartitions=psutil.disk_partitions()
    info=f"Disk parts is {diskpartitions}"
    return info
def get_netiocounters_info():
    netinfocounters=psutil.net_io_counters()
    info=f"Network statistic is:\n   - sent  {round(netinfocounters.bytes_sent/(2**30),3)} Gb\n   - recived {round(netinfocounters.bytes_recv/(2**30),3)} Gb\n"
    return info



boottime=get_boottime_info()
cputime_info=get_cputime_info()
cpupercent_info=get_cpupercent_info()
cpucount_info=get_cpucount_info()
cpustats_info=get_cpustats_info()
cpufreq_info=get_cpufreq_info()
virtualmemory_info=get_virtualmemory_info()
diskpartitions_info=get_diskpartitions_info()
netiocounters=get_netiocounters_info()



print(boottime)
print(cputime_info)
print(cpupercent_info)
print(cpucount_info)
print(cpufreq_info)
print(virtualmemory_info)
print(netiocounters)

print("Process information:")
for proc in psutil.process_iter():
    p=f"pid={proc.pid}, Name of process is  {proc.name()},   Current status: {proc.status()}"
    print (p)


