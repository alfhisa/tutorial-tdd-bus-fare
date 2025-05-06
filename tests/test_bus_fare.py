import unittest
from datetime import datetime
from src.bus_fare import bus_ticket_price

class TestBusFare(unittest.TestCase):

    def test_child_under_2_free(self):
        dt = datetime(2024, 5, 6, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=1, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 0.0)

    # TODO: Complete the tests below based on rules

    def test_teenager_half_fare(self):
        dt = datetime(2024, 5, 6, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=15, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 3.0/2)

    def test_adult_full_fare(self):
        dt = datetime(2024, 5, 6, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=20, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 3.0)

    def test_senior_half_fare(self):
        dt = datetime(2024, 5, 6, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=99, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 3.0/2)

    def test_weekend_flat_rate(self):
        dt = datetime(2025, 5, 3, 10, 0)  # Weekend morning, off-peak
        fare = bus_ticket_price(age=17, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 2.0)

    def test_public_holiday_surcharge(self):
        dt = datetime(2024, 5, 1, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=1, ride_datetime=dt, ride_duration=10, is_public_holiday=True)
        self.assertEqual(fare, 2.0)

    def test_short_trip_off_peak_free(self):
        dt = datetime(2024, 5, 6, 0, 4)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=20, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 0.0)

if __name__ == "__main__":
    unittest.main()
