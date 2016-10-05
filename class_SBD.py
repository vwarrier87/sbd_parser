#Basic funcionality of the parser : To parse the SBD file
# -*- coding: iso-8859-15 -*-
import array

class SBD:
	def __init__(self, data_packet):
		self.data_bytes = array.array('B',data_packet)
		self.header=self.data_bytes[0];				#header tells what all data fields are present
		self.header_encoding_scheme={0:'GPS_Data', 1:'Date_Time', 2:'Supply Voltage', 3:'ADC Channel 0', \
			4:'ADC Channel 1', 5:'GPIO Data', 6:'Accelerometer Data', 7:'Gyroscope Data'}
		self.data_encoding_scheme={0:41, 1:28, 2:9, 3:12, 4:12, 5:2, 6:44, 7:48}
		self.field_encoding_scheme={0:[20,21], 1:[8,9,5,6], 2:[9], 3:[12], 4:[12], 5:[2], \
			6:[12,12,12,8], 7:[16,16,16]}
		self.bitstring=''
		self.data_bitstrings={}
		self.field_bitstrings={}
		self.field_ints={}
		for ch in self.data_bytes:
			self.bitstring +=bin(ch)[2:].rjust(8,'0')

	def get_header_encoding(self):
		return(dict.values(self.header_encoding_scheme))

	def get_packet_contents(self):
		packet_contents=[]
		for i in range (0, 8):
			if (self.header & 1<<i) == 1<<i:
				packet_contents.append(self.header_encoding_scheme[i])
		return packet_contents

	def get_packet_size(self):
		size=0
		for i in range (0, 8):
			if (self.header & 1<<i) == 1<<i:
				size+=self.data_encoding_scheme[i]
		return size

	def get_bitstring(self):
		return self.bitstring

	def parse_data(self):
		bitsread=8
		for i in range (0, 8):
			if (self.header & 1<<i) == 1<<i:
				field_list=[]
				field_int_list=[]
				field_count=0
				print("!--------------" + str(self.header_encoding_scheme[i]) + "--------------!")
				self.data_bitstrings[i] = self.bitstring[bitsread:bitsread+self.data_encoding_scheme[i]]
				for j in range(0,len(self.field_encoding_scheme[i])):
					field_list.append(self.data_bitstrings[i][field_count:field_count+self.field_encoding_scheme[i][j]][::-1])
					field_int_list.append(int(field_list[-1],2))
					field_count += self.field_encoding_scheme[i][j]
				self.field_bitstrings[i] = field_list
				self.field_ints[i]=field_int_list
				bitsread += self.data_encoding_scheme[i]
		print(bitsread)
		print(int(self.field_bitstrings[0][0], 2))
		print(self.field_bitstrings)
		print(self.field_ints)

		print(self.field_ints[0][0]*.00018 -90)
		print(self.field_ints[0][1]*.00018 -180)	

