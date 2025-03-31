# pytest_sporty_poetry

This test framework fetches authors from https://poetrydb.org/

## How to run

* clone repository
* cd into cloned repository
* .\venv\Scripts\activate
* pip install -r requirements.txt
* pytest

## Test cases

### TestPoetryAuthor.test_poetry_non_existing_author

#### Prerequisites:

* name_of_existing_author

#### TestCase Table

| Step                                                      | Expected                                    |
|-----------------------------------------------------------|---------------------------------------------|
| append suffix to name_of_existing_author                  | name_of_non_existing_author created locally |
| get /author with name_of_non_existing_author as pathParam | ok                                          |
| assert response.status_code                               | 200                                         |
| assert response_body["status"]                            | 404                                         |
| assert response_body["reason]                             | Not found                                   |

### TestPoetryAuthor.test_poetry_existing_author

#### Prerequisites:
* name_of_existing_author

#### TestCaseTable
| Step                                                  | Expected                |
|-------------------------------------------------------|-------------------------|
| get /author with name_of_existing_author as pathParam | ok                      |
| assert response.status_code                           | 200                     |
| assert list of titles not empty                       | ok                      |
| forEach title_entity: assert title not empty          | ok                      |
| forEach title_entity: assert author                   | name_of_existing_author |
| forEach title_entity: assert non-empty lines count    | linescount              |
| assert no errors raised in forEach                    | ok                      |
## Validation
PyHamcrest was used as main validation library due to its error readability. 
AssertionUtility was introduced as PyHamcrest wrapper in order to introduce both SoftAssertions and allure report readability.