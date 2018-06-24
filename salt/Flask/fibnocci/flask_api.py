from flask import Flask,jsonify,request
import gc
import logging
import syslog

app = Flask(__name__)
global_cache = {}


@app.route('/',methods=['GET','POST'])
def index():
        syslog.syslog(syslog.LOG_WARNING,'I Got request to Base URL ')
        return 'Usage:  https://ip/fib/num'


@app.route('/fib/<string:value>',methods=['GET'])
def fib(value):
        #custom="Garbage collection thresholds:"+str(gc.get_threshold())
 	ans_list = []
 	global global_cache
        if gc.collect() > 10 : global_cache = {}
	try:
   	   n = int(value)
   	   if n < 0:
              syslog.syslog(syslog.LOG_ERR,'I Got Negative Number and I am Handling it')
   	      return 'negative number - wrong input'
 	except:
              syslog.syslog(syslog.LOG_ERR,'I Got Wrong Input I am Handling it')
              return 'wrong input'
   
 	if n in global_cache.keys():
 	    	ans_list = str(global_cache[n])
 	elif n < 1:
     		ans = 0 
     		global_cache[n] = ans
	else:
     		a,b = 0,1
     		for i in range(n):
         		ans_list.append(a)
         		a,b = b,a+b
     		global_cache[n] = ans_list
        syslog.syslog(syslog.LOG_INFO,'I Processed '+value)
 	return str(ans_list)

if __name__ == '__main__':
	app.run(debug=True)
