import array
with open('300434060605980_000341.sbd', 'r') as file:
	data = file.readlines()

line= array.array('B',data[0])
print(line)

bitstring=''
for ch in line:
	ch_str=bin(ch)[2:].rjust(8,'0')[::-1]
	bitstring+=ch_str
	print(ch_str)
print(len(line))

lat = bitstring[8:28]
print(lat)
print(int(lat[::-1],2))
latitude = int(lat[::-1],2)*0.00018 - 90
print(latitude)

field_encoding_scheme={0:[20,21], 1:[8,9,5,6], 2:[9], 3:[12], 4:[12], 5:[1,1], \
			6:[12,12,12,8], 7:[16,16,16]}

header=line[0]
field_ints={}
bitsread=8
for i in range (0, 8):
	if (header & 1<<i) == 1<<i:
		field_list=[]
		field_int_list=[]
		
		for j in range(0,len(field_encoding_scheme[i])):
			bitstoread = field_encoding_scheme[i][j]
			print("bitstoread" + str(bitstoread))
			field_str=bitstring[bitsread:bitsread+bitstoread]
			bitsread += bitstoread
			print(field_str)
		 	field_list.append(field_str[::-1])
		 	field_int_list.append(int(field_list[-1],2))
		# 	field_count += self.field_encoding_scheme[i][j]
		# self.field_bitstrings[i] = field_list
		field_ints[i]=field_int_list
print(bitsread)
print(field_ints)