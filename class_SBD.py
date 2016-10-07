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
		self.field_encoding_scheme={0:[20,21], 1:[8,9,5,6], 2:[9], 3:[12], 4:[12], 5:[1,1], \
			6:[12,12,12,8], 7:[16,16,16]}
		self.field_data={0:['Latitude', 'Longitude'], 1:['Year','Day','Hour','Minute'], 2:['Supply Voltage'],\
			3:['ADC Channel 0'], 4:['ADC Channel 1'], 5:['GPIO 0','GPIO 1'], 6:['Acc X', 'Acc Y', 'Acc Z', 'Temperature'],\
			7:['Gyro X', 'Gyro Y', 'Gyro Z'] }
		self.field_functions={0:[lambda x:(x*0.00018)-90, lambda x:(x*.00018)-180], 1:[lambda x:(2000+x), 
			lambda x:x,lambda x:x,lambda x:x] , 2:[lambda x: x*0.038672], 3:[lambda x: x*0.000805664], \
			4:[lambda x: x*0.000805664], 5:[lambda x:x,lambda x:x], 6:[lambda x:x,lambda x:x,lambda x:x,lambda x:x],\
			7:[lambda x:x,lambda x:x,lambda x:x] }
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
				for j in range(0,len(self.field_encoding_scheme[i])):
					bitstoread = self.field_encoding_scheme[i][j]
					print("bitstoread" + str(bitstoread))
					bitsread += bitstoread
					q = bitsread / 8
					r = bitsread % 8
					m = bitstoread / 8
					field_str=''
					print("bitsread" + str(bitsread))
					print("q"+str(q))
					print("r"+str(r))
					print("m"+str(m))
					if r == 0:
						for x in range(0,m):
							field_str+= self.bitstring[(8*(q-x-1)):(8*(q-x))]
						rem = bitstoread - (m * 8)
						if rem < 0:
							rem=0
						print("rem"+str(rem))
						field_str+= self.bitstring[8*(q-m-1):(8*(q-m-1))+rem]
					else:
						if r < bitstoread:
							field_str+=self.bitstring[((8*(q+1))-r):(8*(q+1))]
							print(field_str)
						else:
							field_str+= self.bitstring[(bitsread-bitstoread+1):bitsread+1]
						n = (bitstoread - r) / 8
						if n<0:
							n=0
						for x in range(0,n):
							field_str+= self.bitstring[(8*(q-x-1)):8*(q-x)]
						rem = bitstoread - ((n*8)+r)
						if rem <0:
							rem=0
						print("rem"+str(rem))
						field_str+= self.bitstring[8*(q-n-1):(8*(q-n-1))+rem]
					print(field_str)
					field_list.append(field_str)
					field_int_list.append(int(field_list[-1],2))
					field_count += self.field_encoding_scheme[i][j]
				self.field_bitstrings[i] = field_list
				self.field_ints[i]=field_int_list
		print(bitsread)
		#print(int(self.field_bitstrings[0][0], 2))
		print(self.field_bitstrings)
		print(self.field_ints)
		for i in range(0,8):
			if (self.header & 1<<i) == 1<<i:
				print("!--------------" + str(self.header_encoding_scheme[i]) + "--------------!")
				for j in range(0,len(self.field_encoding_scheme[i])):
					result = self.field_functions[i][j](self.field_ints[i][j])
					print(self.field_data[i][j] +":" + str(result))


