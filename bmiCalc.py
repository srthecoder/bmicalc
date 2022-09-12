#!C:/Users/Swachandrika/AppData/Local/Programs/Python/Python39/python.exe
import cgi
# create instance of fieldStorage
form = cgi.FieldStorage()
# get data from fields
n = form.getvalue('name')
a = form.getvalue('age')
ph = form.getvalue('pno')
mid = form.getvalue('mid')
if form.getvalue("gender"):
    g = form.getvalue("gender")
else:
    g = "Not selected!"
flag = flag1 = h = w = inc = p = metric = standard = 0
scale = "-----?"
if form.getvalue("h")== None: flag = 1
else: 
    h = int(form.getvalue("h"))
    inc = h / 2.54 #converting cm to inches
if form.getvalue("w")== None: flag = 1
else: 
    w = int(form.getvalue("w"))
    p = w * 2.205 # converting kg to pounds
    
if form.getvalue("feet") == None: flag1 = 1
else:
    f = int(form.getvalue("feet"))
    if form.getvalue("inch")== None: 
        if h > 0 : inc = h/2.54
        else: 
            inc = f * 12
            h = inc * 2.54 #converting inches to cm
    else: 
        inc = f * 12 + int(form.getvalue("inch"))
        h = inc * 2.54
if form.getvalue("p")== None: flag1 = 1
else: 
    p = int(form.getvalue("p"))
    w = p / 2.205

standard = 703 * p / inc ** 2
metric = w / (h / 100) ** 2
while(flag == 0):
    if metric < 18: scale = "Underweight!"
    elif 18 <= metric < 25: scale = "Healthy!"
    elif 25 <= metric < 30: scale = "Overweight!"
    elif metric >= 30: scale = "Obese!"
    break

while(flag1 == 0):
    if standard < 18: scale = "Underweight!"
    elif 18 <= standard < 25: scale = "Healthy!"
    elif 25 <= standard < 30: scale = "Overweight!"
    elif standard >= 30: scale = "Obese!"
    break

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head><style>div{ margin-right: 4%;border: 2px solid teal; float: left;border-radius: 5px; background-color: honeydew; padding: 20px; box-shadow: 4px 2px 4px 2px rgba(0,0,0,.2);}")
print("h2{margin-top: 0.5%;font-family: SourceSansPro;font-size: 35px;text-shadow: 2px 2px 2px yellow;color: steelblue;}")
print("body{background-color: cadetblue;}</style>")
print("<title> BMI </title>")
print("</head>")
print("<body>")
print("<div style =\"margin-left: 2%;width: 51.5%;\"><h2>-----------Your Body Mass Index-----------</h2>")
print("&emsp;&emsp;<b>Name:</b> %s &emsp;<b>Age: </b>%s &emsp;<b>Gender: </b>%s"%(n,a,g))
print("<br><br><br><div style =\"background-color: mintcream;margin-right: 2%;margin-left: 2%;\"><b>Metric System:</b>")
print("<h4>\n</h4><b>Height(cm): </b>%d&emsp;&emsp;<b>Weight(cm): </b>%d"%(h,w))
print("<h4>\n</h4><b>BMI = </b>%f"%metric)
print("</div><div style =\"background-color: mintcream; margin-left: 1%;\"><b>Standard System:</b>")
print("<h4>\n</h4><b>Height(inc): </b>%d&emsp;&emsp;<b>Weight(lbs): </b>%d"%(inc,p))
print("<h4>\n</h4><b>BMI = </b>%f"%standard)
print("</div></div><div>")
print("<img src=\"scale.png\" style=\"width: 389px\"><br>")
print("<h2 style = \"align: center;\">&emsp;You are %s</div><br><br><br><br><br><br><br><br>"%scale)
print("<br><br><br><br><br><br><br><br><br><br>")
print("<div style= \"margin-left: 2%; width: 90%\"><h2 style = \"align: center;\">Healthy Weight Resources</h2>")
print("<p>Energy is another word for \"calories.\" What you eat and drink is energy which is spent through physical activity. The balance between energy intake and discharge is needed to maintain a healthy weight. Other factors that affect a person's weight include metabolism, genes, and the environment.</p>")
print("<a href= \"https://www.nhlbi.nih.gov/health/educational/wecan/eat-right/choosing-foods.htm\">Eating right!</a>")
print("<p>Help your family move more each day and have fun with it. Think about what your family can do to be active together. Here are some ideas.</p>")
print("<a href= \"https://www.nhlbi.nih.gov/health/educational/wecan/get-active/activity-plan.htm\"> Make an activity plan!</a>")
print("</div></body>")
print("</html>")
