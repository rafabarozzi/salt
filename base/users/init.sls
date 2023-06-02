user_rafael:
  user.present:
    - name: rafael
    - fullname: Rafael Barozzi
    - shell: /bin/bash
    - home: /home/rafael
    - uid: 10000
    - groups:
      - wheel

rafael_key:
  ssh_auth.present:
    - name: rafael
    - user: rafael
    - source: ssh://users/keys/rafael.pub