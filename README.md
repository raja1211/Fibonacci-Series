### Fibonacci_series

This Repository Contains Fibonacci-series code and And its Deployment salt-stack formula.

#### System Requirements:
```
OS  :  Ubuntu 16.04.4 LTS
Container : LXC containers
Saltstack-master,minion Version:  2018.3.1+ds-1
<This Formula Don't maintain any Application software version till date,  and if at all requires I will update the Doc>

```
### Salt-stack Master and Minion simple configuration

Follow Below Link to configure a simple salt-Master and Minion.

> https://github.com/raja1211/Fibonacci-Series/blob/master/Salt-MM.md

#### Deploy Code

--> Once Salt-master and Minion setup is done, download git repo to /srv/ folder
```
 cd /tmp/
 git clone https://github.com/raja1211/Fibonacci-Series.git
 cd /tmp/Fibonacci-Series
 cp -r * /srv/
 service salt-master restart
**update your minions IPs in /srv/pillar/Flask/init.sls**
 sudo salt -L <minion1>,<minion2> saltutil.refresh_pillar
 sudo salt -L <minion1>,<minion2> state.sls Flask
```
##### Access
Once Deployment is Done , you can access service as like below

``` http://<minion1>/fib/<int>  [OR]  http://<minion2>/fib/<int> ```
   
**As we have loadbalanacer configured Load will share among the hosts**
**Note: Because we are using Selfsigned certificates, in browser we need to accept the keys.**

##### Installation softwares
   - python-pip
   - python-dev
   - nginx
   
##### Installation pip packages
  - flask
  - uwsgi
  - Flask
  - gunicorn

### Request Flow:

https://github.com/raja1211/Fibonacci-Series/blob/master/Request-Flow

