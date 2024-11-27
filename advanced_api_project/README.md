# Book API Documentation

## Overview
This API allows users to manage books with the following endpoints:
- List all books
- Retrieve details of a specific book
- Create a new book
- Update an existing book
- Delete a book

## Permissions
- **List and Detail Views**: Accessible to all users, including unauthenticated users.
- **Create, Update, and Delete Views**: Restricted to authenticated users.

## Endpoints
1. **List Books**
   - URL: `/api/books/`
   - Method: `GET`
   - Permission: Public
   - Description: Retrieve a list of all books.

2. **Retrieve Book Details**
   - URL: `/api/books/{id}/`
   - Method: `GET`
   - Permission: Public
   - Description: Retrieve details of a specific book.

3. **Create Book**
   - URL: `/api/books/`
   - Method: `POST`
   - Permission: Authenticated users only
   - Description: Create a new book. Requires the following fields:
     - `title`
     - `publication_year`
     - `author`

4. **Update Book**
   - URL: `/api/books/{id}/`
   - Method: `PUT`
   - Permission: Authenticated users only
   - Description: Update the details of an existing book.

5. **Delete Book**
   - URL: `/api/books/{id}/`
   - Method: `DELETE`
   - Permission: Authenticated users only
   - Description: Delete an existing book.

## Testing
- Use Postman or curl to test each endpoint.
- Ensure that permissions are enforced correctly for each endpoint.
