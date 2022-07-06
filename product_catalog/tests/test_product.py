import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
class TestProductsCRUDClass:

    def test_create_product(self):
        user = User.objects.create_user('test_user', password='test_password')
        client.force_login(user)

        payload = dict(
            name="Test product",
            price=123
        )

        response = client.post("/products/", payload)
        assert response.status_code == 201

        data = response.data
        assert data['name'] == payload['name']
        assert data['price'] == payload['price']

        self.product_id = data['id']
        pass

    def test_read_product(self):
        user = User.objects.create_user('test_user', password='test_password')
        client.force_login(user)

        payload = dict(
            name="Test product",
            price=123
        )

        response = client.post("/products/", payload)
        response = client.get(f"/products/{response.data['id']}/")

        assert response.status_code == 200

        data = response.data
        assert data['name'] == payload['name']
        assert data['price'] == payload['price']
        pass

    def test_update_product(self):
        user = User.objects.create_user('test_user', password='test_password')
        client.force_login(user)

        payload = dict(
            name="Test product",
            price=123
        )

        response = client.post("/products/", payload)
        data = response.data

        payload = dict(name="Test product patched")
        response = client.patch(f"/products/{data['id']}/", payload)

        assert response.status_code == 200

        data = response.data
        assert data['name'] == payload['name']
        pass

    def test_delete_product(self):
        user = User.objects.create_user('test_user', password='test_password')
        client.force_login(user)

        payload = dict(
            name="Test product",
            price=123
        )

        response = client.post("/products/", payload)
        data = response.data

        response = client.delete(f"/products/{data['id']}/")
        assert response.status_code == 204
        pass


@pytest.mark.django_db
class TestRatingsCRUDClass:

    def test_create_rating(self):
        user = User.objects.create_user('test_user', password='test_password')
        client.force_login(user)

        payload = dict(
            name="Test product",
            price=123
        )

        response = client.post("/products/", payload)

        payload = dict(value=4.0, product=response.data['id'])
        response = client.post("/ratings/", payload)

        assert response.status_code == 201

        data = response.data
        assert data['value'] == payload['value']
        assert data['product'] == payload['product']

    @pytest.mark.xfail(
        reason="The fields user, product must make a unique set."
    )
    def test_duplicate_rating_creation_not_allowed(self):
        user = User.objects.create_user('test_user', password='test_password')
        client.force_login(user)

        payload = dict(
            name="Test product",
            price=123
        )

        response = client.post("/products/", payload)

        payload = dict(value=4.0, product=response.data['id'])
        client.post("/ratings/", payload)
        response = client.post("/ratings/", payload)

        assert response.status_code == 400

    def test_update_rating(self):
        user = User.objects.create_user('test_user', password='test_password')
        client.force_login(user)

        payload = dict(
            name="Test product",
            price=123
        )

        response = client.post("/products/", payload)
        payload = dict(value=4.0, product=response.data['id'])
        response = client.post("/ratings/", payload)

        data = response.data
        patch_payload = dict(value=5.0)
        response = client.patch(f"/ratings/{data['id']}/", patch_payload)

        assert response.status_code == 200

        data = response.data
        assert data['value'] == patch_payload['value']
        assert data['product'] == payload['product']

    def test_delete_rating(self):
        user = User.objects.create_user('test_user', password='test_password')
        client.force_login(user)

        payload = dict(
            name="Test product",
            price=123
        )

        response = client.post("/products/", payload)
        payload = dict(value=4.0, product=response.data['id'])
        response = client.post("/ratings/", payload)
        response = client.delete(f"/ratings/{response.data['id']}/")

        assert response.status_code == 204
        pass

    @pytest.mark.xfail(reason="Ensure this value is less than or equal to 5.0.")
    def test_rating_value_range(self):
        user = User.objects.create_user('test_user', password='test_password')
        client.force_login(user)

        payload = dict(
            name="Test product",
            price=123
        )

        response = client.post("/products/", payload)
        payload = dict(value=10.0, product=response.data['id'])
        response = client.post("/ratings/", payload)

        assert response.status_code == 400

    def test_average_rating_on_product(self):
        user1 = User.objects.create_user(
            'test_user_1',
            password='test_password'
        )
        user2 = User.objects.create_user(
            'test_user_2',
            password='test_password'
        )

        client.force_login(user1)
        payload = dict(
            name="Test product",
            price=123
        )
        product_response = client.post("/products/", payload)

        rating_payload_1 = dict(value=1.0, product=product_response.data['id'])
        client.post('/ratings/', rating_payload_1)

        client.force_login(user2)

        rating_payload_2 = dict(value=5.0, product=product_response.data['id'])
        client.post('/ratings/', rating_payload_2)

        product_response = client.get(
            f"/products/{product_response.data['id']}/"
        )

        assert product_response.status_code == 200
        assert product_response.data['average_rating'] == 3
