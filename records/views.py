from django.shortcuts import render
from .models import Record

# Create your views here.
def records(request):
    records = Record.objects.all()#.order_by(dateTime)
    # The dictionary outputs the variable records (above)
    # when rendered. Display it in the records.html template
    # via "template tags" = {% python code %} and {{data}}
    return render(request, 'records/records.html', {'records': records})
