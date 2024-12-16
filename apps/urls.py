from django.urls import path
from . import views

urlpatterns = [
    path('assessment_plan/', views.assessment_plan, name='assessment_plan'),
    path('assessment_plan/assessment_plan_insert/', views.assessment_plan_insert, name='assessment_plan_insert'),
    path('viewuser/',views.viewuser,name='viewuser'),
    path('deleteprofile/<int:id>/',views.deleteprofile,name='deleteprofile'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('updateprofile/<int:id>/',views.updateprofile,name='updateprofile'),
    
]
