#Name: Extruder Inverter
#Info: Invert extruders behavior. Print Left areas with Right Extruder, Right areas/supports with Left Extruder.
#Depend: GCode
#Type: postprocess

__copyright__ = "Copyright (C) 2017 Guillem Avila - Released under terms of the AGPLv3 License"

with open(filename, "r") as f:
	lines = f.readlines()

with open(filename, "w") as f:
	for line in lines:
		if not line.startswith(';CURA_PROFILE_STRING:'):
			if 'T1' in line:
				line = line.replace('T1', 'T0').replace('2nd', '1st')
			elif 'T0' in line:
				line = line.replace('T0', 'T1').replace('1st', '2nd')
		f.write(line)