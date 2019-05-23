import numpy
import mysum2d

def test_mysum_lists():
	A = numpy.array([[1,2],[3,4]])
	B = numpy.array([[4],[5]])
	
	C_expected = numpy.array([[1*4 + 2*5], [3*4 + 4*5]])
	C = mysum2d.mysum_lists(A, B)
	
	numpy.testing.assert_allclose(C, C_expected)
	assert C.shape == C_expected.shape, ("shapes are weird", C.shape, C_expected.shape)
	assert (C == C_expected).all()
	
def test_mysum_numpy():
	A = numpy.array([[1,2],[3,4]])
	B = numpy.array([[4],[5]])
	
	C_expected = numpy.array([[1*4 + 2*5], [3*4 + 4*5]])
	C = mysum2d.mysum_numpy(A, B)
	numpy.testing.assert_allclose(C, C_expected)
	
def test_mysum_einsum():
	A = numpy.array([[1,2],[3,4]])
	B = numpy.array([[4],[5]])
	
	C_expected = numpy.array([[1*4 + 2*5], [3*4 + 4*5]])
	C = mysum2d.mysum_einsum(A, B)
	numpy.testing.assert_allclose(C, C_expected)


def test_wrong_mysum_numpy():
	A = numpy.array([[1,2],[3,4]])
	B = numpy.array([[4,5]])
	
	failed = False
	
	try:
		C = mysum2d.mysum_numpy(A, B)
	except ValueError as e:
		failed = True
	
	assert failed, "assert was raised as expected"


import pytest
def test_wronginput_mysum_lists():
	A = numpy.array([[1,2],[3,4]])
	B = numpy.array([[4,5]])
	
	with pytest.raises(AssertionError):
		mysum2d.mysum_lists(A, B)

import pytest
def test_wronginput_mysum_numpy():
	A = numpy.array([[1,2],[3,4]])
	B = numpy.array([[4,5]])
	
	with pytest.raises(ValueError):
		mysum2d.mysum_numpy(A, B)





