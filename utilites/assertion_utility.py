import allure
from hamcrest import equal_to, assert_that, is_, empty, not_


class AssertionUtility:

    def __init__(self):
        self.error_list = []

    @allure.step
    def clear_errors(self):
        self.error_list = []

    @allure.step
    def assert_no_errors(self):
        self.assert_empty(self.error_list)

    @allure.step
    def softly_assert_equal(self, actual, expected):
        try:
            self.assert_equal(actual, expected)
        except AssertionError as assertion_error:
            self.error_list.append(str(assertion_error))

    @allure.step
    def softly_assert_not_empty(self, actual):
        try:
            self.assert_not_empty(actual)
        except AssertionError as assertion_error:
            self.error_list.append(str(assertion_error))

    @classmethod
    @allure.step
    def assert_equal(cls, actual, expected):
        assert_that(actual, equal_to(expected))

    @classmethod
    @allure.step
    def assert_empty(self, actual):
        assert_that(actual, is_(empty()))

    @classmethod
    @allure.step
    def assert_not_empty(cls, actual):
        assert_that(actual, is_(not_(empty())))