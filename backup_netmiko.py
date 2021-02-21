import logging
from netmiko import ConnectHandler
from netmiko import SSHDetect
import datetime 
import time
import sys
import yaml
import pathlib
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
#from netmiko.ssh_exception import NetMikoTimeoutException
#from netmiko.ssh_exception import AuthenticationException
#from netmiko.ssh_exception import SSHException
class backup_of_multiple_device():
	def __init__(self):
		current_dir = pathlib.Path(__file__).parent
		current_dir = str(current_dir)
		Variable=yaml.safe_load(open(current_dir+'/device_list.yaml'))
		self.IP_ADDRESS=(Variable['IP_ADDRESS'])
		self.username=(Variable['username'])
		self.password=(Variable['password'])
		self.send_commands=(Variable['send_commands'])
		self.device_type=(Variable['device_type'])

	def Connect(self):
		device_list=[]
		connection =''
		for i in range(0,len(self.IP_ADDRESS)):
			connection="connection_{}".format(i)
			connection= {
			   "device_type": self.device_type,
			   "host": self.IP_ADDRESS[i],
			   "username":self.username,
			   "password":self.password,
			     }
			device_list.append(connection)
		return device_list

	def Backing_up_configuration(self,client,net_connect):
		logger.info("Backing_up_configuration for device %s", self.IP_ADDRESS)
		TNOW=datetime.datetime.now().replace(microsecond=0)
		TNOW=str(TNOW).replace(" ","_")
		logger.info("Intiating backup_" +str(client['host'])+"_"+str(TNOW))
		k=0
		listing=[]
		while k < (len(self.send_commands)):
			listing.append(self.send_commands[k])
			k=k+1
		output = net_connect.send_config_set(listing)
		SAVE_FILE=open("backing_up_config"+"_"+str(client['host']),"w")
		print("config back up done")
		SAVE_FILE.write(output)
		SAVE_FILE.close()

	



