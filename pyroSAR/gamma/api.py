###############################################################################
# import wrapper for the pyroSAR GAMMA API

# Copyright (c) 2018-2019, the pyroSAR Developers.

# This file is part of the pyroSAR Project. It is subject to the
# license terms in the LICENSE.txt file found in the top-level
# directory of this distribution and at
# https://github.com/johntruckenbrodt/pyroSAR/blob/master/LICENSE.txt.
# No part of the pyroSAR project, including this file, may be
# copied, modified, propagated, or distributed except according
# to the terms contained in the LICENSE.txt file.
###############################################################################
import os
import sys
import warnings

from .parser import autoparse

try:
    autoparse()
    
    #sys.path.insert(0, os.path.join(os.path.expanduser('~'), '.pyrosar'))
    sys.path.insert(0, '/work/dc129/dc129/shared/.pyrosar')
    
    try:
        from gammaparse import *
    except ImportError:
        warnings.warn('found a GAMMA installation directory, but module parsing failed')

except RuntimeError:
    warnings.warn('could not find GAMMA installation directory; please set the GAMMA_HOME environment variable')
