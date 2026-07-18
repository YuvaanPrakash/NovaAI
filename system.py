"""
system.py

System Information Module
Nova AI
"""

import os
import platform
import socket
import psutil


class System:

    # ----------------------------
    # Operating System
    # ----------------------------

    def operating_system(self):

        return platform.system()

    # ----------------------------
    # OS Version
    # ----------------------------

    def os_version(self):

        return platform.version()

    # ----------------------------
    # Machine
    # ----------------------------

    def machine(self):

        return platform.machine()

    # ----------------------------
    # Processor
    # ----------------------------

    def processor(self):

        return platform.processor()

    # ----------------------------
    # Python Version
    # ----------------------------

    def python_version(self):

        return platform.python_version()

    # ----------------------------
    # Host Name
    # ----------------------------

    def hostname(self):

        return socket.gethostname()

    # ----------------------------
    # IP Address
    # ----------------------------

    def ip_address(self):

        try:

            return socket.gethostbyname(socket.gethostname())

        except:

            return "Unavailable"

    # ----------------------------
    # CPU Usage
    # ----------------------------

    def cpu_usage(self):

        return f"{psutil.cpu_percent(interval=1)} %"

    # ----------------------------
    # RAM Usage
    # ----------------------------

    def ram_usage(self):

        memory = psutil.virtual_memory()

        return f"{memory.percent} %"

    # ----------------------------
    # RAM Total
    # ----------------------------

    def total_ram(self):

        ram = psutil.virtual_memory().total / (1024 ** 3)

        return f"{ram:.2f} GB"

    # ----------------------------
    # Disk Usage
    # ----------------------------

    def disk_usage(self):

        disk = psutil.disk_usage('/')

        return f"{disk.percent} %"

    # ----------------------------
    # Battery
    # ----------------------------

    def battery(self):

        battery = psutil.sensors_battery()

        if battery is None:

            return "Battery Not Available"

        return f"{battery.percent} %"

    # ----------------------------
    # System Summary
    # ----------------------------

    def summary(self):

        return f"""
=========== SYSTEM INFO ===========

Operating System : {self.operating_system()}

OS Version       : {self.os_version()}

Machine          : {self.machine()}

Processor        : {self.processor()}

Python Version   : {self.python_version()}

Host Name        : {self.hostname()}

IP Address       : {self.ip_address()}

CPU Usage        : {self.cpu_usage()}

RAM Usage        : {self.ram_usage()}

Total RAM        : {self.total_ram()}

Disk Usage       : {self.disk_usage()}

Battery          : {self.battery()}

===================================
"""


system = System()


if __name__ == "__main__":

    while True:

        print("\n====== SYSTEM ======")

        print("1. Summary")

        print("2. CPU")

        print("3. RAM")

        print("4. Disk")

        print("5. Battery")

        print("6. Processor")

        print("7. Python Version")

        print("8. Exit")

        choice = input("\nChoice : ")

        if choice == "1":

            print(system.summary())

        elif choice == "2":

            print(system.cpu_usage())

        elif choice == "3":

            print(system.ram_usage())

        elif choice == "4":

            print(system.disk_usage())

        elif choice == "5":

            print(system.battery())

        elif choice == "6":

            print(system.processor())

        elif choice == "7":

            print(system.python_version())

        elif choice == "8":

            break

        else:

            print("Invalid Choice")