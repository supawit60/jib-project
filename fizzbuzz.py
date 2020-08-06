# ถ้า input ที่เข้ามาหาร 3 ลงตัวให้ return คำว่า Fizz
# ถ้า input ที่เข้ามาหาร 5 ลงตัวให้ return คำว่า Buzz
# ถ้า input ที่เข้ามาหาร 3 และ ลงตัวให้ return คำว่า FizzBuuzz
# ถ้าไม่ตรงเคสไหน ให้ return เลขนั้นๆ

import unittest


def fizzbuzz(number):
    if number == 1:
        return 1
    if number == 3:
        return 'Fizz'


class TestFizzBuzz(unittest.TestCase):
    def test_input_1_should_get_1(self):
        result = fizzbuzz(1)
        self.assertEqual(result, 1)

    def test_input_3_should_get_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'Fizz')


# ถ้า run ที่ไฟล์ตรงๆ จะ run unittest, ถ้า import จะไม่ rum unit test
if __name__ == '__main__':
    unittest.main()
