
import pytest
from yandex_api import create_folder


def test_create_folder():
    status_1 = 201
    status_2 = 409
    path = '/80'
    res = create_folder(path)
    assert res == status_1

    res = create_folder(path)
    assert res == status_2