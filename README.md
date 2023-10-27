# DjangoEssentialTrainingLinkedInCourse

Exercises for Django Essential Training Linkedin Course

django-admin startproject name .
django-admin startapp home

Model View Template framework MVT

# run server

> python manage.py runserver

1. Views handle requests and responses
2. Model handles data and how it's stored
3. Template allows us to render DB info to HTML pages; using DTL (Django Template Language) to define pages;
   Templates -> interpreter -> html (interpreter adds the vars to html)

    # app is a small library inside of django project; we can have as many as we want so it can become chaotic

    # it should all be modularized really good

    # all for a single app in the same folder, ideally if you would to delete the app, the folder, nothing breaks

Migrations use command Migrate

# run migration

> python manage.py migrate

# create super user for db

> python manage.py createsuperuser

Django uses an ORM; we need class models that will be transformed with migrations to tables; each attribute is a column
Classes -> make migrations -> migrations -> database
Django's ORM is one of the best Python and SQL ORMs

# Create migrations

> python manage.py makemigrations

# Python shell

> python manage.py shell
>
> > > from notes.models import Notes
> > > mynote = Notes.objects.get(pk='1')
> > > mynote.title
> > > mynote.text
> > > Notes.objects.all()
> > > new_note = Notes.objects.create(title="A second note", text="This is a second note")
> > > Notes.objects.all()
> > > Notes.objects.filter(title**startswith="My") # ** is \_\_
> > > Notes.objects.filter(title**startswith="Django")
> > > Notes.objects.filter(text**icontains='Django')
> > > Notes.objects.exclude(text**icontains='Django')
> > > Notes.objects.filter(text**icontains='Django').exclude(title\*\*icontains='Django')
