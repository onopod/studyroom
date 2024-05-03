rm -f api/migrations/0001_initial.py
rm -f db.sqlite3
/usr/bin/python3 manage.py makemigrations > /dev/null
/usr/bin/python3 manage.py migrate > /dev/null
