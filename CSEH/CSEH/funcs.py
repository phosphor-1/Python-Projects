# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:26:08 2022

@author: isaac
"""

import socket
import os, platform
import psutil
import shutil

def get_platform():
    return platform.system()
    print(get_platform())

def enum_hostname():
   print("Hostname: ", socket.gethostname())
        
def enum_cpu():
    print("CPU Usage: ", psutil.cpu_percent(), "% used")

def enum_disk():
    root_dir = "/"
    if platform.system == "Windows":
        root_dir = "C:/"
    total, used, free = shutil.disk_usage(root_dir)
    print("Disk Usage: ", round((used/total)*100), "% used")

def enum_mem():
    mem = psutil.virtual_memory()
    print("Memory Usage: ", mem.percent, "% used")



def enum_host():
    enum_hostname()
    enum_cpu()
    enum_mem()
    enum_disk()

enum_host()
    
    

        


