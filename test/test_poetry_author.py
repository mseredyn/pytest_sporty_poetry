import logging
import random

import pytest
from hamcrest import assert_that, equal_to

from utilites.assertion_utility import AssertionUtility

LOGGER = logging.getLogger(__name__)


class TestPoetryAuthor:

    @pytest.fixture(scope="function")
    def get_existing_author(self, poetry_client):
        response = poetry_client.get_authors()
        assert_that(response.status_code, equal_to(200))
        return random.choice(response.json()["authors"])

    def test_poetry_existing_author(self, poetry_client, get_existing_author):
        # fetch existing author
        response = poetry_client.get_author(get_existing_author)
        assertion_utility = AssertionUtility()
        assertion_utility.assert_equal(response.status_code, 200)
        response_body = response.json()
        # assert titles not empty
        assertion_utility.assert_not_empty(response_body)
        # forEch title assert that
        for title_entity in response_body:
            # assert title is not empty
            assertion_utility.softly_assert_not_empty(title_entity["title"])
            # assert author of title is same as author for which title is fetched
            assertion_utility.softly_assert_equal(title_entity["author"], get_existing_author)
            # assert non-empty lines are equal to linecount
            lines = title_entity["lines"]
            lines = list(filter(lambda a: a != "", lines))
            assertion_utility.softly_assert_equal(str(len(lines)), title_entity["linecount"])
        # assert no errors were raised
        assertion_utility.assert_no_errors()

    def test_poetry_non_existing_author(self, poetry_client, get_existing_author):
        # fetch non-existing author
        non_existing_author = f'{get_existing_author}p'
        response = poetry_client.get_author(non_existing_author)
        AssertionUtility.assert_equal(response.status_code, 200)

        # assert message that author does not exist
        response_body = response.json()
        AssertionUtility.assert_equal(response_body["status"], 404)
        AssertionUtility.assert_equal(response_body["reason"], "Not found")
