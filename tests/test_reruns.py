import random

import pytest

@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_reruns():
    assert random.choice([True, False])
