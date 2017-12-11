# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators import csrf

#form
def search_form(request):
	return render_to_response('search_form.html')

#receive request data
def search(request):
	request.encoding='utf-8'
	if 'search_str' in request.GET:
		message = 'you are searching for ' + request.GET['search_str']
	else:
		message = 'you submitted a blank form'
	return HttpResponse(message)

# get POST request
def search_post(request):
	ctx={}
	if request.POST:
		ctx['rlt'] =request.POST['search_str']
	return render(request, "search_post.html",ctx) 

