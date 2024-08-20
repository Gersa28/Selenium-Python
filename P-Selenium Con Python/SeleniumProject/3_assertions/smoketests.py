'''
Orquestador de tests
'''


from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTests
from searchtests import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_test]) # SUIT DE PRUEBAS, pasamos la lista de los tests

kwargs = { # Parámetros para el Reporte
    "output": 'smoke-report',
    "report_name": 'report_name_test'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)