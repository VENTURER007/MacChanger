import subprocess

interface = input("interface > ")
new_mac = input("new mac > ")

print("[+]Changing mac address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " +interface + " hw ether " + new_mac,shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig "+interface, shell=True)