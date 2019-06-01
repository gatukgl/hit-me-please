from django.http import HttpResponse
from django.views import View


class LandingPageView(View):
    def get(self, request):
        html = '<form action="." method="post">'
        html += '<input type="email">'
        html += '<input type="submit">Submit</input>'
        return HttpResponse(html)
