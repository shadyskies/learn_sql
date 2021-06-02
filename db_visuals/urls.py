from django.urls import path, include
from .views import home, results_view, select, where, agg, ob, joins, gb, limit, null_f


urlpatterns = [
    path('', home, name="home"),
    path('select/', select, name='select'),
    path('where/', where, name='where'),
    path('agg/', agg, name='agg'),
    path('ob/', ob, name='ob'),
    path('joins/', joins, name='joins'),
    path('gb/', gb, name='gb'),
    path('limit/', limit, name='limit'),
    path('null/', null_f, name='null'),
]
