## API Endpoints

### Books

- `GET /api/books/`: Retrieve a list of all books. Supports filtering by `publication_year` and `author__name`, and ordering by `title` and `publication_year`.
- `POST /api/books/create/`: Create a new book. Requires authentication.
- `GET /api/books/<id>/`: Retrieve details of a specific book.
- `PUT /api/books/<id>/update/`: Update a specific book. Requires authentication and ownership.
- `DELETE /api/books/<id>/delete/`: Delete a specific book. Requires authentication and ownership.

### Permissions

- List and Detail views are accessible to all users (read-only for unauthenticated users).
- Create, Update, and Delete operations require authentication.
- Update and Delete operations also require the requesting user to be the author of the book.

### Filtering and Ordering

The book list endpoint (`/api/books/`) supports the following query parameters:

- `publication_year`: Filter books by publication year
- `author__name`: Filter books by author name
- `ordering`: Order books by `title` or `publication_year` (use `-` for descending order, e.g., `-publication_year`)

Example: `/api/books/?publication_year=2023&ordering=-title`

### Running Unit Tests

To run the unit tests for the Book API, use the following command:

python manage.py test api
