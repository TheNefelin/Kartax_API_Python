from datetime import datetime, timezone
from unittest.mock import MagicMock
from sqlalchemy.exc import SQLAlchemyError
from src.api.categories import crud, schemas

def mock_category_instance():
    mock = MagicMock()
    mock.id = 1
    mock.name = "Mock Category"
    mock.img = "img.png"
    mock.is_enable = True
    mock.created_at = datetime.now(timezone.utc)
    mock.updated_at = datetime.now(timezone.utc)
    return mock

def test_get_categories():
    mock_db = MagicMock()
    mock_db.query().all.return_value = [mock_category_instance()]
    result = crud.get_categories(mock_db)
    assert result.status == "Success"
    assert isinstance(result.data, list)
    assert result.data[0].name == "Mock Category"

def test_get_category_found():
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = mock_category_instance()
    result = crud.get_category(mock_db, 1)
    assert result.status == "Success"
    assert result.data.name == "Mock Category"

def test_get_category_not_found():
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = None
    result = crud.get_category(mock_db, 999)
    assert result.status == "Not Found"

# def test_create_category_success():
#     mock_db = MagicMock()
#     schema = schemas.CategoryCreate(name="New", img="img.png")
#     result = crud.create_category(mock_db, schema)
#     assert result.status == "Created"
#     assert result.data is not None
#     assert hasattr(result.data, "name")
#     assert result.data.name == "New"

def test_create_category_db_error():
    mock_db = MagicMock()
    mock_db.commit.side_effect = SQLAlchemyError("DB Error")
    schema = schemas.CategoryCreate(name="Fail", img="img.png")
    result = crud.create_category(mock_db, schema)
    assert result.status == "Internal Server Error"
    assert "DB Error" in result.message

def test_update_category_found():
    db_obj = mock_category_instance()
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = db_obj
    schema = schemas.CategoryUpdate(name="Updated", img="updated.png")
    result = crud.update_category(mock_db, 1, schema)
    assert result.status == "Success"
    assert result.data.name == "Updated"

def test_update_category_not_found():
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = None
    schema = schemas.CategoryUpdate(name="X", img="X")
    result = crud.update_category(mock_db, 999, schema)
    assert result.status == "Not Found"

def test_patch_category_partial_update():
    db_obj = mock_category_instance()
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = db_obj
    schema = schemas.CategoryPatch(name="Patch Only")
    result = crud.patch_category(mock_db, 1, schema)
    assert result.status == "Success"
    assert result.data.name == "Patch Only"

def test_patch_category_empty_payload():
    db_obj = mock_category_instance()
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = db_obj
    schema = schemas.CategoryPatch()
    result = crud.patch_category(mock_db, 1, schema)
    assert result.status == "Bad Request"

def test_delete_category_success():
    db_obj = mock_category_instance()
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = db_obj
    result = crud.delete_category(mock_db, 1)
    assert result.status == "Success"

def test_delete_category_not_found():
    mock_db = MagicMock()
    mock_db.query().filter().first.return_value = None
    result = crud.delete_category(mock_db, 1)
    assert result.status == "Not Found"
