#custom mouse curve for windows registry by janix

import struct
import numpy
linear_factor = 3

def calculate_point(number):
	fixed = struct.pack('I', (int(number*65536)))
	byte_array = []
	for item in list(fixed):
		item = hex(item)[2:].zfill(2)
		byte_array.append(item)
	proper_format = ','.join(map(str, byte_array))
	
	return proper_format


array = []

Xpoints = numpy.array([0.0, 1.0, 2.0, 4.0, 40.0])
Ypoints = Xpoints * linear_factor

print(Ypoints)

def make_reg_point_text(points_array):
	text = ''
	for index, item in enumerate(points_array):
		if index < len(points_array) - 1:
			text = text + '\t'+ calculate_point(item) +',00,00,00,00,\\' + '\n'
		else:
			text = text + '\t'+ calculate_point(item) +',00,00,00,00' + '\n'
	print(text)
	return text


array.append('''Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Control Panel\Mouse]
"SmoothMouseXCurve"=hex:\\
''')
array.append(make_reg_point_text(Xpoints))
array.append('"SmoothMouseYCurve"=hex:\\ \n')
array.append(make_reg_point_text(Ypoints))

with open("janix.reg", 'w') as f:
 	f.writelines(array)


def read_point_from_reg(str_point):
	str_point = str_point.replace(',', '')
	str_point= bytes.fromhex(str_point)

	unpacked = struct.unpack('I', str_point)
	number = unpacked[0]/65536.0
	return number

# print(read_point_from_reg('00,00,38,00')/ read_point_from_reg('C0,CC,0C,00'))
# print(read_point_from_reg('00,00,70,00')/ read_point_from_reg('80,99,19,00'))
# print(read_point_from_reg('00,00,A8,00')/ read_point_from_reg('40,66,26,00'))
# print(read_point_from_reg('00,00,E0,00')/ read_point_from_reg('00,33,33,00'))


# print (read_point_from_reg('80,99,19,00')/read_point_from_reg('C0,CC,0C,00'))
# print (read_point_from_reg('40,66,26,00')/read_point_from_reg('80,99,19,00'))
# print (read_point_from_reg('00,33,33,00')/read_point_from_reg('40,66,26,00'))