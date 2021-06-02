from django.shortcuts import render, redirect, HttpResponseRedirect
from .db_ops import connect, query_db
from .forms import select_clause, where_clause, ob_clause,agg_clauses, join_clause, limit_clause, null_clause
from django.urls import reverse


def home(request):
    engine = connect(database='emp')
    val = query_db(engine=engine, query="SELECT * FROM EMPLOYEE")
    print(val)
    return render(request, "db_visuals/home.html", context={"val":val})


def results_view(request, query):
    di = {'select': 'db_visuals/select.html', 'where': 'db_visuals/where.html', 'distinct': 'db_visuals/distinct.html',
              'order': 'db_visuals/order.html', 'gb': 'db_visuals/gb.html', 'agg': 'db_visuals/agg.html', 'limit':'db_visuals/limit.html',
              'joins': 'db_visuals/joins.html'}
    di = {'select': 'select', 'where': 'where', 'distinct': 'distinct'}
    if query in di:
        eval(query + f'({request})')


def select(request):
    engine = connect(database='emp')
    val = query_db(engine=engine, query="SELECT * FROM EMPLOYEE;")
    if request.method == 'POST':
        form = select_clause(request.POST)
        if form.is_valid():
            tmp1 = form.cleaned_data
            quer = 'SELECT ' + tmp1['select'] + ' FROM EMPLOYEE;'
            res = query_db(engine=engine, query=quer)
            return render(request, 'db_visuals/select.html', {'val': val, "res": res, "form": form, 'quer': quer})
    else:
        form = select_clause()
    return render(request, 'db_visuals/select.html',  {'val': val, "res": val, "form": form})


def where(request):
    engine = connect(database='emp')
    val = query_db(engine=engine, query="SELECT * FROM EMPLOYEE ;")
    if request.method == 'POST':
        form = where_clause(request.POST)
        if form.is_valid():
            sel = form.cleaned_data
            quer = 'SELECT * FROM EMPLOYEE WHERE ' + sel['query']
            res = query_db(engine, quer)
            return render(request, 'db_visuals/where.html', {'val': val, "res": res, "form": form, 'quer': quer})
    else:
        form = where_clause()
    return render(request, 'db_visuals/where.html', {'val': val, "res": val, 'form': form})


def ob(request):
    engine = connect(database='emp')
    val = query_db(engine=engine, query="SELECT * FROM EMPLOYEE;")
    if request.method == 'POST':
        form = ob_clause(request.POST)
        if form.is_valid():
            tmp1 = form.cleaned_data
            quer = 'SELECT * FROM EMPLOYEE ORDER BY ' + tmp1['query']
            res = query_db(engine, quer)
            return render(request, 'db_visuals/order.html', {'val': val, "res": res, 'form': form, 'quer': quer})
    else:
        form = ob_clause()
    return render(request, 'db_visuals/order.html',  {'val': val, "res": val, 'form': form})


def gb(request):
    engine = connect(database='emp')
    val = query_db(engine=engine, query="SELECT * FROM EMPLOYEE;")

    return render(request, 'db_visuals/select.html',  {'val': val, "res": val})


def joins(request):
    engine = connect(database='emp')
    val = query_db(engine=engine, query="SELECT * FROM EMPLOYEE;")
    cust_table = query_db(engine, query="SELECT * FROM orders;")
    if request.method == 'POST':
        form = join_clause(request.POST)
        if form.is_valid():
            tmp1 = form.cleaned_data
            quer = f'SELECT * FROM orders '+ tmp1['joins'] + ' EMPLOYEE on EMPLOYEE.emp_id = orders.emp_id'
            res = query_db(engine, quer)
            return render(request, 'db_visuals/joins.html', {'val': val, "res": res, "form": form, 'cust_table': cust_table, 'quer': quer})

    else:
        form = join_clause()
    return render(request, 'db_visuals/joins.html',  {'val': val, "res": val, "form": form, 'cust_table': cust_table})


def agg(request):
    engine = connect(database='emp')
    val = query_db(engine=engine, query="SELECT * FROM EMPLOYEE;")
    if request.method == 'POST':
        form = agg_clauses(request.POST)
        if form.is_valid():
            tmp1 = form.cleaned_data
            ls = list(tmp1.keys())
            for i in range(len(tmp1)):
                if tmp1[ls[i]] != '':
                    tmp2 = tmp1[ls[i]]
                    break
            quer = 'SELECT' + f' {ls[i]}({tmp2}) FROM EMPLOYEE; '
            res = query_db(engine, quer)
            return render(request, 'db_visuals/agg.html', {'val': val, "res": res, 'form': form, 'quer': quer})
    else:
        form = agg_clauses()
    return render(request, 'db_visuals/agg.html',  {'val': val, "res": val, "form": form})


def limit(request):
    engine = connect('emp')
    val = query_db(engine, 'SELECT * FROM EMPLOYEE')
    if request.method == 'POST':
        form = limit_clause(request.POST)
        if form.is_valid():
            tmp1 = form.cleaned_data
            quer = 'SELECT * FROM EMPLOYEE LIMIT ' + str(tmp1['limit'])
            res = query_db(engine, quer)
            return render(request, 'db_visuals/limit.html', {'val': val, 'res': res, 'quer': quer ,'form': form})
    else:
        form = limit_clause()
    return render(request, 'db_visuals/limit.html',{'val': val,'form': form})


def null_f(request):
    engine = connect('emp')
    val = query_db(engine, 'SELECT * FROM EMPLOYEE')
    if request.method == 'POST':
        form = null_clause(request.POST)
        if form.is_valid():
            tmp1 = form.cleaned_data
            quer = 'SELECT * FROM EMPLOYEE WHERE ' + tmp1['col'] + " " + tmp1['NULL']
            res = query_db(engine, quer)
            return render(request, 'db_visuals/null.html', {'val': val, 'res': res, 'quer': quer, 'form': form})
    else:
        form = null_clause()
    return render(request, 'db_visuals/null.html', {'val': val,'form': form})

