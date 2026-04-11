from playwright.sync_api import Page, expect
import allure
from typing import Pattern
from tools.logger import get_logger

logger = get_logger('BASE_ELEMENT')


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    #Проверяем что мы попали по нужной нам ссылке 
    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking current url matches pattern "{expected_url.pattern}"'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)