import datetime
import uscalendar.market_open as mo
import uscalendar.federal_holiday as fh
import unittest


class MarketOpen(unittest.TestCase):

    def test_weekend(self):
        self.assertTrue(mo.is_weekend('2022-01-08'))  # works for Saturday
        self.assertTrue(mo.is_weekend('2022-01-09'))  # works for Sunday
        self.assertFalse(mo.is_weekend('2022-01-10'))  # works for Monday
        self.assertFalse(mo.is_weekend('2022-01-11'))  # works for Tuesday
        self.assertFalse(mo.is_weekend('2022-01-12'))  # works for Wednesday
        self.assertFalse(mo.is_weekend('2022-01-13'))  # works for Thursday
        self.assertFalse(mo.is_weekend('2022-01-14'))  # works for Friday

    def test_weekday(self):
        self.assertFalse(mo.is_weekday('2022-01-08'))  # works for Saturday
        self.assertFalse(mo.is_weekday('2022-01-09'))  # works for Sunday
        self.assertTrue(mo.is_weekday('2022-01-10'))  # works for Monday
        self.assertTrue(mo.is_weekday('2022-01-11'))  # works for Tuesday
        self.assertTrue(mo.is_weekday('2022-01-12'))  # works for Wednesday
        self.assertTrue(mo.is_weekday('2022-01-13'))  # works for Thursday
        self.assertTrue(mo.is_weekday('2022-01-14'))  # works for Friday

    def test_new_years(self):
        self.assertFalse(mo.market_open('2021-01-01'))
        self.assertTrue(mo.market_open('2021-01-04'))  # Monday day after new years is not a holiday
        self.assertFalse(mo.market_open('2022-01-01'))  # Saturday Jan 1
        self.assertTrue(mo.market_open('2021-12-31'))  # Friday Dec 31 market is open, even though it's a fed holiday
        self.assertFalse(mo.market_open('2023-01-02'))  # New Years Day 2023
        self.assertFalse(mo.market_open('2024-01-01'))  # 2024
        self.assertFalse(mo.market_open('2025-01-01'))  # 2025
        self.assertFalse(mo.market_open('2026-01-01'))  # NYD 2026
        self.assertFalse(mo.market_open('2027-01-01'))  # Friday Dec 31 off for 2022
        self.assertTrue(mo.market_open('2027-12-31'))  # NYD 2028, market is open as 1 Jan is Saturday
        self.assertFalse(mo.market_open('2029-01-01'))  # NYD 2029
        self.assertFalse(mo.market_open('2030-01-01'))  # NYD 2029

    def test_mlk_day(self):
        self.assertFalse(mo.market_open('2021-01-18'))  # MLK day 2021
        self.assertTrue(mo.market_open('2021-01-19'))  # Day after MLK day 2021
        self.assertFalse(mo.market_open('2022-01-17'))  # MLK Day 2022
        self.assertFalse(mo.market_open('2023-01-16'))  # MLK Day 2023
        self.assertFalse(mo.market_open('2024-01-15'))  # MLK Day 2024
        self.assertFalse(mo.market_open('2025-01-20'))  # MLK Day 2025, also Inauguration day
        self.assertFalse(mo.market_open('2026-01-19'))  # MLK Day 2026
        self.assertFalse(mo.market_open('2027-01-18'))  # MLK Day 2027
        self.assertFalse(mo.market_open('2028-01-17'))  # MLK Day 2028
        self.assertFalse(mo.market_open('2029-01-15'))  # MLK Day 2029
        self.assertFalse(mo.market_open('2030-01-21'))  # MLK Day 2030

    def test_presidents_day(self):
        self.assertFalse(mo.market_open('2021-02-15'))  # Presidents day 2021
        self.assertTrue(mo.market_open('2021-02-16'))  # Day after Presidents day 2021
        self.assertFalse(mo.market_open('2022-02-21'))  # Presidents Day 2022
        self.assertFalse(mo.market_open('2023-02-20'))  # Presidents Day 2023
        self.assertFalse(mo.market_open('2024-02-19'))  # Presidents Day 2024
        self.assertFalse(mo.market_open('2025-02-17'))  # Presidents Day 2025
        self.assertFalse(mo.market_open('2026-02-16'))  # Presidents Day 2026
        self.assertFalse(mo.market_open('2027-02-15'))  # Presidents Day 2027
        self.assertFalse(mo.market_open('2028-02-21'))  # Presidents Day 2028
        self.assertFalse(mo.market_open('2029-02-19'))  # Presidents Day 2029
        self.assertFalse(mo.market_open('2030-02-18'))  # Presidents Day 2030

    def test_good_friday(self):  # lunar calenders suck
        self.assertFalse(mo.market_open('2021-04-02'))  # Good Friday 2021
        self.assertTrue(mo.market_open('2021-04-01'))  # Day before Good Friday 2021
        self.assertFalse(mo.market_open('2022-04-15'))  # Good Friday 2022
        self.assertFalse(mo.market_open('2023-04-07'))  # Good Friday 2022

    def test_memorial_day(self):
        self.assertFalse(mo.market_open('2021-05-31'))  # Memorial Day 2021
        self.assertTrue(mo.market_open('2021-06-01'))  # Day before Memorial Day 2021
        self.assertFalse(mo.market_open('2022-05-30'))  # Memorial Day 2022
        self.assertFalse(mo.market_open('2023-05-29'))  # Memorial Day 2023
        self.assertFalse(mo.market_open('2023-05-29'))  # Memorial Day 2023
        self.assertFalse(mo.market_open('2024-05-27'))  # Memorial Day 2024
        self.assertFalse(mo.market_open('2025-05-26'))  # Memorial Day 2025
        self.assertFalse(mo.market_open('2026-05-25'))  # Memorial Day 2026
        self.assertFalse(mo.market_open('2027-05-31'))  # Memorial Day 2027
        self.assertFalse(mo.market_open('2028-05-29'))  # Memorial Day 2028
        self.assertFalse(mo.market_open('2029-05-28'))  # Memorial Day 2029
        self.assertFalse(mo.market_open('2030-05-27'))  # Memorial Day 2030

    def test_independence_day(self):
        self.assertFalse(mo.market_open('2021-07-05'))  # July 4th 2021 is a Sunday
        self.assertFalse(mo.market_open('2022-07-04'))  # July 4th 2022
        self.assertTrue(mo.market_open('2022-07-05'))  # Day after July 4th 2022
        self.assertFalse(mo.market_open('2023-07-04'))  # July 4th 2023
        self.assertFalse(mo.market_open('2024-07-04'))  # July 4th 2024
        self.assertFalse(mo.market_open('2025-07-04'))  # July 4th 2025
        self.assertTrue(mo.market_open('2026-07-03'))  # July 4th 2026 is on a Saturday, market open on Friday
        self.assertFalse(mo.market_open('2027-07-05'))  # July 4th 2027 is on a Sunday
        self.assertFalse(mo.market_open('2028-07-04'))  # July 4th 2028
        self.assertFalse(mo.market_open('2029-07-04'))  # July 4th 2029
        self.assertFalse(mo.market_open('2030-07-04'))  # July 4th 2030

    def test_labor_day(self):
        self.assertFalse(mo.market_open('2021-09-06'))  # Labor day 2021
        self.assertTrue(mo.market_open('2021-09-07'))  # Day after Labor day 2021
        self.assertFalse(mo.market_open('2022-09-05'))  # Labor Day 2022
        self.assertFalse(mo.market_open('2023-09-04'))  # Labor Day 2023
        self.assertFalse(mo.market_open('2024-09-02'))  # Labor Day 2024
        self.assertFalse(mo.market_open('2025-09-01'))  # Labor Day 2025
        self.assertFalse(mo.market_open('2026-09-07'))  # Labor Day 2026
        self.assertFalse(mo.market_open('2027-09-06'))  # Labor Day 2027
        self.assertFalse(mo.market_open('2028-09-04'))  # Labor Day 2028
        self.assertFalse(mo.market_open('2029-09-03'))  # Labor Day 2029
        self.assertFalse(mo.market_open('2030-09-02'))  # Labor Day 2030

    def test_thanksgiving(self):
        self.assertFalse(mo.market_open('2021-11-25'))  # Thanksgiving Day 2021
        self.assertTrue(mo.market_open('2021-11-26'))  # Day after Thanksgiving 2021
        self.assertFalse(mo.market_open('2022-11-24'))  # Thanksgiving 2022
        self.assertFalse(mo.market_open('2023-11-23'))  # Thanksgiving Day 2023
        self.assertFalse(mo.market_open('2024-11-28'))  # Thanksgiving Day 2024
        self.assertFalse(mo.market_open('2025-11-27'))  # Thanksgiving Day 2025
        self.assertFalse(mo.market_open('2026-11-26'))  # Thanksgiving Day 2026
        self.assertFalse(mo.market_open('2027-11-25'))  # Thanksgiving Day 2027
        self.assertFalse(mo.market_open('2028-11-23'))  # Thanksgiving Day 2028
        self.assertFalse(mo.market_open('2029-11-22'))  # Thanksgiving Day 2029
        self.assertFalse(mo.market_open('2030-11-28'))  # Thanksgiving Day 2030

    def test_christmas(self):
        self.assertFalse(mo.market_open('2021-12-24'))  # Friday the 24th of December 2021
        self.assertFalse(mo.market_open('2022-12-26'))  # Monday the 26th of December 2022
        self.assertFalse(mo.market_open('2023-12-25'))  # Christmas 2023
        self.assertTrue(mo.market_open('2023-12-26'))  # Day after Christmas and a Tuesday
        self.assertFalse(mo.market_open('2024-12-25'))  # Christmas 2024
        self.assertFalse(mo.market_open('2025-12-25'))  # Christmas 2025
        self.assertFalse(mo.market_open('2026-12-25'))  # Christmas 2026
        self.assertFalse(mo.market_open('2027-12-24'))  # Christmas 2027
        self.assertFalse(mo.market_open('2028-12-25'))  # Christmas 2028
        self.assertFalse(mo.market_open('2029-12-25'))  # Christmas 2029
        self.assertFalse(mo.market_open('2030-12-25'))  # Christmas 2030

    def test_dates(self):
        self.assertTrue(mo.market_open('2021-05-07'))  # check again for normal market open date
        self.assertTrue(mo.market_open('2021-5-7'))  # check for dates without 0s
        self.assertTrue(mo.market_open(datetime.date(2021, 5, 7)))  # Check for datetime date
        self.assertTrue(mo.market_open(datetime.datetime(2021, 5, 7, 10, 23)))  # Check for datetime date
        # Check for datetime date, may change if you run on weekend
        # self.assertTrue(mo.market_open(datetime.datetime.now()))

    def test_next_open_day(self):
        self.assertEqual(mo.next_market_open_date('2021-05-13'), '2021-05-14')  # check for Friday
        self.assertEqual(mo.next_market_open_date('2021-05-14'), '2021-05-17')  # check for Weekend
        self.assertEqual(mo.next_market_open_date('2021-05-15'), '2021-05-17')  # check for day on weekend
        self.assertEqual(mo.next_market_open_date('2021-01-15'), '2021-01-19')  # check for MLK
        self.assertEqual(mo.next_market_open_date('2021-11-24'), '2021-11-26')  # check for Thanksgiving


