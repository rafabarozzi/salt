{% for user, data in pillar.get('admin_users', {}).items() %}
user_{{ user }}:
  user.present:
    - name: {{ user }}
    - fullname: {{ data['fullname'] }}
    - shell: {{ data['shell'] }}
    - home: {{ data['home'] }}
    - uid: {{ data['uid']}}
    - groups: {{ data['groups'] }}

{{ user }}_key:
  ssh_auth.present:
    - name: {{ data['ssh_key'] }}
    - user: {{ user }}

{% endfor %}}