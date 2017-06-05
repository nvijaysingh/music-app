####Prerequisites

Python 2.7+
virtualenv
pip
bower


####Commands

virtualenv ENV
source ENV/bin/activate
pip install -r requirements.txt
bower install
cd chat_backend/
python manage.py collectstatic
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
