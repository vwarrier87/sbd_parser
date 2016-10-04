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

print(sbd.get_bitstring())
sbd.parse_data()