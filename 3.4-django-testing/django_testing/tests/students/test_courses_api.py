import pytest
from rest_framework.test import APIClient
from students.models import Course


@pytest.mark.django_db
def test_get_courses():
    Course.objects.create(name="Python")
    Course.objects.create(name="Django")

    client = APIClient()
    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_get_course_by_id():
    course = Course.objects.create(name="Python")

    client = APIClient()
    response = client.get(f'/api/v1/courses/{course.id}/')

    assert response.status_code == 200
    assert response.data['name'] == "Python"


@pytest.mark.django_db
def test_create_course():
    client = APIClient()
    response = client.post('/api/v1/courses/', {'name': 'Flask'})

    assert response.status_code == 201
    assert response.data['name'] == 'Flask'


@pytest.mark.django_db
def test_update_course():
    course = Course.objects.create(name="Old")

    client = APIClient()
    response = client.patch(f'/api/v1/courses/{course.id}/', {'name': 'New'})

    assert response.status_code == 200
    assert response.data['name'] == 'New'


@pytest.mark.django_db
def test_delete_course():
    course = Course.objects.create(name="Delete me")

    client = APIClient()
    response = client.delete(f'/api/v1/courses/{course.id}/')

    assert response.status_code == 204
