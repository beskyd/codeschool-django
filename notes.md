### `virtualenv`

---

1. Install `virtualenv`
```bash
    pip install virtualenv
```
2. Create a new virtual environment called `venv`
```bash
    virtualenv venv
```
3. Activate virtual environment `venv`
```bash
    source venv/bin/activate
```
4. To install version `1.7` of Django type
```bash
    pip install Django==1.7
```
5. To see what is currently istalled in this environment type
```bash
    pip freeze
```
6. To deactivate virtual environment `venv` type
```bash
    deactivate venv
```

### Django

---

1. Create new project `Treasuregram`
```bash
    django-admin startproject Treasuregram
```
2. Run created project
```bash
    python manage.py runserver
```
3. Create an app inside our Treasuregram project
```bash
    python manage.py startapp main_app
```

#### Perform a migration

4. Make a migration file
```bash
    python manage.py makemigrations
```

*Optionally you could preview the SQL commands before applying the migration*
```bash
    python manage.py sqlmigrate app_name migration
```
*like so*
```bash
    python manage.py sqlmigrate main_app 0001
```

5. Apply the migration to the db
```bash
    python manage.py migrate
```