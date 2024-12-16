
from django.template import loader
from django.shortcuts import render
from .models import AssessmentPlan
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
@csrf_protect
def assessment_plan(request):
    return render(request,"assessment_plan.html",{'request':request})

def assessment_plan_insert(request):
    vduration= request.POST['duration']
    vWeightage = request.POST['Weightage']
    vtypeology = request.POST['typeology']
    vPattern= request.POST['Pattern']
    vschedule = request.POST['schedule']
    vtopicscoverd = request.POST['topicscoverd']
    ap = AssessmentPlan(duration=vduration, Weightage = vWeightage, typeology = vtypeology,Pattern =vPattern,schedule=vschedule,topicsovered=vtopicscoverd)
    ap.save()
    return render(request, 'assessment_plan.html',{})

def viewuser(request):
    user=AssessmentPlan.objects.all()
    return render(request,"viewuser.html",{'userdata':user})

def deleteprofile(request,id):
    us=AssessmentPlan.objects.filter(id=id)
    us.delete()
    return redirect("/viewuser")

def edit(request,id):
    user=AssessmentPlan.objects.filter(id=id)
    return render(request, "edit.html",{'userdata':user})

def updateprofile(request,id):
    avduration= request.POST['duration']
    avWeightage = request.POST['Weightage']
    avtypeology = request.POST['typeology']
    avPattern= request.POST['Pattern']
    avschedule = request.POST['schedule']
    avtopicscoverd = request.POST['topicscoverd']
    user=AssessmentPlan.objects.get(id=id)
    user.duration=avduration
    user.Weightage=avWeightage
    user.typeology=avtypeology
    user.Pattern= avPattern
    user.schedule= avschedule
    user.topicscoverd= avtopicscoverd
    user.save()
    return redirect("/viewuser")