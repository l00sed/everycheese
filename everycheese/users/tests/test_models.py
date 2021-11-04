import pytest

from everycheese.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    url = f"/users/{user.username}/"
    assert user.get_absolute_url() == url
