#!/bin/bash
echo "Starting Django server"
echo "Change ownership of /media/uploads to 1000:1000"
chown -R 1000:1000 /media/uploads
echo "Run Django server"
python manage.py runserver 0.0.0.0:8000