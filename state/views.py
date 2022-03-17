from django.shortcuts import render

from state.models import District, State

# Create your views here.

def index(request):
    state=State.objects.all()
    return render(request,'index.html',{'state':state})

def state_check(request):
    id=request.GET['id']
    district_data=District.objects.filter(state_id=id)
    return render(request,'district.html',{'dist_data':district_data,})