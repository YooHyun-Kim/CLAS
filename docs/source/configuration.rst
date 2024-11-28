Configuration Guide
===================

This guide explains the configuration options, default settings, and methods for customizing the **Black and White Chef** project.

Configuration Options:
----------------------

1. **Database Settings**:
   - **Default**: The project uses a PostgreSQL database.
   - **Customization**:
     - To use a different database (e.g., MySQL or SQLite), update the `DATABASES` configuration in `settings.py`:
       ```python
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.mysql',
               'NAME': 'Bae',
               'USER': 'Bae',
               'PASSWORD': '1234',
               'HOST': 'localhost',
               'PORT': '3306',
           }
       }
       ```

2. **Frontend Theme**:
   - **Default**: The project uses a minimalistic theme.
   - **Customization**:
     - To customize the theme, edit the CSS files located in `static/css`:
       ```
       static/css/theme.css
       ```

3. **User Authentication**:
   - **Default**: Basic username and password authentication.
   - **Customization**:
     - To enable third-party authentication (e.g., Google or GitHub), add and configure the corresponding OAuth libraries in `settings.py`.

Default Settings:
-----------------

1. **Server Port**:
   - Default: The server runs on port `8000`.
   - To change the port, run the server with the `--port` option:
     ```
     python manage.py runserver 8080
     ```

2. **Debug Mode**:
   - Default: `DEBUG = True` during development.
   - For production, set `DEBUG = False` in `settings.py`:
     ```python
     DEBUG = False
     ```

Customization Methods:
----------------------

1. **Environment Variables**:
   - Store sensitive data such as API keys, database credentials, and debug mode settings in environment variables.
   - Use a `.env` file and the `python-decouple` package for easy management:
     ```
     DATABASE_PASSWORD=your_password
     DEBUG=False
     ```

2. **Localization**:
   - The project supports multiple languages.
   - To add a new language, create a new `.po` file in the `locale` directory and update `settings.py` with the new language code:
     ```python
     LANGUAGES = [
         ('en', 'English'),
         ('ko', 'Korean'),
     ]
     ```

3. **Logging**:
   - Configure logging settings in `settings.py` to track errors or custom events:
     ```python
     LOGGING = {
         'version': 1,
         'disable_existing_loggers': False,
         'handlers': {
             'file': {
                 'level': 'DEBUG',
                 'class': 'logging.FileHandler',
                 'filename': 'debug.log',
             },
         },
         'loggers': {
             'django': {
                 'handlers': ['file'],
                 'level': 'DEBUG',
                 'propagate': True,
             },
         },
     }
     ```

By following this guide, you can configure and customize the **Black and White Chef** project to suit your needs.
