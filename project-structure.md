```
src/
├── backend/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── recipe.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── recipes.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   ├── main.css
│   │   │   └── recipe.css
│   │   ├── js/
│   │   │   ├── main.js
│   │   │   └── recipe.js
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       └── recipes/
│           ├── list.html
│           ├── detail.html
│           └── create.html
└── tests/
    ├── __init__.py
    ├── test_auth.py
    └── test_recipes.py
```
