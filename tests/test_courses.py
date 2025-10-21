import pytest
from playwright.sync_api import expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
        page = chromium_page_with_state
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_drawer = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_drawer).to_be_visible()
        expect(courses_drawer).to_have_text('Courses')

        view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(view_title).to_be_visible()
        expect(view_title).to_have_text('There is no results')

        view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(view_icon).to_be_visible()

        view_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(view_text).to_be_visible()
        expect(view_text).to_have_text('Results from the load test pipeline will be displayed here')