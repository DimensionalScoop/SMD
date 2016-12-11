from libc.math cimport sqrt,pow
from cpython cimport array
import array

def distances(double[:,:] vectors,int lenght):
	"""Calculates the euclidean distances squared between the origin and each element of vectors. Vectors must not contain more than 10000 elements. The elements of vectors must be 3d arrays."""
	cdef double distances[10000]
	cdef int i = 0
	cdef double[:,:] vec = vectors

	while i<lenght:
		distances[i] = pow(vec[i,0],2)+pow(vec[i,1],2)+pow(vec[i,2],2)
		i+=1

	return distances