from django.views.generic import ListView
from .models import Tab
from services.services_for_model import Table


class TabNameList(ListView):
    model = Tab
    template_name = 'summary_per_hour/base.html'



class TableListView(ListView):
    template_name = 'summary_per_hour/test.html'
    table = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.t = Table()
        self.tt = self.t.Collector()


    def get_queryset(self):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            date_selected = self.kwargs.get('date_selected')
            tab_name = self.kwargs.get('tab_name')
            self.tt.set_params(tab_name=tab_name, date_selected=date_selected)
            self.tt.get_dict()
            self.tt.filling_body_dict()
            self.tt.filling_non_body_dict()
            # self.tt.print_params()
            self.t.merging_table(bodies=self.tt.bodies, headers=self.tt.headers, siders=self.tt.siders)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = {'table': self.t.get_tables() }
        return context
    #
