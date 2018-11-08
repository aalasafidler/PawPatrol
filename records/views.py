from django.shortcuts import render
from .models import Record
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def records(request):
    records = Record.objects.all()#.order_by(dateTime)
    # The dictionary outputs the variable records (above)
    # when rendered. Display it in the records.html template
    # via "template tags" = {% python code %} and {{data}}
    return render(request, 'records/records.html', {'records': records})

@login_required(login_url="/accounts/login/")
def record_create(request):
    return render(request, 'records/record_create.html')
    #return redirect('/')
