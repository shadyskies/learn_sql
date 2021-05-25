from django.shortcuts import render
from .db_ops import connect, query_db


def home(request):
    engine = connect(database='emp')
    val = query_db(engine=engine, query="SELECT * FROM EMPLOYEE")
    context = {
        "val": val
    }
    return render(request, "db_visuals/home.html", context=context)