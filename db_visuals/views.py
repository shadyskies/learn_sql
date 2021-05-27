from django.shortcuts import render, redirect, HttpResponseRedirect
from .db_ops import connect, query_db
from .views import query_db
# from .forms import db_query_form
from django.urls import reverse


def home(request):
    engine = connect(database='emp')
    val = query_db(engine=engine, query="SELECT * FROM EMPLOYEE")
    # if request.method == 'POST':
    #     qform = db_query_form(request.POST)
    #     if qform.is_valid():
    #         qform = qform.cleaned_data
    #         print("###################################")
    #         print(type(qform))
    #         print("###################################")
    #         url = reverse('results_view', kwargs={"res": qform})
    #         return HttpResponseRedirect(url)
    # else:
    #     qform = db_query_form()
    # context = {
    #     # "val": val,
    #     "form": qform
    # }
    return render(request, "db_visuals/home.html", context={"val":val})


# def results_view(request, res):
#     res = eval(res)
#     print(res)
#     context = {"res": res}
#     return render(request, 'db_visuals/query_res.html', context=context)


def results_view(request, query):
    print(query)
    context = {'res': query}
    di = {'select': 'db_visuals/select.html', 'where': 'db_visuals/where.html', 'distinct': 'db_visuals/distinct.html',
          'order': 'db_visuals/order.html', 'gb': 'db_visuals/gb.html', 'agg': 'db_visuals/agg.html', 'limit':'db_visuals/limit.html'}

    return render(request, di[query], {'res': query})