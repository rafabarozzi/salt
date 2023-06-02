user_rafael:
  user.present:
    - name: barozzidev
    - fullname: Dev Barozzi
    - shell: /bin/bash
    - home: /home/barozzidev
    - uid: 10001
    - groups:
      - wheel

rafael_key:
  ssh_auth.present:
    - name: barozzidev
    - user: barozzidev
    - source: ssh://users/keys/barozzidev.pub