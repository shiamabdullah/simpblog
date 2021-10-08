# A simple blog 
A simple blog side made with django. Where user can post blogs and see them. \
It is hosted on pythonanywhere.com.
For a quick peek of the site visit: \
http://blogshiamify.pythonanywhere.com/

<a href="https://ibb.co/qxPy5pm"><img src="https://i.ibb.co/qxPy5pm/Screenshot-1257.png" alt="Screenshot-1257" border="0"></a>
#### Technologies

- Django
- HTML/CSS
- Sqlite

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r https://raw.githubusercontent.com/juanifioren/django-project-template/master/requirements.txt

# You may want to change the name `projectname`.
$ django-admin startproject --template https://github.com/juanifioren/django-project-template/archive/master.zip projectname

$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py migrate
$ python manage.py runserver
```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* Split settings in two files. `settings_custom.py` for specific environment settings (localhost, production, etc). `projectname/settings.py` for core settings.
* Simple logging setup ready for production envs.

## Contributing
I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request

## Author Info

- Facebook - [@shiam.abdullah1](https://www.facebook.com/shiamabdullah1/)
- Website - [Shiamify](https://boring-euclid-df9d83.netlify.app/)
