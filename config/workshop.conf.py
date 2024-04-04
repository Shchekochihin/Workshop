[program:workshop]
command=/home/artem/venv/bin/gunicorn workshop.wsgi:application -c /home/artem/workshop/config/gunicorn.conf.py
directory=/home/artem/workshop
user=artem
autorestart=true
redirect_stderr=true
stdout_logfile = /home/artem/workshop/logs/debug.log