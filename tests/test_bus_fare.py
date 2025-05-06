import unittest
from datetime import datetime
from src.bus_fare import bus_ticket_price

class TestBusFare(unittest.TestCase):

    def test_child_under_2_free(self):
        dt = datetime(2024, 5, 6, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=1, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 0.0)

    def test_teenager_half_fare(self):
        dt = datetime(2024, 5, 6, 11, 0)  # Weekday, off-peak
        fare = bus_ticket_price(age=17, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 1.5)  # Half of $3

    def test_adult_full_fare(self):
        dt = datetime(2024, 5, 6, 11, 0)  # Weekday, off-peak
        fare = bus_ticket_price(age=30, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 3.0)

    def test_senior_half_fare(self):
        dt = datetime(2024, 5, 6, 11, 0)  # Weekday, off-peak
        fare = bus_ticket_price(age=70, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 1.5)

    def test_weekend_flat_rate(self):
        dt = datetime(2024, 5, 5, 11, 0)  # Sunday
        fare = bus_ticket_price(age=30, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 2.0)

    def test_public_holiday_surcharge(self):
        dt = datetime(2024, 5, 6, 11, 0)  # Weekday, but it's a holiday
        fare = bus_ticket_price(age=30, ride_datetime=dt, ride_duration=10, is_public_holiday=True)
        self.assertEqual(fare, 2.0)  # Flat holiday rate

    def test_short_trip_off_peak_free(self):
        dt = datetime(2024, 5, 6, 11, 0)  # Weekday, off-peak
        fare = bus_ticket_price(age=30, ride_datetime=dt, ride_duration=4, is_public_holiday=False)
        self.assertEqual(fare, 0.0)

    def test_short_trip_peak_paid(self):
        dt = datetime(2024, 5, 6, 8, 30)  # Weekday, during peak hours (8:30 AM)
        fare = bus_ticket_price(age=30, ride_datetime=dt, ride_duration=4, is_public_holiday=False)
        self.assertEqual(fare, 4.5)  # Short trip during peak hours should charge $3 + $1.5

    def test_teenager_peak_fare(self):
        dt = datetime(2024, 5, 6, 8, 30)  # Weekday, during peak hours
        fare = bus_ticket_price(age=17, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 3.0)  # Teenagers still pay half fare during peak hours

    def test_senior_peak_fare(self):
        dt = datetime(2024, 5, 6, 8, 30)  # Weekday, during peak hours
        fare = bus_ticket_price(age=70, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 2.25)  # Senior pays half fare with peak surcharge ($1.5 + $0.75)

if __name__ == "__main__":
    unittest.main()
