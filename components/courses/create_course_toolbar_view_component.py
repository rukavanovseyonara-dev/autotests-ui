from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_exercise_button = Button(page, 'create-course-toolbar-create-course-button', 'Button')

    def check_visible(self, is_create_course_disabled: bool = True):
        if is_create_course_disabled:
            self.create_exercise_button.check_enabled()

        if not is_create_course_disabled:
            self.create_exercise_button.check_disabled()

    def click_create_course_button(self):
        self.create_exercise_button.check_visible()
        self.create_exercise_button.click()
