import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add1(self):
        time1 = data.Time(4,4,24)
        time2 = data.Time(5,5,35)
        results = lab5.time_add(time1,time2)
        expected = data.Time(9,9,59)
        self.assertEqual(expected,results)

    def test_time_add2(self):
        time1 = data.Time(4, 54, 25)
        time2 = data.Time(5, 5, 35)
        results = lab5.time_add(time1, time2)
        expected = data.Time(10, 0, 0)
        self.assertEqual(expected, results)

    # Part 4
    def test_is_descending_1(self):
        list1 = [5,4,3,2,1]
        results = lab5.is_descending(list1)
        expected = True
        self.assertEqual(expected, results)
    def test_is_descending_2(self):
        list1 = [1,2,3,4,5]
        results = lab5.is_descending(list1)
        expected = False
        self.assertEqual(expected, results)
    # Part 5
    def test_largeset_between_1(self):
        new_list = [1,2,3,4,5,6,8,9,10]
        results = lab5.largest_between(new_list,2,4)
        expected = 2
        self.assertEqual(expected,results)
    def test_largeset_between_2(self):
        new_list = [1,2,3,4,5,6,7,8,9,10]
        results = lab5.largest_between(new_list,1,10)
        expected = 8
        self.assertEqual(expected,results)


    # Part 6
    def test_furthest_from_origin_1(self):
        point_list = [data.Point(1,2),data.Point(9,4),data.Point(8,8)]
        results = lab5.furthest_from_origin(point_list)
        expected = 2
        self.assertEqual(expected, results)

    def test_furthest_from_origin_2(self):
        point_list = []
        results = lab5.furthest_from_origin(point_list)
        expected = None
        self.assertEqual(expected, results)




if __name__ == '__main__':
    unittest.main()
