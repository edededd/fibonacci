from flask import Flask
  
app = Flask(__name__)



def fibonacci(n):
    a = 0
    b = 1

    if n == 1:
        return 1
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
    

@app.route('/fibo/<int:n>', methods=['GET'])
def fibo(n):
    k=fibonacci(n)
    return f"{k}"

app.run()