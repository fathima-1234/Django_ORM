from django.http import HttpResponse
from django.template import loader
# from .models import Member
from django.db.models import Q

# def members(request):
#   mymembers = Member.objects.filter (Q(firstname='Emil')|Q(lastname ='Tobias')).values()
#   template = loader.get_template('myfirst.html')
#   context = {
#     'mymembers': mymembers,
#   }
#   return HttpResponse(template.render(context, request))

# Create your views here.
