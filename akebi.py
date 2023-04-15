#!/usr/bin/env python
# -*- coding:utf-8 -*-

import platform
import argparse
import datetime
import distro
import subprocess
import psutil

from cpuinfo import get_cpu_info


############################################
#                                          #
#        Let's Grab the informations       #
#                                          #
############################################

#
# Used system information
#

host_system = platform.system()

#
# CPU information
#

cpuinfo_all = get_cpu_info()
cpu_model = cpuinfo_all['brand_raw']
cpu_cores = cpuinfo_all['count']
cpu_freq = cpuinfo_all['hz_advertised'][0]
cpu_freq_ghz = round(cpu_freq / 10**9, 1)
cpu_usage_percent = psutil.cpu_percent()

#
# Memory info
#

# Memory infor in byte
total_mem = psutil.virtual_memory().total
free_mem = psutil.virtual_memory().free

# Memory infor in megabyte
total_mem_mb = round((total_mem / (1024**2)))
free_mem_mb = round((free_mem / (1024**2)))

#
# Machine Information
#

boot_time = psutil.boot_time()
boot_time_dt = datetime.datetime.fromtimestamp(boot_time)
info_uptime = datetime.datetime.now() - boot_time_dt

# Format the system uptime as days, hours, minutes, and seconds
uptime_str = str(info_uptime).split('.')[0]
uptime_days = info_uptime.days
uptime_hours = info_uptime.seconds // 3600
uptime_minutes = (info_uptime.seconds // 60) % 60
uptime_seconds = info_uptime.seconds % 60

# machine_uptime = uptime_days , " days, " , uptime_hours , "hours, " , uptime_minutes , "minutes"
if uptime_days > 0:
    machine_uptime = f"{uptime_days} days, {uptime_hours} hours, {uptime_minutes} minutes"
else:
    machine_uptime = f"{uptime_hours} hours, {uptime_minutes} minutes"

#
# System Information
#

# Installed OS Info
if host_system == "Darwin":
    mac_version = platform.mac_ver()[0]
    installed_os = f" macOS {mac_version}"
elif host_system == "Linux":
    dist_name = distro.name()
    dist_version = distro.version()
    installed_os = f"{dist_name} {dist_version}"
elif host_system == "Windows":
    win_version = platform.system() + ' ' + platform.release()
    nstalled_os = f"{win_version}"
else:
    nstalled_os = "Unknown"

# Installed Kernel Info
kernel_release = platform.release()
installed_kernel = f"{host_system} {kernel_release}"
############################################
#                                          #
#      Let's define needed functions       #
#                                          #
############################################

#
# Main function
#

def main_info():
    print("==========================================================")
    print("                Akebi - System Information                ")
    print("==========================================================")
    print(f"CPU Model Name: {cpu_model}")
    print(f"CPU Core(s)   : {cpu_cores} Core(s)")
    print(f"CPU Usage     : {cpu_usage_percent}%")
    print(f"CPU Freuency  : {cpu_freq_ghz} GHz")
    print(f"Total Memory  : {total_mem_mb} MB")
    print(f"Free Memory   : {free_mem_mb} MB")
    print(f"Installed OS  : {installed_os}")
    print(f"Kernel        : {installed_kernel}")
    print(f"Uptime        : {machine_uptime}")
    print("==========================================================")

def mem_info():
    print("====-------")
    print("==========================================================")
    print("                Akebi - Memory Information                ")
    print("==========================================================")
    print(f"Total Memory  : {total_mem_mb} MB")
    print(f"Free Memory   : {free_mem_mb} MB")
    print("==========================================================")

def display_info():
    print("====-------")
    print("==========================================================")
    print("                Akebi - Display Information               ")
    print("==========================================================")
    print(f"CPU Model Name: {cpu_model}")
    print("==========================================================")

############################################
#                                          #
#           Handle user arguments          #
#                                          #
############################################

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments to the parser
parser.add_argument("-d", "--display", help="Display information", action="store_true")
parser.add_argument("-m", "--memory", help="Show memory information", action="store_true")

# Parse the arguments
args = parser.parse_args()

# Check the arguments and call the appropriate function
if args.memory:
    mem_info()
elif args.display:
    display_info()
else:
    main_info()
