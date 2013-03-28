from django.http import HttpResponse 
from django.template import Context
from django.template.loader import get_template
import datetime  
def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('test.html')
    html = t.render(Context())  
    return HttpResponse(html)