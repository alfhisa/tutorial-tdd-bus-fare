import unittest
from datetime import datetime
from anjay.bus_fare import bus_ticket_price

class TestBusFare(unittest.TestCase):

    def test_child_under_2_free(self):
        dt = datetime(2024, 5, 6, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=1, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 0.0)

    def test_teenager_half_fare(self):
        dt = datetime(2024, 5, 6, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=14, ride_datetime=dt, ride_duration=100, is_public_holiday=False)
        self.assertEqual(fare, 1.5)
        pass

    def test_adult_full_fare(self):
        dt = datetime(2024, 5, 6, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=20, ride_datetime=dt, ride_duration=100, is_public_holiday=False)
        self.assertEqual(fare, 3)
        pass

    def test_senior_half_fare(self):
        dt = datetime(2024, 5, 6, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=66, ride_datetime=dt, ride_duration=100, is_public_holiday=False)
        self.assertEqual(fare, 1.5)
        pass

    def test_weekend_flat_rate(self):
        # dt = datetime(year, month, day, hours, minute)
        dt = datetime(2025, 5, 10, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=20, ride_datetime=dt, ride_duration=100, is_public_holiday=False)
        self.assertEqual(fare, 2)
        pass

    def test_public_holiday_surcharge(self):
        dt = datetime(2024, 5, 10, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=20, ride_datetime=dt, ride_duration=100, is_public_holiday=True)
        self.assertEqual(fare, 5)
        pass

    def test_short_trip_off_peak_free(self):
        dt = datetime(2024, 5, 10, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=20, ride_datetime=dt, ride_duration=1, is_public_holiday=False)
        self.assertEqual(fare, 0)
        pass

if __name__ == "__main__":
    unittest.main()
