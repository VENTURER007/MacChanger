import subprocess
from optparse import OptionParser

def get_arguments():
    parser = OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change the mac address")
    parser.add_option("-m","--mac",dest="new_mac",help="new mac address")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[-]Please specify the interface...For more informatioon use --help")
    if not options.new_mac:
        parser.error("[-]Please specify the mac_address...For more informatioon use --help")
    return options      

def change_mac(interface, new_mac):
    
    print("[+]Changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig" , interface , "down"])
    subprocess.call(["ifconfig" , interface , "hw",  "ether", new_mac])
    subprocess.call(["ifconfig" , interface , "up"]) 
    subprocess.call(["ifconfig","wlan0"])

(options)=get_arguments()
change_mac(options.interface,options.new_mac)





