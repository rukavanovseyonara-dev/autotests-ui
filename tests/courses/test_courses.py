import allure
import pytest

from config import settings
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)

        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.CREATE_COURSES)
        create_course_page.check_visible_create_course_title()
        create_course_page.check_disable_create_course_button()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form_component.check_visible(
            '', '', '', '0', '0'
        )
        create_course_page.create_course_toolbar.check_visible(False)
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.create_course_exercises_toolbar.click_create_exercise_button()
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form_component.fill(
            'Playwright', '2 weeks', 'Playwright', '100', '10'
        )
        create_course_page.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            0, 'Playwright', '100', '10', '2 weeks'
        )

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.CREATE_COURSES)
        create_course_page.create_course_form_component.fill(
            title="My course",
            estimated_time="3 weeks",
            description="My new course",
            max_score="100",
            min_score="10"
        )
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="My course",
            estimated_time="3 weeks",
            max_score="100",
            min_score="10"
        )
        courses_list_page.course_view_menu_component.click_edit(index=0)
        create_course_page.create_course_form_component.fill(
            title="My course 1",
            estimated_time="2 weeks",
            description="My new course 1",
            max_score="101",
            min_score="11"
        )
        create_course_page.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title="My course 1",
            estimated_time="2 weeks",
            max_score="101",
            min_score="11"
        )
