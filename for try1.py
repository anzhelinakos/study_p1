import psutil
import datetime


def record_info(func):
    file_name = "info_record.log"
    cpupercent_string = "{0} ({1})\n"

    def record_info_worker():
        res = func()
        with open(file_name, "a") as cpupercent_file:
            cpupercent_file.write(cpupercent_string.format(res, datetime.datetime.now()))
        return res
    return record_info_worker

@record_info
def get_cpupercent_info():
    cpupercent_info = psutil.cpu_percent()
    return cpupercent_info

a=get_cpupercent_info()
print(a)


