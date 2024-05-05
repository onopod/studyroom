from django.views.generic import ListView
from api.models import Display

class DisplayListView(ListView):
    model = Display

    def get_context_data(self):
        ctx = super().get_context_data()

        queryset = ctx.get("object_list").order_by("place")
        d = {}
        for u in queryset:
            d[u.place] = d.get(u.place, []) + [u]
        ctx["user_dict"] = d
        return ctx

