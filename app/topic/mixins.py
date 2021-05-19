class QueryparamMixins(object):

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['queryparam_filter'] = self.request.GET.get('filter', 'all')
        context['queryparam_search'] = self.request.GET.get('search', '')
        context['queryparams'] = self.request.GET.urlencode()
        return context