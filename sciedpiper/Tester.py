
__author__ = "Timothy Tickle"
__copyright__ = "Copyright 2014"
__credits__ = [ "Timothy Tickle", "Brian Haas" ]
__license__ = "MIT"
__maintainer__ = "Timothy Tickle"
__email__ = "ttickle@broadinstitute.org"
__status__ = "Development"


import CommandlineTester
import CommandTester
import DependencyTreeTester
import PipelineTester
import unittest


# Calls all unit tests as a regression suite.
suite = unittest.TestSuite()
suite.addTest( CommandlineTester.suite() )
suite.addTest( CommandTester.suite() )
suite.addTest( DependencyTreeTester.suite() )
suite.addTest( PipelineTester.suite() )


runner = unittest.TextTestRunner()
runner.run( suite )