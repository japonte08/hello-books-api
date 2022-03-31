# def test_get_one_book(client, two_saved_books):
#     # Act
#     response = client.get("/books/1")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 200
#     assert response_body == {
#         "id": 1,
#         "title": "Ocean Book",
#         "description": "watr 4evr"
#     }

# def test_create_one_book(client):
#     # Act
#     response = client.post("/books", json={
#         "title": "New Book",
#         "description": "The Best!"
#     })
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 201
#     assert response_body == "Book New Book successfully created"

# @pytest.fixture
# def two_saved_books(app):
#     # Arrange
#     ocean_book = Book(title="Ocean Book",
#                       description="watr 4evr")
#     mountain_book = Book(title="Mountain Book",
#                          description="i luv 2 climb rocks")

#     db.session.add_all([ocean_book, mountain_book])
#     # Alternatively, we could do
#     # db.session.add(ocean_book)
#     # db.session.add(mountain_book)
#     db.session.commit()