## Configure Saltstack in Ubuntu 16.04

#### Run:

> wget -O - https://repo.saltstack.com/py3/ubuntu/16.04/amd64/2018.3/SALTSTACK-GPG-KEY.pub | sudo apt-key add - 

Add below content to  
'/etc/apt/sources.list.d/saltstack.list' file :

> deb http://repo.saltstack.com/py3/ubuntu/16.04/amd64/2018.3 xenial main


### To install salt-master,

#### Run: 

> sudo apt-get update

#### Run:

> sudo apt-get -y install salt-master
> mkdir -p /srv/salt /srv/pillar

Add below Content to file:

> -->'/etc/salt/master' 
```
file_roots:
  base:
    - /srv/salt/
pillar_roots:
  base:
    - /srv/pillar
```

Add below Content to file:
> -->'/srv/salt/top.sls'
```
base:
  '*':
    - Flask
```

> sudo systemctl restart salt-master


### To install Salt-minion,


__ Run:
> sudo apt-get update
> sudo apt-get -y install salt-minion

Add below content to file:
> --> '/etc/hosts'  :
``` <IP of salt-master>  salt ```

> sudo systemctl restart salt-minion

once salt-minion is installed in minion server , you can go to salt-master server and have to accept the key using below command:

> salt-key -L --> to display the Keys

> salt-key -a <minion_id> -y ---> to accept the specific minion key
