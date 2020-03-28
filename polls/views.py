from django.shortcuts import render, redirect, HttpResponseRedirect
import requests
import simplejson as JSON
from django.contrib.sessions.models import Session
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

class AuthenticateView(View) :
    def get(self, request, *args, **kwargs) :  
        try: 
            print(request.session['StudentID'])
            return redirect("/Enstitute"); 
        except :  
            return render(request, 'Login.html', {})



class IndexView(View) :
    def get(self, request, *args, **kwargs) :
        try: 
            StudentID = request.session['StudentID']
            return render(request, 'Index.html')
        except :  
            return redirect("../")


@csrf_exempt
def GetStudent(request):
    StudentID = request.session['StudentID']
    print( StudentID )
    url = "https://localhost:5001/StudentApi/GetStudent?student_id="+StudentID
    response = requests.get( url, verify=False )
    if response.status_code == 200 :
        data = JSON.loads(response.content)
        context =  dict(
            full_name = data[ "lastName" ] + data[ "firstName" ] ,
            address = data[ "address" ][ "streetAdress" ] + data[ "address" ][ "appartementAdress" ],
            email = data[ "email" ],
            nationality = data[ "nationality" ],
            group = data[ "group" ][ "label" ] )

    return HttpResponse( JSON.dumps( context ) ) 

@csrf_exempt
def GetTotalAbsences(request):
    StudentID = request.session['StudentID']
    url = "https://localhost:5001/StudentApi/GetTotalAbsences?student_id="+StudentID
    response = requests.get( url, verify=False )
    if response.status_code == 200 :
        data = JSON.loads(response.content)
        context =  dict( total = data )

    return HttpResponse( JSON.dumps( context ) ) 

@csrf_exempt
def GetTotalDelays(request):
    StudentID = request.session['StudentID']
    url = "https://localhost:5001/StudentApi/GetTotalDelays?student_id="+StudentID
    response = requests.get( url, verify=False )
    if response.status_code == 200 :
        data = JSON.loads(response.content)
        context =  dict( total = data )

    return HttpResponse( JSON.dumps( context ) ) 

@csrf_exempt
def GetModules(request):
    StudentID = request.session['StudentID']
    url = "https://localhost:5001/StudentApi/GetModules?student_id="+StudentID
    response = requests.get( url, verify=False )
    if response.status_code == 200 :
        data = JSON.loads(response.content)
        context =  dict( modules = data )

    return HttpResponse( JSON.dumps( context ) ) 





@csrf_exempt
def Authenticate(request) : 
    #Get the posted form
    username_input = request.POST['username']
    password_input = request.POST['password']

    response = requests.get("https://localhost:5001/StudentApi/Authenticate?username="+username_input+"&password="+password_input, verify=False)

    if response.status_code == 200 :
        data = JSON.loads(response.content)
        if data['code'] == 1 :
            context =  dict(ERROR = False)
        else : 
            request.session['StudentID'] = data['message']
            return  HttpResponse( JSON.dumps(  dict( Redirect = True ) ) ) 
    else :
        context =  dict(ERROR = True)

    return HttpResponse( JSON.dumps( context ) ) 

