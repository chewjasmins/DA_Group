import unittest
import requests


url = "http://172.18.58.80/creative/"


class TestMyProgram(unittest.TestCase):

    def test_TestUrl(self):
        try:
            resp = requests.get(url)
            if int(resp.status_code) == 200:
                print("[TestUrl] URL OK")
            else:
                print("[TestUrl] Requested URL not found")
        except Exception as e:
            print("[TestUrl] Error: ", {e})

    def test_TestCase_2(self):
        print("[TestCase_2] Test case 2")


if __name__ == '__main__':
    unittest.main()

