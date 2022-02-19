from django.views.generic import ListView

class HomePage(ListView):
    template_name = 'base.html'
    def get_queryset(self):
        pass



