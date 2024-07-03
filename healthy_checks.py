import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print(free)
    return free > 20

def check_cpu_usage():
    cu = psutil.cpu_percent(1)
    print(cu)
    return cu < 75

if check_disk_usage('/') and check_cpu_usage():
    print("Everythign is OK!")
else:
    print("ERROR!")
    
