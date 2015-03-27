# HOW-TO START

Build image:

```bash
$ docker build -t djangotpl .
```

Run container:

```bash
$ docker run -p 8000:8000 -d --name djangotpl djangotpl
```

Login into a running container:

```bash
$ docker exec -ti djangotpl /bin/sh
```

Install project dependencies:

```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

Now you can run Django dev-server:

```bash
$ DJANGO_SETTINGS_MODULE=config.settings.dev python manage.py runserver 0:8000
```

or run appserver by uwsgi:

```bash
$ DJANGO_SETTINGS_MODULE=config.settings.dev uwsgi --http :8000 --module config.wsgi
```


# STRUCTURE

Directories structure::

    www.example.com/             # ROOT_DIR
        ansible/
        application/             # BASE_DIR (application's source files)
            apps/                # APPS_DIR (custom django apps)
            config/
                settings/
                urls.py
                wsgi.py
            common/              # general modules
            static/              # site-specific static files (added to the STATICFILES_DIRS)
            templates/           # site-specific templates
            tests/               # site-specific tests (mostly in-browser ones)
        docs/
        etc/                     # The etc folder holds all files related to the server configuration of the project.
                                 # The files contained within are symlinked to the appropriate locations on the
                                 # dev/production server.
            nginx/
            supervisord/
            uwsgi/
        site/                    # The site root functions as a container for a specific deployment. All the files it
                                 # contains are those that will vary from deployment to deployment, and most importantly
                                 # will change during the running of the site -- log files, user uploads, filesystem-based
                                 # caches and PID files all fall into this category.
            db/
            logs/
            media/               # uploaded media files; MEDIA_ROOT
            static/              # compiled static files (collected by collectstatic); STATIC_ROOT
            tmp/
        tools/                   # tools and scripts for maintenance work
            scripts/
