import pytest
import logging

from drivers import driver_manager
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.watch_page import WatchPage

logger = logging.getLogger(__name__)


def test_user_login(login_test_cases):
    logger.info(f"执行测试用例: {login_test_cases['用例标题']}")
    # 初始化页面对象
    main_page = MainPage()
    login_page = LoginPage()

    # 测试步骤
    main_page.open_url()
    login_page.open_login_url()

    # 提取用户名和密码
    username = login_test_cases["测试数据"].get("username")
    password = login_test_cases["测试数据"].get("password")

    # 执行登录
    login_page.login(username, password)
    login_page.wait()

    # 验证预期结果
    assert login_test_cases["预期结果"] in driver_manager.driver.page_source
    logger.info(f"测试用例 {login_test_cases['用例标题']} 执行成功")


def test_search_video(search_test_cases):
    logger.info(f"执行测试用例: {search_test_cases['用例标题']}")
    # 初始化页面对象
    main_page = MainPage()
    search_page = SearchPage()

    # 测试步骤
    main_page.open_url()
    search_page.search(search_test_cases["测试数据"].get("keyword"))

    # 验证预期结果
    assert search_test_cases["预期结果"] in driver_manager.driver.page_source
    logger.info(f"测试用例 {search_test_cases['用例标题']} 执行成功")


def test_play_video(video_test_cases):
    logger.info(f"执行测试用例: {video_test_cases['用例标题']}")
    # 初始化页面对象
    main_page = MainPage()
    search_page = SearchPage()
    watch_page = WatchPage()

    # 测试步骤
    main_page.open_url()
    search_page.search("高等数学")
    watch_page.go_to_watch()

    # 验证预期结果
    assert video_test_cases["预期结果"] in driver_manager.driver.page_source
    logger.info(f"测试用例 {video_test_cases['用例标题']} 执行成功")


def test_send_bullet_chat(bullet_chat_test_cases):
    logger.info(f"执行测试用例: {bullet_chat_test_cases['用例标题']}")
    # 初始化页面对象
    main_page = MainPage()
    search_page = SearchPage()
    watch_page = WatchPage()

    # 测试步骤
    main_page.open_url()
    search_page.search("高等数学")
    watch_page.go_to_watch()
    watch_page.send_bullet_chat(bullet_chat_test_cases["测试数据"].get("bullet_chat"))

    # 验证预期结果
    assert bullet_chat_test_cases["预期结果"] in driver_manager.driver.page_source
    logger.info(f"测试用例 {bullet_chat_test_cases['用例标题']} 执行成功")