Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess beheerconsole-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/beheerconsole/log/apache2/error.log"
        CustomLog "/srv/sites/beheerconsole/log/apache2/access.log" common

        WSGIProcessGroup beheerconsole-<target>

        Alias /media "/srv/sites/beheerconsole/media/"
        Alias /static "/srv/sites/beheerconsole/static/"

        WSGIScriptAlias / "/srv/sites/beheerconsole/src/beheerconsole/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-beheerconsole-<target>]
    user = <user>
    command = /srv/sites/beheerconsole/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/beheerconsole/src/beheerconsole/wsgi/wsgi_<target>.py
    home = /srv/sites/beheerconsole/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/beheerconsole/log/uwsgi_err.log
    stdout_logfile = /srv/sites/beheerconsole/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_beheerconsole_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/beheerconsole/log/nginx-access.log;
      error_log /srv/sites/beheerconsole/log/nginx-error.log;

      location /500.html {
        root /srv/sites/beheerconsole/src/beheerconsole/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/beheerconsole/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/beheerconsole/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_beheerconsole_<target>;
      }
    }
