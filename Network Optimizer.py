import subprocess
import time
import ctypes
import platform

def set_mtu(interface, mtu_size):
    subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'subinterface', interface, 'mtu={}'.format(mtu_size)], capture_output=True, text=True)
    print("MTU size changed for", interface)

def flush_dns():
    subprocess.run(['ipconfig', '/flushdns'], capture_output=True, text=True)

def set_window_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def main():
    if platform.system() != 'Windows':
        print("Incompatible OS")
        time.sleep(10)
        return
    
    set_window_title("Network optimizer")
    set_mtu("Wi-Fi", 1472)
    set_mtu("Ethernet", 1472)

    while True:
        flush_dns()
        print("DNS flushed.")
        time.sleep(30)

if __name__ == '__main__':
    main()
