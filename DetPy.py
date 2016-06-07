#-*- coding: utf-8 -*-
import numpy as N
print "Enter some array like this"\
 " \"[1,2],[2,3]\" (without quotations)"
array_input = eval(raw_input())
array_input = N.array(array_input)
array_determinant = N.linalg.det(array_input)
print "Determinant = %d"%array_determinant