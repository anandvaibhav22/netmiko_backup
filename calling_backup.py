from backup_netmiko import *

class calling_nexus_backup(backup_of_multiple_device):
	def __init__(self):
		backup_of_multiple_device.__init__(self)
	def backing_config(self):
		device_list = self.Connect()
		print(device_list)
		for item in device_list:
			try:
				net_connect=ConnectHandler(**item)
				logger.info("connecting to the device %s", item['host'])
				self.Backing_up_configuration(item,net_connect)
			except Exception as error:
				logger.error("Not able to parse the list of the device")
			


def main():
	object_id = calling_nexus_backup()
	object_id.backing_config()

if __name__ == '__main__':
	main()