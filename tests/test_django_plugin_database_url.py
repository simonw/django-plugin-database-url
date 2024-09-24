from django.test.client import Client


def test_index_page_200():
    response = Client().get("/")
    assert response.status_code == 200


# Testing settings.DATABASES here is hard because the pytest-django
# mechanisms replace what was configured with a in-memory test DB
