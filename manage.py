#!/usr/bin/env python
"""
manage.py: Django's command-line utility for app administrative tasks.

Django app created to meet the requirements of CS50W-2020 Final project

ChangeLog(v1.09):
- Ran `pip freeze > requirements.txt` to create requirements file.
- Created `docker-compose.yml`,`Dockerfile`,`wait-for-it.sh`, & `startFrontRoyalOutdoors.sh` files.
- Ran `docker-compose up` to test. System now working in docker. Cmd `docker-compose up -d` also ok
- settings.py: Changed "DATABASES" setting `'HOST': '127.0.0.1',` to `'HOST': 'db',` to configure
for Docker environment.
- settings.py: ALLOWED_HOSTS changed to `ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]` for Docker.
- Changed postgres password lines in `settings.py` & `docker-compose.yml`. Old settings commented.
- riverRent/admin.py: Registered models `User` & `Trip_Details`.
- Changed all Trip_Details to Trip_Detail in `model.py`, `views.py`, `admin.py`, & populate.py`.
- Deleted then re-ran makemigrations, migrate and DB populate script.
- riverRent/models.py: Added `def __str__(self):` to Trip_Detail model.
- riverRent/models.py: Added datetime & timezone Python imports.
- riverRent/models.py: Defined admin display return formats for all models.
- settings.py: Removed local PostgreSQL server password & hostname, leaving only Docker settings.


Thoughts:
- Might also add mid-week discounts. Not absolutely necessary.
- Could have server also do price total calculation from trip/boat data sent on check out, & not
accept if value differs from what is sent from local storage. Probably should be added for security
in production environment.
- Still is known data issue where our number calculations may not accurately reflect actual boat
count, due to boats that may be out on multi day trips. No one would really notice this bug right
now, so I might decide to submit anyhow. Will need fix if ever in production. In theory, this
could be fixed by pulling invoice lines for last three days in `views.py(avail)`, & add calc to
take into account. Might be better to re-design database to have reservations table that holds
counts for boats reserved for given date to be populated as selected, & do calc from it if exists.
Otherwise calculations would proceed as is. This would be a bit like a cache in a way. This could
potentially run faster, as less data needs to be pulled from DB, & calc may be less intense. It is
possible that some of the bugs fixed since `v1.08-changeDateAfterAdjustToZeroBug` backup would not
exist, but suspect that most will.


Attributions:
- Many of the pictures were used with permission of `frontroyaloutdoors.com`, and cannot be used
without written permission.
- Info about a way to handle phone numbers came from:
https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
which referenced: https://github.com/stefanfoulis/django-phonenumber-field. Installed app.
- Info about running a script in the Django environment to populate DB can be found on:
`https://django-extensions.readthedocs.io/en/latest/` (see <project_root>/scripts/populate.py`).
- Idea to outline text for readability came from:
https://stackoverflow.com/questions/4919076/outline-effect-to-text
- Used flatpickr datetime picker plugin found on `https://flatpickr.js.org/` &
`https://github.com/flatpickr/flatpickr`. Used from CDN `https://cdn.jsdelivr.net/npm/flatpickr`.
Software is released under MIT license (see `LICENSE-flatpickr.md`).
- Found 'wait-for-it.sh` listed in Docker docs at:
`https://docs.docker.com/compose/startup-order/` && `https://github.com/Eficode/wait-for`

"""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frontroyaloutdoors.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
