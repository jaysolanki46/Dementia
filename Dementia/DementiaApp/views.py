from django.shortcuts import render

# Create your views here.
def patient_form(request):
    return render(request, "patient_forms/patient_form.html")
