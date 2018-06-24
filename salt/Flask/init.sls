{% set site_user = 'ubuntu' %}
{% set site_group = 'ubuntu' %}
{% set site_name = 'fibnocci' %}
{% set project_name = 'fib_test' %}
{% set sites_dir = '/fib-flask' %}

pre_requisites:
  pkg.installed:
    - pkgs:
       - python-pip
       - python-dev
       - nginx
  pip.installed:
    - pkgs: 
        - flask
        - uwsgi
        - Flask
        - gunicorn

flask-user-group:
  user.present:
    - name: {{ site_user }}
    - gid_from_name: True
    - system: True

  group.present:
    - name: {{ site_group }}
    - system: True


/fib-flask:
  file.directory:
    - user: {{ site_user }}
    - group: {{ site_group }}
    - require:
       - user : flask-user-group
       - pkg : pre_requisites


flask-source:
  file.recurse:
    - name: {{ sites_dir }}/{{ site_name }}
    - user: {{ site_user }}
    - dir_mode: 2775
    - file_mode: '0644'
    - template: jinja
    - source: salt://Flask/fibnocci/
    - include_empty: True

#### Gunicorn process as systemd service

gunicorn-config:
  file.managed:
    - name: /etc/systemd/system/fib.service
    - source: salt://Flask/config/fib.service
    - template: jinja
    - context:
        path: '{{ sites_dir }}/{{ site_name }}'

daemon_reload:
  cmd.run:
    - name: "systemctl daemon-reload"
    - onchanges:  
        - file: gunicorn-config
  service.running:
    - name: fib
    - enable: True
    - restart: True
    - watch:
      - file: flask-source

nginx-ssl-changes:
  file.recurse:
    - name: /etc/nginx/ssl/
    - user: {{ site_user }}
    - dir_mode: 2775
    - file_mode: '0644'
    - template: jinja
    - source: salt://Flask/nginx/ssl
    - include_empty: True

nginx-changes:
  file.managed:
    - name: /etc/nginx/sites-available/default
    - source: salt://Flask/nginx/default
    - template: jinja

nginx-service:
  service.running:
    - name: nginx
    - enable: True
    - restart: True
    - watch:
      - file: nginx-changes
      - file: nginx-ssl-changes

