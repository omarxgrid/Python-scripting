import argparse
import platform
import psutil
import os
import socket


def get_distro_info():
    return platform.linux_distribution()


def get_memory_info():
    mem = psutil.virtual_memory()
    return {'total': mem.total, 'used': mem.used, 'free': mem.free}


def get_cpu_info():
    return {
        'model': platform.processor(),
        'cores': psutil.cpu_count(logical=False),
        'speed': psutil.cpu_freq().current
    }


def get_current_user():
    return os.getlogin()


def get_load_average():
    return os.getloadavg()


def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


parser = argparse.ArgumentParser(description='Get system information')
parser.add_argument('-d', '--distro', action='store_true', help='Get distribution info')
parser.add_argument('-m', '--memory', action='store_true', help='Get memory info')
parser.add_argument('-c', '--cpu', action='store_true', help='Get CPU info')
parser.add_argument('-u', '--user', action='store_true', help='Get current user info')
parser.add_argument('-l', '--load', action='store_true', help='Get system load average')
parser.add_argument('-i', '--ip', action='store_true', help='Get IP address')

args = parser.parse_args()

if args.distro:
    print('Distribution Info:', get_distro_info())

if args.memory:
    print('Memory Info:', get_memory_info())

if args.cpu:
    print('CPU Info:', get_cpu_info())

if args.user:
    print('Current User:', get_current_user())

if args.load:
    print('Load Average:', get_load_average())

if args.ip:
    print('IP Address:', get_ip_address())
