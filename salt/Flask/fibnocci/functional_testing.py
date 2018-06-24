import requests

host_list = ['10.2.52.176','10.2.52.169']
class FuncTestCase:
    def __init__(self):
        pass
    def test_positive_integer(self,value):
        for i in host_list:
                url =  'https://'+str(i)+'/fib/'+str(value)
                r = requests.get(url,verify=False)

                a = list((r.json()['result']))
                if not a:
                    print('Test Case with PositiveNumbers Failed on -->',value)
                else:
                    print('Test Case with PositiveNumbers Passed on -->', value)
                    import random
                    index = random.randint(2, len(a))
                    resul = a[index]
                    for i in host_list:
                        url = 'https://' + str(i) + '/fib/' + str(index+1)
                        req = requests.get(url,verify=False)
                        if max((req.json()['result'])) == resul:
                            print('Test Case with Positive Random Number Passed on --> ',index,i)
                        else:
                            print('Test Case with Positive Random  Numbers Failed --> ',index,i)

    def test_negative_number(self,value):
        for i in host_list:
                url =  'https://'+str(i)+'/fib/'+str(value)
                r = requests.get(url,verify=False)
                #print(r.json()['result'])
                if r.json()['result'] == str('negative number - wrong input'):
                    print('Negative Number Testcase passed On --> ',value,i)
                else:
                    print('Negative Number Testcase Failed On --> ',value,i)

    def test_zero(self,value):
        for i in host_list:
                url =  'https://'+str(i)+'/fib/'+str(value)
                r = requests.get(url,verify=False)
                a = list((r.json()['result']))
                if not a:
                    print('Test Case with Zero Passed',i)
                else:
                    print('Zero Test Case Failed',i)

    def test_unknown(self,value):
        for i in host_list:
                url =  'https://'+str(i)+'/fib/'+str(value)
                req = requests.get(url,verify=False)
                ans = (req.json()['result'])
                if ans == 'wrong input':
                     print('Test Case with Unknown Passed --> ',value,i)
                else:
                     print('Test Case with Unknow Failed -->',value,i)


if __name__=='__main__':

   fib_test = FuncTestCase()
   val = [-16,16,0,10.0,'hello']
   for index  in range(len(val)):
       variable = val[index]
       if isinstance(variable,(float)):
           #print(variable)
           fib_test.test_unknown(value=variable)
       else:
           try:
                if  int(variable) < 0 :
                    #print(variable)
                    fib_test.test_negative_number(value=variable)
                elif int(variable) == 0 :
                    #print(variable)
                    fib_test.test_zero(value=int(variable))
                else :
                    #print('positive',variable)
                    fib_test.test_positive_integer(value=variable)

           except:
               #print(variable)
               fib_test.test_unknown(value=variable)
