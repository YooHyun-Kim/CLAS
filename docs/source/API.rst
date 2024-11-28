API
==============
Overview
The CLAS API provides programmatic access to recipe sharing, user management, and platform features.
Authentication
All API requests require authentication using JWT tokens.
Authentication Header

.. code-block:: http

    Authorization: Bearer <your_access_token>

Base Endpoints
--------------

User Management
~~~~~~~~~~~~~~~

Register User
^^^^^^^^^^^^^
* **Endpoint:** ``/api/v1/users/register``
* **Method:** POST
* **Request Body:**

.. code-block:: json

    {
        "username": "string",
        "email": "string",
        "password": "string",
        "display_name": "string"
    }

* **Response:**

.. code-block:: json

    {
        "user_id": "string",
        "status": "success",
        "token": "jwt_token"
    }

Get User Profile
^^^^^^^^^^^^^^^^
* **Endpoint:** ``/api/v1/users/profile``
* **Method:** GET
* **Response:**

.. code-block:: json

    {
        "user_id": "string",
        "username": "string",
        "tier": "light|black",
        "total_recipes": "integer",
        "total_likes": "integer"
    }

Recipe Endpoints
~~~~~~~~~~~~~~~~

Create Recipe
^^^^^^^^^^^^^
* **Endpoint:** ``/api/v1/recipes/create``
* **Method:** POST
* **Request Body:**

.. code-block:: json

    {
        "title": "string",
        "description": "string",
        "ingredients": ["string"],
        "steps": ["string"],
        "cuisine_type": "string",
        "difficulty_level": "easy|medium|hard"
    }

* **Response:**

.. code-block:: json

    {
        "recipe_id": "string",
        "status": "success"
    }

Get Recipe
^^^^^^^^^^
* **Endpoint:** ``/api/v1/recipes/{recipe_id}``
* **Method:** GET
* **Response:**

.. code-block:: json

    {
        "recipe_id": "string",
        "title": "string",
        "author": "string",
        "likes": "integer",
        "ingredients": ["string"],
        "steps": ["string"]
    }

Like Recipe
^^^^^^^^^^^
* **Endpoint:** ``/api/v1/recipes/{recipe_id}/like``
* **Method:** POST
* **Response:**

.. code-block:: json

    {
        "status": "success",
        "total_likes": "integer"
    }

Ranking Endpoints
~~~~~~~~~~~~~~~~~

Get Tier Rankings
^^^^^^^^^^^^^^^^^
* **Endpoint:** ``/api/v1/rankings``
* **Method:** GET
* **Parameters:**
    - ``tier``: light|black
    - ``page``: integer
    - ``limit``: integer (default 10)

* **Response:**

.. code-block:: json

    {
        "rankings": [
            {
                "user_id": "string",
                "username": "string",
                "total_likes": "integer",
                "rank": "integer"
            }
        ],
        "total_pages": "integer"
    }

Error Handling
--------------
API returns standard HTTP status codes:

* ``200``: Successful request
* ``400``: Bad request
* ``401``: Unauthorized
* ``403``: Forbidden
* ``404``: Not found
* ``500``: Server error

Error Response Format
.. code-block:: json
{
    "error": "string",
    "message": "detailed error description",
    "code": "error_code"
}

Rate Limiting

Maximum 100 requests per minute
Exceeding limit returns 429 Too Many Requests

Webhooks
Real-time event notifications available for:

New recipe creation
User tier changes
Ranking updates

Example Webhook Payload
.. code-block:: json

    {
        "event_type": "recipe_created",
        "data": {
            "recipe_id": "string",
            "user_id": "string"
        },
        "timestamp": "iso8601_datetime"
    }

SDK and Library Support
-----------------------
* Official Python SDK available
* Community-contributed libraries for:
    - JavaScript
    - Ruby
    - Go

Version History
---------------
* ``v1.0.0``: Initial release
* ``v1.1.0``: Added ranking and tier system
* ``v1.2.0``: Enhanced API capabilities
