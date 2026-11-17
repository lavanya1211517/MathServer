from django.shortcuts import render
def churn_rate(request):
    h = float(request.POST.get('initial', '0'))
    a = float(request.POST.get('lost', '0'))
    ChurnRate = (a / h) * 100 if request.method == 'POST' else 0
    print("initial =",h)
    print("lost =",a)
    print("ChurnRate=",ChurnRate)
    return render(request, 'myapp/myapp.html',{'h': h, 'a': a, 'ChurnRate': ChurnRate})