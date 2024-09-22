from django.http import HttpResponse
from django.utils.translation import gettext as _  # импортируем функцию для перевода
from django.views import View


# Create your views here.

class Index(View):
    def get(self, request):
        string = _('Hello world')

        return HttpResponse(string)