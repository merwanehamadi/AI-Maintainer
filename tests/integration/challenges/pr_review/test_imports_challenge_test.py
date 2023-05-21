from types import SimpleNamespace
import pytest

from tests.integration.challenges.pr_review.base import run_tests

PARAMETERS = SimpleNamespace(
    source_branch_name="imports-challenge-test",
    source_repo_user="merwanehamadi",

    # PR information
    title="imports-challenge-test",
    body="imports-challenge-test",

    # PR success criteria
    review_contains=[],
    # contains={"bad_variable_name.py": ["variable"]},
)
@pytest.mark.skip("skip")
def test_imports_challenge_test(

) -> None:
    run_tests(PARAMETERS)
