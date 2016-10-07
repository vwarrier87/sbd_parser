#Test file for SBD Class

from class_SBD import SBD

def test_sbd_display_packet_size():
	sbd = SBD('A')
	assert sbd.get_packet_size() == 85
def test_sbd_parse():
	with open('300434060605980_000341.sbd', 'r') as file:
		data = file.readlines()
		sbd = SBD(data[0])
		expected_vals={ 0:[44.72082,-63.70524],1:[2014,63,4,16],2:[12.259024],3:[1.057836832],4:[0.924096608], 
			5:[0,0],6:[72,30,24,242],7:[64863,32755,0] }

		ints_dict=sbd.parse_data()
		for i in range(0,8):
			if (sbd.header & 1<<i) == 1<<i:
				for j in range(0,len(sbd.field_encoding_scheme[i])):
					result = sbd.field_functions[i][j](sbd.field_ints[i][j])
					print("Expectation: " + str(expected_vals[i][j]) + "\tActual" + str(result))
					#assert result == expected_vals[i][j]
					assert abs(result - expected_vals[i][j]) < 1e-5



test_sbd_parse()