import pytest
import pandas as pd
import ast

class TestBilibiliLogin:
    @staticmethod
    def load_test_cases(filename):
        df = pd.read_csv(filename, encoding='utf-8')
        test_cases = []
        for _, row in df.iterrows():
            test_data = ast.literal_eval(row['测试数据'])
            test_cases.append((test_data, row['预期结果']))
        return test_cases

    @pytest.mark.parametrize("test_data, expected", load_test_cases.__func__('登录模块_test_cases.csv'))
    def test_login(self, test_data, expected):
        print(f"测试数据: {test_data}")
        print(f"预期结果: {expected}")

if __name__ == '__main__':
    pytest.main(["-v", __file__])