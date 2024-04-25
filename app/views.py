from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    content = ''' <center><h1> Hello World </h1> \n'''
    content += ''' <center><h2> I am not Online Server </h2> '''
    content += ''' <center><h2> I am Backend developer </h2> '''
    return HttpResponse(content)


def index(request):
    path = request.path
    method = request.method
    content = ''' 
    <center><h2>Testing Django Request Response Objects</h2> 
    <p>Request path : " {}</p> 
    <p>Request Method :{}</p></center> 
    '''.format(path, method)
    return HttpResponse(content)
