
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import unittest
from project import Smartphone

def custom_function(file_name):
    with open(file_name, 'rt') as f:
        return sum(1 for _ in f)
# TestCase를 작성
class CustomTests(unittest.TestCase): 

    def test_runs(self):
        """단순 실행여부 판별하는 테스트 메소드"""
        with self.assertRaises(TypeError):
            custom_function()
            custom_function2()

    def test_runs2(self):
        """단순 실행여부 판별하는 테스트 메소드"""
        with self.assertRaises(TypeError):
            custom_function()
            custom_function2()

# unittest를 실행
if __name__ == '__main__':  
    print(dir(unittest))
    unittest.main()


#python unittest
## 목적 : 단위 테스트로 작성 코드 검증
## 방법
### unittest.Testcase 상속하여 테스트 클래스 작성

