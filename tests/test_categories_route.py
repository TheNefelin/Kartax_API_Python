def test_get_categories(client):
    response = client.get("/categories/")
    assert response.status_code == 200
    data = response.json()
    assert data["isSuccess"] is True
    assert isinstance(data["data"], list)

def test_get_category(client):
    # Primero crea una categoría para asegurarte que exista
    payload = {"name": "Category Get", "img": "img.png"}
    create_resp = client.post("/categories/", json=payload)
    category_id = create_resp.json()["data"]["id"]

    response = client.get(f"/categories/{category_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == category_id

def test_create_category(client):
    payload = {"name": "Category Create", "img": "test_image.png"}
    response = client.post("/categories/", json=payload)

    assert response.status_code in (200, 201)
    data = response.json()
    assert "id" in data["data"]   # Aquí accedemos al dict interno "data"
    assert data["data"]["name"] == "Category Create"
    assert data["data"]["img"] == "test_image.png"

def test_update_category(client):
    # Crear categoría para actualizar
    payload = {"name": "Category Update", "img": "img.png"}
    create_resp = client.post("/categories/", json=payload)
    category_id = create_resp.json()["data"]["id"]

    update_payload = {"name": "Updated Name", "img": "updated_img.png"}
    response = client.put(f"/categories/{category_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["name"] == "Updated Name"


def test_patch_category(client):
    # Crear categoría para patch
    payload = {"name": "Category Patch", "img": "img.png"}
    create_resp = client.post("/categories/", json=payload)
    category_id = create_resp.json()["data"]["id"]

    patch_payload = {"name": "Patched Name"}
    response = client.patch(f"/categories/{category_id}", json=patch_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["name"] == "Patched Name"

def test_delete_category(client):
    # Crear categoría para borrar
    payload = {"name": "Category Delete", "img": "img.png"}
    create_resp = client.post("/categories/", json=payload)
    category_id = create_resp.json()["data"]["id"]

    response = client.delete(f"/categories/{category_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["isSuccess"] is True

    # Verificar que ya no exista
    get_response = client.get(f"/categories/{category_id}")
    assert get_response.status_code == 404    