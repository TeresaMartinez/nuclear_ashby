"""
Element melting point extension for periodictable in Celsius
source http://en.wikipedia.org/wiki/Melting_points_of_the_elements_(data_page)
mainly Haynes, William M., ed. (2011). CRC Handbook of Chemistry and Physics (92nd ed.). CRC Press. pp. 4.121-4.123. ISBN 1439855110.
Example --> print U melting temperature in Celsius
>>> import melting_point
>>> import periodictable as pt
>>> print pt.U.melting_point

"""
import periodictable.core

def init(table, reload=False):
	if 'melting_point' in table.properties and not reload:
		return table.properties.append('melting_point')
	# Set the default, if any
	periodictable.core.melting_point = None
    # Units
	periodictable.core.melting_point_units = 'Celsius'
	# Load data
	for symbol,eldata in data.items():
		el = table.symbol(symbol)
		el.melting_point = eldata

# Data table
data = dict(
	n	=	0.,
	H	=	-259.160,
	He	=	-272.200,
	Li	=	180.500,
	Be	=	1287.000,
	B	=	2075.000,
	C	=	4489.000,
	N	=	-210.000,
	O	=	-218.790,
	F	=	-219.670,
	Ne	=	-248.590,
	Na	=	97.794,
	Mg	=	650.000,
	Al	=	660.320,
	Si	=	1414.000,
	P	=	44.150,
	S	=	95.300,
	Cl	=	-101.500,
	Ar	=	-189.340,
	K	=	63.500,
	Ca	=	842.000,
	Sc	=	1541.000,
	Ti	=	1668.000,
	V	=	1910.000,
	Cr	=	1907.000,
	Mn	=	1246.000,
	Fe	=	1538.000,
	Co	=	1495.000,
	Ni	=	1455.000,
	Cu	=	1084.620,
	Zn	=	419.530,
	Ga	=	29.771,
	Ge	=	938.250,
	As	=	817.000,
	Se	=	180.000,
	Br	=	-7.200,
	Kr	=	-157.380,
	Rb	=	39.300,
	Sr	=	777.000,
	Y	=	1522.000,
	Zr	=	1855.000,
	Nb	=	2477.000,
	Mo	=	2623.000,
	Tc	=	2157.000,
	Ru	=	2334.000,
	Rh	=	1964.000,
	Pd	=	1554.900,
	Ag	=	961.780,
	Cd	=	321.070,
	In	=	156.600,
	Sn	=	231.930,
	Sb	=	630.630,
	Te	=	449.510,
	I	=	113.700,
	Xe	=	-111.795,
	Cs	=	28.500,
	Ba	=	727.000,
	La	=	918.000,
	Ce	=	798.000,
	Pr	=	931.000,
	Nd	=	1021.000,
	Pm	=	1042.000,
	Sm	=	1074.000,
	Eu	=	822.000,
	Gd	=	1313.000,
	Tb	=	1356.000,
	Dy	=	1412.000,
	Ho	=	1474.000,
	Er	=	1529.000,
	Tm	=	1545.000,
	Yb	=	819.000,
	Lu	=	1663.000,
	Hf	=	2233.000,
	Ta	=	3017.000,
	W	=	3422.000,
	Re	=	3186.000,
	Os	=	3033.000,
	Ir	=	2446.000,
	Pt	=	1768.400,
	Au	=	1064.180,
	Hg	=	-38.837,
	Tl	=	304.000,
	Pb	=	327.460,
	Bi	=	271.400,
	Po	=	254.000,
	At	=	302.000,
	Rn	=	-71.000,
	Fr	=	27.000,
	Ra	=	700.000,
	Ac	=	1051.000,
	Th	=	1750.000,
	Pa	=	1572.000,
	U	=	1135.000,
	Np	=	644.000,
	Pu	=	640.000,
	Am	=	1176.000,
	Cm	=	1345.000,
	Bk	=	986.000,
	Cf	=	900.000,
	Es	=	860.000,
	Fm	=	1527.000,
	Md	=	827.000,
	No	=	827.000,
	Lr	=	1627.000
)