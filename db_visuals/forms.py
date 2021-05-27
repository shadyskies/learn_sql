from django import forms


class db_query_form(forms.Form):
    select = forms.CharField(label='SELECT')
    where = forms.CharField(label='WHERE')
    exists = forms.CharField(label="EXISTS")
    gb = forms.CharField(label="GROUP BY")
    distict = forms.CharField(label="DISTINCT")
    order = forms.CharField(label="ORDER BY")

    fields = ['select', 'where', 'exists', 'gb', 'distinct', 'order']

