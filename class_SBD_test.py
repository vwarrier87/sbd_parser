#Test file for SBD Class

from class_SBD import SBD

def test_sbd_display_packet_size():
	sbd = SBD('A')
	assert sbd.get_packet_size() == 85



#sbd.get_header_encoding()
#sbd.get_packet_contents()
#sbd.get_packet_size()
with open('300434060605980_000341.sbd', 'r') as file:
	data = file.readlines()
sbd = SBD(data[0])
#sbd.parse_data()
sbd.display_parsed_data()
# print(sbd.get_bitstring())
# sbd_f_data=sbd.parse_data()
# header = sbd.get_header()
# for i in range(0,8):
# 	if (header & 1<<i) == 1<<i:
# 		print("!--------------" + str(self.header_encoding_scheme[i]) + "--------------!")
# 		for j in range(0,len(sbd_f_data[i])):
# 			print(self.field_data[i][j] +":" + str(result))
