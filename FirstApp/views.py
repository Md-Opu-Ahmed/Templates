from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def my_name (request):
#     return HttpResponse ('My name is Md.Opu Ahmed')
# def webpage (request):
#     return render (request,'file/index.html')

# def manage (request):
#     if request.method == 'POST':
#         n1 = request.GET.get('name')
#         n2 = request.GET.get('age')
#         print(n1,n2)
#         context = {
#             'name':n1,
#             'age':n2
#         }
#     return render (request,'manage.html',context)

# # one way............
# def userForm (request):
#     try:
#         n1 = int(request.GET['name1'])
#         n2 =int(request.GET['name2']) 
#         print(n1+n2)
#     except:
#         pass
#     return render (request,'file/manage.html')
# # two way .............
# def userForm (request):
#     finalans = 0
#     try:
#         n1 = int(request.GET.get('name1'))
#         n2 =int(request.GET.get('name2')) 
#         finalans = n1 + n2
#     except:
#         pass
#     return render (request,'file/manage.html',{'output':'finalans'})

def file (request):
    return render(request,'file/file.html')
