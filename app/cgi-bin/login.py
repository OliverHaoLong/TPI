import cgi
form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if 'user' = 'hao' :
    print('<h1>Please enter your name.</h1>')
else:
    print('<h1>Hello!</h1>')
    
