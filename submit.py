import numpy as np
import sklearn

# You are allowed to import any submodules of numpy or sklearn e.g. sklearn.metrics.accuracy_score to calculate accuracy of a learnt model
# You are not allowed to use other libraries such as scipy, keras, tensorflow etc

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_map, my_params etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here


_EVEN = np.arange(0, 32, 2)   # [0, 2, 4, ..., 30]  shape (16,)
_ODD  = np.arange(1, 32, 2)   # [1, 3, 5, ..., 31]  shape (16,)

################################
# Non Editable Region Starting #
################################
def my_map( X ):
################################
#  Non Editable Region Ending  #
################################

	n = X.shape[0]

	Xe = X[:, _EVEN].astype(np.int8)   # shape (n, 16)
	Xo = X[:, _ODD].astype(np.int8)    # shape (n, 16)

	Xc = (Xe[:, :, None] & Xo[:, None, :]).reshape(n, -1)   # shape (n, 256)

	# Concatenate: [even | odd | cross-products]  -> shape (n, 288)
	X_map = np.hstack([Xe, Xo, Xc])

	return X_map

################################
# Non Editable Region Starting #
################################
def my_params( X_map, X_raw, y ):
################################
#  Non Editable Region Ending  #
################################


	my_params = {
		'loss'          : 'squared_hinge',
		'dual'          : False,
		'C'             : 1.0,
		'tol'           : 5e-3,
		'fit_intercept' : True,
		'max_iter'      : 1000,
	}

	return my_params
