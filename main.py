from __future__ import print_function

import sys

import psutil


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def check():
    batt = psutil.sensors_battery()
    if batt.power_plugged:
        print('is_charge')

def main():
    #check()
    if not hasattr(psutil, "sensors_battery"):
        return sys.exit("platform not supported")
    batt = psutil.sensors_battery()
    if batt is None:
        return sys.exit("no battery is installed")

    print("charge:     %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        print(
            "status:     %s"
            % ("charging" if batt.percent < 100 else "fully charged")
        )
        print("plugged in: yes")
        print(batt.power_plugged)
    else:
        print("left:       %s" % secs2hours(batt.secsleft))
        print("status:     %s" % "discharging")
        print("plugged in: no")


if __name__ == '__main__':
    main()
