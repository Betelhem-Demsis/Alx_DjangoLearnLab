# Permissions and Groups Setup

This Django application uses custom permissions and groups to control access to various parts of the application.

## Groups and Permissions:
- **Editors**: Can create and edit book.
- **Viewers**: Can view book.
- **Admins**: Can view, create, edit, and delete instances.

## Usage:
Permissions are enforced in views using the `permission_required` decorator. Users must belong to the appropriate group to access these views.
