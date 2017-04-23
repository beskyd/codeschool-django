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