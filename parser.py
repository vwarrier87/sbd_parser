#Basic funcionality of the parser : To parse the SBD file
import array

class SBD:
	def __init__(self, data_packet):
		self.data_bytes = array.array('B',data_packet)
		self.header=self.data_bytes[0];				#header tells what all data fields are present
		self.header_encoding_scheme={0:'GPS_Data', 1:'Date_Time', 2:'Supply Voltage', 3:'ADC Channel 0', \
			4:'ADC Channel 1', 5:'GPIO', 6:'Accelerometer Data', 7:'Gyroscope Data'}
	def parse_header(self):
		print("Gello")
	def display_header_encoding(self):
		print(dict.values(self.header_encoding_scheme))
	def display_packet_contents(self):
		for i in range (0, 8):
			if (self.header & 1<<i) == 1<<i:
				print (self.header_encoding_scheme[i])



sbd = SBD('a')
sbd.parse_header()
sbd.display_header_encoding()
sbd.display_packet_contents()



