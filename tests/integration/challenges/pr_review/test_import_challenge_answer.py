from types import SimpleNamespace
import pytest

from tests.integration.challenges.pr_review.base import run_tests

PR_LINK = "https://github.com/merwanehamadi/Auto-GPT/pull/136"
PARAMETERS = SimpleNamespace(
    source_branch_name="import-challenge-answer",
    source_repo_user="merwanehamadi",

    # PR information
    title="import-challenge-answer",
    body="import-challenge-answer",

    # PR success criteria
    approved=False,
    pr_number=136,
    review_contains=["import"],
)

# @pytest.skip("skip")
def test_import_challenge_answer() -> None:
    run_tests(PARAMETERS)
