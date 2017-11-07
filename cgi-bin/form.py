# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 06.11.2017
import cgi

form = cgi.FieldStorage()
a = float(form.getfirst("a", "Missing a argument."))
b = float(form.getfirst("b", "Missing b argument."))
c = float(form.getfirst("c", "Missing c argument."))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Result</title>
        </head>
        <body>""")

if a < b + c and b < a + c and c < a + b:
    print("Yay. Triangle.")
else:
    print("Nope. I cant build triangle.")

print("""</body>
        </html>""")
