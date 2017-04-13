from src.PreFlight import PreFlight
from src.TestConductor import TestConductor

pre_flight = PreFlight()
pre_flight.check()

test_conductor = TestConductor()
test_conductor.run_tests()
