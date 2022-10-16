
import time
from ppadb.client import Client as AdbClient
import os

path_file = ('cd Pass-to-E.V.A.')
start_file = ('python main.py')
swipe_down = '882 35 882 400 10'  # x y
swipe_up = '882 1900 882 35 10'
tap_vpn = '336 541'
tap_wifi = '759 562'
check_file = ('cat all_info.txt')
text = ('1')
on_sshd = 'sshd'

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

def search_file():
    device.shell(f'input text "{path_file}"')
    device.shell('input keyevent 66')
    time.sleep(1)
    device.shell(f'input text "{start_file}"')
    device.shell('input keyevent 66')

def on_and_off_vpn():
    device.shell(f'input swipe {swipe_down}')
    count = 0
    while count != 5:
        time.sleep(1)
        device.shell(f'input tap {tap_vpn}')
        device.shell(f'input tap {tap_vpn}')
        device.shell(f'input swipe {swipe_up}')
        time.sleep(2)
        device.shell(f'input text "{text}"')
        device.shell('input keyevent 66')
        device.shell(f'input swipe {swipe_down}')
        time.sleep(3)
        count += 1

def end():
    device.shell(f'input swipe {swipe_up}')
    time.sleep(1)
    device.shell(f'input text "{check_file}"')
    device.shell('input keyevent 66')
    device.shell(f'input swipe {swipe_down}')
    device.shell(f'input tap {tap_wifi}')
    device.shell(f'input tap {tap_vpn}')
    time.sleep(10)
    device.shell(f'input swipe {swipe_up}')
    time.sleep(5)
    device.shell(f'input text "{on_sshd}"')
    device.shell('input keyevent 66')
    time.sleep(3)
    os.system('ansible all -m ping')
    os.system('ansible all -m fetch -a "src=/data/data/com.termux/files/home/Pass-to-E.V.A./all_info.txt dest=/home/nikita/ flat=yes" ')

def main():
    search_file()
    time.sleep(4)
    start_time = time.monotonic()
    on_and_off_vpn()
    print(f'spend{time.monotonic() - start_time}')
    time.sleep(1)
    end()

if __name__ == '__main__':
    device, client = connect()
    main()

