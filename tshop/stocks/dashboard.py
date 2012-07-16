from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, \
    AppIndexDashboard
from admin_tools.utils import get_admin_site_name
from stocks.models import *




class StocksDashboard(modules.DashboardModule):
    title = _(u'Estado de stocks')
    template = 'admin/stocks_dashboard.html'

    def __init__(self, *args, **kwargs):
        super(StocksDashboard, self).__init__(*args, **kwargs)
        self.stock = Stock.objects.all()[0]

    def is_empty(self):
        return False


