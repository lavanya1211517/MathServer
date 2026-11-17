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