class FederalHolidayTest(unittest.TestCase):

    def test_weekend(self):
        self.assertTrue(fh.is_weekend('2022-01-08'))  # works for Saturday
        self.assertTrue(fh.is_weekend('2022-01-09'))  # works for Sunday
        self.assertFalse(fh.is_weekend('2022-01-10'))  # works for Monday
        self.assertFalse(fh.is_weekend('2022-01-11'))  # works for Tuesday
        self.assertFalse(fh.is_weekend('2022-01-12'))  # works for Wednesday
        self.assertFalse(fh.is_weekend('2022-01-13'))  # works for Thursday
        self.assertFalse(fh.is_weekend('2022-01-14'))  # works for Friday

    def test_weekday(self):
        self.assertFalse(fh.is_weekday('2022-01-08'))  # works for Saturday
        self.assertFalse(fh.is_weekday('2022-01-09'))  # works for Sunday
        self.assertTrue(fh.is_weekday('2022-01-10'))  # works for Monday
        self.assertTrue(fh.is_weekday('2022-01-11'))  # works for Tuesday
        self.assertTrue(fh.is_weekday('2022-01-12'))  # works for Wednesday
        self.assertTrue(fh.is_weekday('2022-01-13'))  # works for Thursday
        self.assertTrue(fh.is_weekday('2022-01-14'))  # works for Friday

    def test_working_day(self):
        self.assertFalse(fh.is_working_day('2022-01-08'))  # works for Saturday
        self.assertFalse(fh.is_working_day('2022-01-09'))  # works for Sunday
        self.assertTrue(fh.is_working_day('2022-01-10'))  # works for Monday
        self.assertTrue(fh.is_working_day('2022-01-11'))  # works for Tuesday
        self.assertTrue(fh.is_working_day('2022-01-12'))  # works for Wednesday
        self.assertTrue(fh.is_working_day('2022-01-13'))  # works for Thursday
        self.assertTrue(fh.is_working_day('2022-01-14'))  # works for Friday

        # test for holiday
        self.assertFalse(fh.is_working_day('2021-01-18'))  # MLK day 2021

    def test_off_day(self):
        self.assertTrue(fh.is_off_day('2022-01-08'))  # works for Saturday
        self.assertTrue(fh.is_off_day('2022-01-09'))  # works for Sunday
        self.assertFalse(fh.is_off_day('2022-01-10'))  # works for Monday
        self.assertFalse(fh.is_off_day('2022-01-11'))  # works for Tuesday
        self.assertFalse(fh.is_off_day('2022-01-12'))  # works for Wednesday
        self.assertFalse(fh.is_off_day('2022-01-13'))  # works for Thursday
        self.assertFalse(fh.is_off_day('2022-01-14'))  # works for Friday

        # test for holiday
        self.assertTrue(fh.is_off_day('2021-01-18'))  # MLK day 2021

    def test_new_years(self):
        self.assertTrue(fh.is_federal_holiday('2021-01-01'))
        self.assertFalse(fh.is_federal_holiday('2021-01-02'))  # day after new years is not a holiday
        self.assertFalse(fh.is_federal_holiday('2022-01-01'))  # Saturday Jan 1
        self.assertTrue(fh.is_federal_holiday('2021-12-31'))  # Friday Dec 31 off for 2022
        self.assertTrue(fh.is_federal_holiday('2023-01-02'))  # New Years Day 2023
        self.assertTrue(fh.is_federal_holiday('2024-01-01'))  # 2024
        self.assertTrue(fh.is_federal_holiday('2025-01-01'))  # 2025
        self.assertTrue(fh.is_federal_holiday('2026-01-01'))  # NYD 2026
        self.assertTrue(fh.is_federal_holiday('2027-01-01'))  # Friday Dec 31 off for 2022
        self.assertTrue(fh.is_federal_holiday('2027-12-31'))  # NYD 2028
        self.assertTrue(fh.is_federal_holiday('2029-01-01'))  # NYD 2029
        self.assertTrue(fh.is_federal_holiday('2030-01-01'))  # NYD 2029

        self.assertTrue(fh.holiday_name('2021-12-31') == "New Years Day")
        self.assertFalse(fh.holiday_name('2021-12-31') == "banana")
        self.assertTrue(fh.holiday_name('2021-01-02') == "None")  # make sure initial assignment to None works

    def test_mlk_day(self):
        self.assertTrue(fh.is_federal_holiday('2021-01-18'))  # MLK day 2021
        self.assertFalse(fh.is_federal_holiday('2021-01-19'))  # Day after MLK day 2021
        self.assertTrue(fh.is_federal_holiday('2022-01-17'))  # MLK Day 2022
        self.assertTrue(fh.is_federal_holiday('2023-01-16'))  # MLK Day 2023
        self.assertTrue(fh.is_federal_holiday('2024-01-15'))  # MLK Day 2024
        self.assertTrue(fh.is_federal_holiday('2025-01-20'))  # MLK Day 2025, also Inauguration day
        self.assertTrue(fh.is_federal_holiday('2026-01-19'))  # MLK Day 2026
        self.assertTrue(fh.is_federal_holiday('2027-01-18'))  # MLK Day 2027
        self.assertTrue(fh.is_federal_holiday('2028-01-17'))  # MLK Day 2028
        self.assertTrue(fh.is_federal_holiday('2029-01-15'))  # MLK Day 2029
        self.assertTrue(fh.is_federal_holiday('2030-01-21'))  # MLK Day 2030

        self.assertTrue(fh.holiday_name('2023-01-16') == "Martin Luther King Day")
        self.assertFalse(fh.holiday_name('2023-01-16') == "banana")

    def test_presidents_day(self):
        self.assertTrue(fh.is_federal_holiday('2021-02-15'))  # Presidents day 2021
        self.assertFalse(fh.is_federal_holiday('2021-02-16'))  # Day after Presidents day 2021
        self.assertTrue(fh.is_federal_holiday('2022-02-21'))  # Presidents Day 2022
        self.assertTrue(fh.is_federal_holiday('2023-02-20'))  # Presidents Day 2023
        self.assertTrue(fh.is_federal_holiday('2024-02-19'))  # Presidents Day 2024
        self.assertTrue(fh.is_federal_holiday('2025-02-17'))  # Presidents Day 2025
        self.assertTrue(fh.is_federal_holiday('2026-02-16'))  # Presidents Day 2026
        self.assertTrue(fh.is_federal_holiday('2027-02-15'))  # Presidents Day 2027
        self.assertTrue(fh.is_federal_holiday('2028-02-21'))  # Presidents Day 2028
        self.assertTrue(fh.is_federal_holiday('2029-02-19'))  # Presidents Day 2029
        self.assertTrue(fh.is_federal_holiday('2030-02-18'))  # Presidents Day 2030

        self.assertTrue(fh.holiday_name('2023-02-20') == "President's Day")
        self.assertFalse(fh.holiday_name('2023-02-20') == "banana")  # test to make sure function returns right name

    def test_memorial_day(self):
        self.assertTrue(fh.is_federal_holiday('2021-05-31'))  # Memorial Day 2021
        self.assertFalse(fh.is_federal_holiday('2021-06-01'))  # Day before Memorial Day 2021
        self.assertTrue(fh.is_federal_holiday('2022-05-30'))  # Memorial Day 2022
        self.assertTrue(fh.is_federal_holiday('2023-05-29'))  # Memorial Day 2023
        self.assertTrue(fh.is_federal_holiday('2023-05-29'))  # Memorial Day 2023
        self.assertTrue(fh.is_federal_holiday('2024-05-27'))  # Memorial Day 2024
        self.assertTrue(fh.is_federal_holiday('2025-05-26'))  # Memorial Day 2025
        self.assertTrue(fh.is_federal_holiday('2026-05-25'))  # Memorial Day 2026
        self.assertTrue(fh.is_federal_holiday('2027-05-31'))  # Memorial Day 2027
        self.assertTrue(fh.is_federal_holiday('2028-05-29'))  # Memorial Day 2028
        self.assertTrue(fh.is_federal_holiday('2029-05-28'))  # Memorial Day 2029
        self.assertTrue(fh.is_federal_holiday('2030-05-27'))  # Memorial Day 2030

        self.assertTrue(fh.holiday_name('2023-05-29') == "Memorial Day")
        self.assertFalse(fh.holiday_name('2023-05-3') == "Banana")

    def test_juneteenth(self):
        self.assertTrue(fh.is_federal_holiday('2021-06-18'))  # Juneteenth 2021, day early on a Friday
        self.assertFalse(fh.is_federal_holiday('2021-06-19'))  # Day after juneteeth but on a Saturday
        self.assertTrue(fh.is_federal_holiday('2022-06-20'))  # Juneteenth 2022, day late on a Monday
        self.assertTrue(fh.is_federal_holiday('2023-06-19'))  # Juneteenth 2023, on 19 June as should be
        self.assertTrue(fh.is_federal_holiday('2024-06-19'))  # Juneteenth 2024, on 19 June as should be
        self.assertTrue(fh.is_federal_holiday('2025-06-19'))  # Juneteenth 2025, on 19 June as should be
        self.assertTrue(fh.is_federal_holiday('2026-06-19'))  # Juneteenth 2026, on 19 June as should be
        self.assertTrue(fh.is_federal_holiday('2027-06-18'))  # Juneteenth 2027
        self.assertTrue(fh.is_federal_holiday('2028-06-19'))  # Juneteenth 2028, on 19 June as should be
        self.assertTrue(fh.is_federal_holiday('2029-06-19'))  # Juneteenth 2029, on 19 June as should be
        self.assertTrue(fh.is_federal_holiday('2030-06-19'))  # Juneteenth 2030, on 19 June as should be

        self.assertTrue(fh.holiday_name('2023-06-19') == "Juneteenth")
        self.assertFalse(fh.holiday_name('2023-06-19') == "banana")  # test to make sure function returns right name

    def test_independence_day(self):
        self.assertTrue(fh.is_federal_holiday('2021-07-05'))  # July 4th 2021 is a Sunday
        self.assertTrue(fh.is_federal_holiday('2022-07-04'))  # July 4th 2022
        self.assertFalse(fh.is_federal_holiday('2022-07-05'))  # Day after July 4th 2022
        self.assertTrue(fh.is_federal_holiday('2023-07-04'))  # July 4th 2023
        self.assertTrue(fh.is_federal_holiday('2024-07-04'))  # July 4th 2024
        self.assertTrue(fh.is_federal_holiday('2025-07-04'))  # July 4th 2025
        self.assertTrue(fh.is_federal_holiday('2026-07-03'))  # July 4th 2026 is on a Saturday
        self.assertTrue(fh.is_federal_holiday('2027-07-05'))  # July 4th 2027 is on a Sunday
        self.assertTrue(fh.is_federal_holiday('2028-07-04'))  # July 4th 2028
        self.assertTrue(fh.is_federal_holiday('2029-07-04'))  # July 4th 2029
        self.assertTrue(fh.is_federal_holiday('2030-07-04'))  # July 4th 2030

        self.assertTrue(fh.holiday_name('2022-07-04') == "Independence Day")
        self.assertFalse(fh.holiday_name('2022-07-04') == "Banana")

    def test_labor_day(self):
        self.assertTrue(fh.is_federal_holiday('2021-09-06'))  # Labor day 2021
        self.assertFalse(fh.is_federal_holiday('2021-09-07'))  # Day after Labor day 2021
        self.assertTrue(fh.is_federal_holiday('2022-09-05'))  # Labor Day 2022
        self.assertTrue(fh.is_federal_holiday('2023-09-04'))  # Labor Day 2023
        self.assertTrue(fh.is_federal_holiday('2024-09-02'))  # Labor Day 2024
        self.assertTrue(fh.is_federal_holiday('2025-09-01'))  # Labor Day 2025
        self.assertTrue(fh.is_federal_holiday('2026-09-07'))  # Labor Day 2026
        self.assertTrue(fh.is_federal_holiday('2027-09-06'))  # Labor Day 2027
        self.assertTrue(fh.is_federal_holiday('2028-09-04'))  # Labor Day 2028
        self.assertTrue(fh.is_federal_holiday('2029-09-03'))  # Labor Day 2029
        self.assertTrue(fh.is_federal_holiday('2030-09-02'))  # Labor Day 2030

        self.assertTrue(fh.holiday_name('2023-09-04') == "Labor Day")
        self.assertFalse(fh.holiday_name('2023-09-04') == "Banana")

    def test_columbus_day(self):
        self.assertTrue(fh.is_federal_holiday('2021-10-11'))  # Columbus day 2021
        self.assertFalse(fh.is_federal_holiday('2021-10-12'))  # day after Columbus day 2021
        self.assertTrue(fh.is_federal_holiday('2022-10-10'))  # Columbus day 2022
        self.assertTrue(fh.is_federal_holiday('2023-10-09'))  # Columbus day 2023
        self.assertTrue(fh.is_federal_holiday('2024-10-14'))  # Columbus day 2024
        self.assertTrue(fh.is_federal_holiday('2025-10-13'))  # Columbus day 2025
        self.assertTrue(fh.is_federal_holiday('2026-10-12'))  # Columbus day 2026
        self.assertTrue(fh.is_federal_holiday('2027-10-11'))  # Columbus day 2027
        self.assertTrue(fh.is_federal_holiday('2028-10-09'))  # Columbus day 2028
        self.assertTrue(fh.is_federal_holiday('2029-10-08'))  # Columbus day 2029
        self.assertTrue(fh.is_federal_holiday('2030-10-14'))  # Columbus day 2030

        self.assertTrue(fh.holiday_name('2023-10-09') == "Columbus Day")
        self.assertFalse(fh.holiday_name('2023-09-04') == "Banana")

    def test_thanksgiving(self):
        self.assertTrue(fh.is_federal_holiday('2021-11-25'))  # Thanksgiving Day 2021
        self.assertFalse(fh.is_federal_holiday('2021-11-26'))  # Day after Thanksgiving 2021
        self.assertTrue(fh.is_federal_holiday('2022-11-24'))  # Thanksgiving 2022
        self.assertTrue(fh.is_federal_holiday('2023-11-23'))  # Thanksgiving Day 2023
        self.assertTrue(fh.is_federal_holiday('2024-11-28'))  # Thanksgiving Day 2024
        self.assertTrue(fh.is_federal_holiday('2025-11-27'))  # Thanksgiving Day 2025
        self.assertTrue(fh.is_federal_holiday('2026-11-26'))  # Thanksgiving Day 2026
        self.assertTrue(fh.is_federal_holiday('2027-11-25'))  # Thanksgiving Day 2027
        self.assertTrue(fh.is_federal_holiday('2028-11-23'))  # Thanksgiving Day 2028
        self.assertTrue(fh.is_federal_holiday('2029-11-22'))  # Thanksgiving Day 2029
        self.assertTrue(fh.is_federal_holiday('2030-11-28'))  # Thanksgiving Day 2030

        self.assertTrue(fh.holiday_name('2021-11-25') == "Thanksgiving Day")
        self.assertFalse(fh.holiday_name('2021-11-25') == "Banana")

    def test_christmas(self):
        self.assertTrue(fh.is_federal_holiday('2021-12-24'))  # Friday the 24th of December 2021
        self.assertTrue(fh.is_federal_holiday('2022-12-26'))  # Monday the 26th of December 2022
        self.assertTrue(fh.is_federal_holiday('2023-12-25'))  # Christmas 2023
        self.assertFalse(fh.is_federal_holiday('2023-12-26'))  # Day after Christmas and a Tuesday
        self.assertTrue(fh.is_federal_holiday('2024-12-25'))  # Christmas 2024
        self.assertTrue(fh.is_federal_holiday('2025-12-25'))  # Christmas 2025
        self.assertTrue(fh.is_federal_holiday('2026-12-25'))  # Christmas 2026
        self.assertTrue(fh.is_federal_holiday('2027-12-24'))  # Christmas 2027
        self.assertTrue(fh.is_federal_holiday('2028-12-25'))  # Christmas 2028
        self.assertTrue(fh.is_federal_holiday('2029-12-25'))  # Christmas 2029
        self.assertTrue(fh.is_federal_holiday('2030-12-25'))  # Christmas 2030

        self.assertTrue(fh.holiday_name('2023-12-25') == "Christmas Day")
        self.assertFalse(fh.holiday_name('2023-12-25') == "Banana")

    def test_inauguration_day(self):
        self.assertTrue(fh.is_federal_holiday('2013-01-21'))  # inauguration day 2013, day later on a Monday
        self.assertFalse(fh.is_federal_holiday('2013-01-20'))  # Sunday but right day, should be false
        self.assertTrue(fh.is_federal_holiday('2017-01-20'))  # day on a Friday
        self.assertTrue(fh.holiday_name('2017-01-20') == "Inauguration Day")  # day on a Friday
        self.assertTrue(fh.holiday_name('2017-01-21') == "None")  # day on a Friday

        self.assertTrue(fh.is_federal_holiday('2021-01-20'))  # day on a Wednesday
        self.assertTrue(fh.is_federal_holiday('2025-01-20'))  # day on a Wednesday, also MLK Day

        self.assertTrue(fh.holiday_name('2025-01-20') == "Martin Luther King Day and Inauguration Day")  # shares a day

        self.assertFalse(fh.is_federal_holiday('2029-01-20'))  # on a weekend

    def test_dates(self):
        self.assertFalse(fh.is_federal_holiday('2021-05-07'))  # check again for normal day
        self.assertFalse(fh.is_federal_holiday('2021-5-7'))  # check for dates without 0s
        self.assertFalse(fh.is_federal_holiday(datetime.date(2021, 5, 7)))  # Check for datetime date
        self.assertFalse(fh.is_federal_holiday(datetime.datetime(2021, 5, 7, 10, 23)))  # Check for datetime date

        # Check for datetime date, may change if you run on weekend
        # self.assertFalse(fh.is_federal_holiday(datetime.datetime.now()))


if __name__ == '__main__':
    unittest.main()
