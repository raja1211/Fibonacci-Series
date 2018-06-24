from flask import Flask,jsonify,request

app = Flask(__name__)
global_cache = {}


@app.route('/',methods=['GET','POST'])
def index():
        return 'Usage:  https://ip/fib/num'


@app.route('/fib/<string:value>',methods=['GET'])
def fib(value):
 try:
   n = int(value)
   if n < 0:
   	return 'Sorry you entered negative number \n'
 except:
   return 'Seems to be you enterd unsupported value\n'
   
 ans_list = []
 global global_cache
 if n in global_cache.keys():
     ans_list = str(global_cache[n])
 elif n < 1:
     ans = 0 
     global_cache[n] = ans
#     ans_list = ans
 else:
     a,b = 0,1
     for i in range(n):
         ans_list.append(a)
         a,b = b,a+b
     global_cache[n] = ans_list
 return str(ans_list)




if __name__ == '__main__':
    app.run(debug=True)
