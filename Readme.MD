Built by Daniel Oluwajuwon

### Activation Virtualenv

`python -m venv env`

## if you are using windows

`env\Scripts\activate`

### Other OS

`source env/bin/activate`

### installing packages ( make sure you are in the root folder)

`pip install -r requirements.txt`

### Run

`python manage.py runserver `

### Run Task on Windows

- (If on Mac ) celery -A BincomTest worker --loglevel=info
- (If on Windows) celery -A BincomTest worker -l info --pool=solo

### open another tab

- `celery -A BincomTest beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
