
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import TMtool
 




# 数据库操作
def testdb(request):
    test1 = TMtool(name='runoob')
    test1.save()
    test2 = TMtool(name='runoob2')
    test2.save()



    # initialize
    response = ""
    response1 = ""

    # use all() in model manager objects, to get all the records, like SELECT * FROM
    list  = TMtool.objects.all()



    #out put all
    for var in list:
        response1 += str(var.id) + "-" + var.name + "       "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


def testdbdel(request):
	TMtool.objects.filter(id=6).delete()

    # initialize
	response = ""
	response1 = ""

    # use all() in model manager objects, to get all the records, like SELECT * FROM
	list  = TMtool.objects.all()



    #out put all
	for var in list:
		response1 += str(var.id) + "-" + var.name + "      "
	response = response1
	return HttpResponse("<p>" + response + "</p>")

def testdbupdt(request):
	TMtool.objects.filter(id=8).update(name='Google')
    
    # initialize
	response = ""
	response1 = ""


    # use all() in model manager objects, to get all the records, like SELECT * FROM
	list  = TMtool.objects.all()



    #out put all
	for var in list:
		response1 += str(var.id) + "-" + var.name + "       "
	response = response1
	return HttpResponse("<p>" + response + "</p>")