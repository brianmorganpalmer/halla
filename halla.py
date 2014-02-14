"""
Author: George Weingart
Description: Halla command python wrapper.
"""

#####################################################################################
#Copyright (C) <2012>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in the
#Software without restriction, including without limitation the rights to use, copy,
#modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#and to permit persons to whom the Software is furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies
#or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#####################################################################################

__author__ = "George Weingart"
__copyright__ = "Copyright 2014"
__credits__ = ["George Weingart"]
__license__ = "MIT"
__maintainer__ = "George Weingart"
__email__ = "george.weingart@gmail.com"
__status__ = "Development"

#************************************************************************************
#*   halla.py                                                                       *
#*   Feb. 12, 2014:   George Weingart                                               *
#*   The objective of this program is to serve as a simple wrapper for the halla    *
#*   command.                                                                       *
#*   It accepts as input the parameters that the halla command would accept and     *
#*    passes them verbatum to the halla command                                     *
#************************************************************************************

import os
import sys
CommandInvoke = "python -m halla "  + ' '.join(sys.argv[1:])
os.system(CommandInvoke)
exit (0)

