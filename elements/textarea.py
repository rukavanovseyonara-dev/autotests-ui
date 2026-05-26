from ui_coverage_tool import ActionType

from elements.base_element import BaseElement
from playwright.sync_api import expect, Locator
import allure
from tools.logger import get_logger

logger = get_logger('BASE_ELEMENT')


class TextArea(BaseElement):
    @property
    def type_of(self) -> str:
        return 'textarea'

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator("textarea").first

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'
        self.track_coverage(ActionType.FILL)
        self.get_locator().fill(value)

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has "{value}"'
        self.track_coverage(ActionType.VALUE)
        assert self.get_locator().input_value() == value

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)
