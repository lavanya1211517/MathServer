# Ex.03 Design a Website for Server Side Processing
## Date:10-11-2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
<html>
    <head>
        <title>Math</title>
    </head>
    <body>
        <h1>LAVANYA V (26009527)</h1>
        <h2>CHURN RATE CALCULATON</h2>

        <form method="POST">
          {% csrf_token %}
            
            <label>Customers lost count:</label>
            <input type="number"  value="{{ Customers_count }}" name="length">
            <br><br>
            
            <label>Initial Customers count:</label>
            <input type="number"  value="{{ Initial_Customer }}" name="breadth">
            <br><br>
            
            <input type="submit" value="calculate">
            <br><br>
            
            <label>Churn Rate count:</label>
            <input type="number"  value="{{ area }}" >
        </form>
    </body>
</html>

views.py

from django.shortcuts import render

def cumchurn_area(request):
     Customers_count = float(request.POST.get('length', '0'))
     Initial_Customer   = float(request.POST.get('breadth', '0'))
     area =( Customers_count / Initial_Customer)*100 if request.method == 'POST' else 0

     print("Customers lost count =", Customers_count)
     print("Initial customers count =", Initial_Customer)
     print("Churn Rate =", area)

     return render(
        request,
        'mysivan/sivan.html',
        {'Customers_count': Customers_count, 'Initial_Customer': Initial_Customer, 'area': area}
    )

urls.py

from django.contrib import admin
from django.urls import path
from mysivan import views

urlpatterns = [
    path('', views. cumchurn_area, name='cumchurn_area'),
]


```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-11-17 134359.png>)

## OUTPUT - WEBPAGE:

![alt text](<Screenshot 2026-11-17 134832.png>)


## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
