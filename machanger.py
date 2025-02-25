import subprocess

if __name__ == "__main__":
	interface = "wlp2s0" 		#Enter Your Wireless Device Name Here
	new_mac = "22:00:11:33:44:55"	#Enter New MAC Address
	
	print(f"Shutting Down The Interface: {interface.upper()}")
	subprocess.run(["ifconfig", interface, "down"])
	
	print(f"CHnaging {interface.upper()} MAC Address to: {new_mac}")
	subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.run(["ifconfig", interface, "up"])
	
	print("Network Interface Turned ON")	
