from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataCapt_Form

# Create your views here.

def Home_Page(request, *args, **kwargs):
	return HttpResponse("<h1>Welcome to the Home Page...</h1>")

def DataCapt_Page(request, *args, **kwargs):
	DataCapt_Frm = DataCapt_Form()
	if request.method == "POST" and "Save" in request.POST:
		DataCapt_Frm = DataCapt_Form(request.POST)
		if DataCapt_Frm.is_valid():
			DataCapt_Frm.save()
			print(DataCapt_Frm.cleaned_data)
		return redirect("/captdata/")
	DataCapt_Context = {"DataCapt_Blk": DataCapt_Frm}
	return render(request,"DataCapt_Html_Page",DataCapt_Context)				
