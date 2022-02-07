import subprocess
from optparse import OptionParser
import re

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


def get_current_mac(interface):
    output = subprocess.check_output(["ifconfig",interface])
    
    
    try:
        mac_address_search_result = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(output)).group(0)
        return mac_address_search_result
    except AttributeError as e:
        print("Input is not valid")
    except subprocess.CalledProcessError as e:
        print("Input is not valid")
    except Exception as e:
        print("Something went wrong!")


   
(options)=get_arguments()
(Orginal_MAC)=get_current_mac(options.interface)
print("current MAC is " + Orginal_MAC)

change_mac(options.interface,options.new_mac)

(current_mac)=get_current_mac(options.interface)

if options.new_mac == current_mac:
    print("[+]MAC address changed sucessfully to " + current_mac)
else:
    print("[-]MAC address is not changed! ")







