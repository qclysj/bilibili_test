import pytest
import pandas as pd
import logging
import ast  # 用于将字符串转换为字典
import os

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='test.log',
    filemode='w'
)

logger = logging.getLogger(__name__)


def read_csv(file_path):
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            logger.error(f"文件不存在: {file_path}")
            return []

        df = pd.read_csv(file_path, encoding='utf-8')
        test_cases = []
        for _, row in df.iterrows():
            # 将测试数据列的字符串转换为字典
            test_data_str = row['测试数据'].strip()
            # 替换中文冒号为英文冒号
            test_data_str = test_data_str.replace('：', ':')
            # 替换反引号为单引号
            test_data_str = test_data_str.replace('`', "'")
            # 确保字符串以 '{' 开头和 '}' 结尾
            if test_data_str.startswith('{') and test_data_str.endswith('}'):
                try:
                    test_data = ast.literal_eval(test_data_str)
                except:
                    test_data = {}
                    logger.error(f"无法解析测试数据: {test_data_str}")
            else:
                test_data = {}
                # 尝试解析键值对
                if ':' in test_data_str:
                    key, value = test_data_str.split(':', 1)
                    key = key.strip().strip("'")
                    value = value.strip().strip("'")
                    test_data[key] = value
            test_cases.append({
                "用例编号": row['用例编号'],
                "用例标题": row['用例标题'],
                "前置条件": row['前置条件'],
                "测试步骤": row['测试步骤'],
                "测试数据": test_data,
                "预期结果": row['预期结果']
            })
        return test_cases
    except Exception as e:
        logger.error(f"读取 CSV 文件时出错: {e}")
        return []


@pytest.fixture(scope="module", params=read_csv("登录模块_test_cases.csv"))
def login_test_cases(request):
    return request.param


@pytest.fixture(scope="module", params=read_csv("搜索功能模块_test_cases.csv"))
def search_test_cases(request):
    return request.param


@pytest.fixture(scope="module", params=read_csv("视频播放模块_test_cases.csv"))
def video_test_cases(request):
    return request.param


@pytest.fixture(scope="module", params=read_csv("弹幕模块_test_cases.csv"))
def bullet_chat_test_cases(request):
    return request.param
