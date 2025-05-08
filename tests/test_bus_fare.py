import unittest
from datetime import datetime
from src.bus_fare import bus_ticket_price

class TestBusFare(unittest.TestCase):

    def test_child_under_2_free(self):
        dt = datetime(2024, 5, 6, 10, 0)
        fare = bus_ticket_price(age=1, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 0.0)

    def test_teenager_half_fare(self):
        dt = datetime(2024, 5, 6, 10, 0)
        fare = bus_ticket_price(age=16, ride_datetime=dt, ride_duration=20, is_public_holiday=False)
        self.assertEqual(fare, 1.5)

    def test_adult_full_fare(self):
        dt = datetime(2024, 5, 6, 10, 0)
        fare = bus_ticket_price(age=30, ride_datetime=dt, ride_duration=20, is_public_holiday=False)
        self.assertEqual(fare, 3.0)

    def test_senior_half_fare(self):
        dt = datetime(2024, 5, 6, 10, 0)
        fare = bus_ticket_price(age=70, ride_datetime=dt, ride_duration=20, is_public_holiday=False)
        self.assertEqual(fare, 1.5)

    def test_weekend_flat_rate(self):
        dt = datetime(2024, 5, 4, 10, 0) 
        fare = bus_ticket_price(age=30, ride_datetime=dt, ride_duration=20, is_public_holiday=False)
        self.assertEqual(fare, 2.0)

    def test_public_holiday_surcharge(self):
        dt = datetime(2024, 5, 6, 10, 0)
        fare = bus_ticket_price(age=30, ride_datetime=dt, ride_duration=20, is_public_holiday=True)
        self.assertEqual(fare, 2.0)

    def test_short_trip_off_peak_free(self):
        dt = datetime(2024, 5, 6, 10, 0)
        fare = bus_ticket_price(age=30, ride_datetime=dt, ride_duration=4, is_public_holiday=False)
        self.assertEqual(fare, 0.0)

if __name__ == "__main__":
    unittest.main()
