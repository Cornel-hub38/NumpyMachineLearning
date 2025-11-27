#!/usr/bin/env python
import numpy as np


array_2d = np.array([ [5, 10, 15], [20, 25, 30], [35, 40, 45] ] )
print("\n array_2d \n", array_2d, "\n")
print("\n array_2d[0] \n", array_2d[0], "\n")
print("\n array_2d[2] \n", array_2d[2], "\n")

print("\n array_2d[2,1] \n", array_2d[2,1], "\n")
# L shape - start indexing from top to bottom and then left to right
#  So top of L = 0-row,
# and far extreme of L = 5-column - in a 5x5 matrix

# s 45 from array_2d = array[2,2]
print("array_2d[2,2] \n" , array_2d[2,2], "\n")
print("array_2d", array_2d, "\n")
# Slicing
# top row
print("SLICING : \n")
tp_row = array_2d[0:1,:]
print("top row \n", tp_row, "\n")
# slicing - bottom row = 35, 40, 45
print("SLICING botttom row = 35, 40, 45\n")
print("line 25 \n", array_2d[2:3,:], "\n")
# slicing middle row
print("\n MIDDLE ROW \n")
print("\n array_2d[1:2], : ] ", array_2d[1:2, :], "\n")
# slicing 2 rows - row1 and row 2
print("\n SLICING TWO ROWS, row1 and row2 \n")
set =array_2d[1:3,:]
print("\n set... where set=array_2d[1:3, : ] ", set, "\n")
# now take a subset of above
set[0:1, :]
array_2d[1:3, 1:3]
# array_2d
array_2d
#  top left slice/selection
#selection of bottom left
array_2d[1:3,0:1]
#error there
# ty again

print("array_2d[1:3, 0:2] == selection of bottom left: ", array_2d[1:3, 0:2], "\n")
print("\nrightmost bottom half\n")
print("\n array_2d[1:3, 1:3] ", array_2d[1:3, 1:3], "\n")
#top right of array_2d
array_2d[0:2, 1:3]
array_2d[0:2,0:2]
# try slicing with a 4 d array
f4_arrayslicing = np.array(  [ [69, 20, 31, 15 ], [55, 200, 16, 5 ],   [ 12, 19, 66, 45],  [ 77, 99, 86, 46   ] , [ 45, 28, 92, 56] ]  )
f4_arrayslicing
#top left selection
f4_arrayslicing [ 0:5, 0:2 ]
# top left  2x2
f4_arrayslicing[0:2, 0:2]
# selectin= 19 --> 86
f4_arrayslicing[ 2:4, 1:3]
# array conditionals
f4_arrayslicing > 45
f4_arrayslicing [f4_arrayslicing > 45]
f4_arrayslicing
f4_arrayslicing[f4_arrayslicing < 16]
