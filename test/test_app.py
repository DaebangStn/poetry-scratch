import pytest
from poetry_scratch.function import f


def test_f_has_system_exit():
    with pytest.raises(SystemExit):
        f()
