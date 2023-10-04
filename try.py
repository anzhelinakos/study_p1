import psutil
import datetime


def get_boottime_info():
    boottime_info = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return boottime_info
   

def get_cputime_info():
    cputime_info = psutil.cpu_times()
    return cputime_info, cpupercent_info


def get_cpupercent_info():
    cpupercent_info = psutil.cpu_percent() 
    return cpupercent_info


def get_cpucount_info():
    cpucount_info=psutil.cpu_count()
    return cpucount_info


def get_cpustats_info():
    cpustats_info=psutil.cpu_stats()
    return cpustats_info


def get_cpufreq_info():
    cpufreq_info=psutil.cpu_freq()
    return cpufreq_info


def get_virtualmemory_info():
    virtualmemory_info=psutil.virtual_memory()
    return virtualmemory_info


def get_diskpartitions_info():
    diskpartitions_info=psutil.disk_partitions()
    return diskpartitions_info


def get_netiocounters_info():
    netinfocounters_info=psutil.net_io_counters()
    return netinfocounters_info

def get_processes_info():
    for proc in psutil.process_iter():
        processes_info=[{proc.pid()},{proc.name()},{proc.status()}]
    return processes_info

def show_boottime_info():
    boottime_info_edit=(f"\nLast boot of this PC was {boottime_info}\n")
    print (boottime_info_edit)


def show_cputime_info():
    cputime_info_edit = f"Current values of system CPU times for:\n   -user is {cputime_info.user} s; \n   -nice is {cputime_info.nice} s; \n   -system is {cputime_info.system} s; \n   -idle is {cputime_info.idle} s.\n"
    print (cputime_info_edit)


def show_cpupercent_info():
    cpupercent_info_edit = f"CPU utilization is {cpupercent_info} %\n"
    print (cpupercent_info_edit)


def show_cpucount_info():
    cpucount_info_edit=f"Number of logical CPUs is {cpucount_info}\n"
    print (cpucount_info_edit)


def show_cpustats_info():
    cpustats_info_edit = f"CPU statts is {cpustats_info}"
    print (cpustats_info_edit)


def show_cpufreq_info():
    cpufreq_info_edit=f"Min CPU frequency = {cpufreq_info.min}, Max CPU frequency = {cpufreq_info.max}\n"
    print (cpufreq_info_edit)


def show_virtualmemory_info():
    virtualmemory_info_edit=f"System memory usage:\n    -total: {round(virtualmemory_info.total/(2**30),3)} Gb\n    -available: {round(virtualmemory_info.available/(2**30),3)} Gb\n    -used: {round(virtualmemory_info.used/(2**30),3)} Gb\n    -free: {round(virtualmemory_info.free/(2**30),3)} Gb\n    -active: {round(virtualmemory_info.active/(2**30),3)} Gb\n    -inactive: {round(virtualmemory_info.inactive/(2**30),3)} Gb\n"
    print (virtualmemory_info_edit)


def show_diskpartitions_info():
    diskpartitions_info_edit=f"Disk parts is {diskpartitions_info}"
    print (diskpartitions_info_edit)


def show_netiocounters_info():
    netinfocounters_info_edit=f"Network statistic is:\n   - sent  {round(netinfocounters_info.bytes_sent/(2**30),3)} Gb\n   - recived {round(netinfocounters_info.bytes_recv/(2**30),3)} Gb\n"
    print (netinfocounters_info_edit)


def show_processes_info():
    for element in processes_info
        processes_info_edit=f"pid={processes_info.pid}, Name of process is  {processes_info.name()},   Current status: {processes_info.status()}"
        print (processes_info_edit)


def main():
    cpu_info=

if _name_ == '_main_':
    main()

