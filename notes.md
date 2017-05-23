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
*To use particular version of Python*
```bash
    virtualenv -p python3 venv
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

#### Work in Python/Django shell

6. Run a python shell
```bash
    python manage.py shell
```
7. Import models
```bash
    >>> from main_app.models import Treasure
```
8. List all Treasure objects
```bash
    >>> Treasure.objects.all()
```
9. Or filter some Treasure objects
```bash
    Treasure.objects.filter(location = 'Orlando, FL')
```
10. Get an element
```bash
    Treasure.objects.get(pk = 1)
```
11. Create an object
```bash
    t = Treasure(name='Coffee Can', value=20.00, location='Acme, CA', material='tin', img_url='...')
```
12. Save the object to db
```bash
    t.save()
```
13. Delete object from db
```bash
    Treasure.objects.filter(pk = 4).delete()
```
14. Update object/entry's field in db
```bash
    t = Treasure.objects.get(pk = 1)
    t.name = "new_name"
    t.save(update_fields=['name'])
```
15. Count objects/entries in db
 ```bash
     Treasure.objects.count()
```

#### Django Admin

17. Create superuser
```bash
    python manage.py createsuperuser
```
18. Register models in admin.py
```python
    from .models import Treasure
    
    admin.site.register(Treasure)
```

##### Fixtures
```bash
    python manage.py loaddata www/fixtures/team.json
```

#### Cloud9

Once your workspace has been created, perform a migrate then start the Django server from the terminal (bind to host $IP and port $PORT):
```bash
    python manage.py migrate
    python manage.py runserver $IP:$PORT
```