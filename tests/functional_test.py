import unittest
import sys
from AdagucTests.TestWMS import TestWMS
from AdagucTests.TestWCS import TestWCS
from AdagucTests.TestWMSSLD import TestWMSSLD
from AdagucTests.TestWMSDocumentCache import TestWMSDocumentCache
from AdagucTests.TestOpenDAPServer import TestOpenDAPServer
from AdagucTests.TestWMSTiling import TestWMSTiling
from AdagucTests.TestWMSPolylineRenderer import TestWMSPolylineRenderer
from AdagucTests.TestADAGUCFeatureFunctions import TestADAGUCFeatureFunctions
from AdagucTests.TestCSV import TestCSV
from AdagucTests.TestGeoJSON import TestGeoJSON
from AdagucTests.TestMetadataService import TestMetadataService

testsuites=[];
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestWMS))
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestWCS))
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestWMSSLD))
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestWMSDocumentCache))
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestOpenDAPServer))
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestWMSPolylineRenderer))
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestWMSTiling))
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestADAGUCFeatureFunctions))
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestCSV))
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestGeoJSON))
testsuites.append(unittest.TestLoader().loadTestsFromTestCase(TestMetadataService))
result=unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(testsuites))


sys.exit(not result.wasSuccessful())
