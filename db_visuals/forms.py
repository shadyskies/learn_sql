from django import forms


class select_clause(forms.Form):
    sel = [('*', '*'),
           ('name', 'name'),
           ('age', 'age'),
           ('yearsofexp', 'yearsofexp'),
           ('emp_id', 'emp_id')]
    select = forms.ChoiceField(choices=sel)


class where_clause(forms.Form):
    query = forms.CharField(max_length=30, initial="name='naman'")


class ob_clause(forms.Form):
    query = forms.CharField(max_length=40, initial='name ASC')


class agg_clauses(forms.Form):
    COUNT = forms.CharField(max_length=30, required=False)
    AVG = forms.CharField(max_length=30, required=False)
    MAX = forms.CharField( required=False)
    MIN = forms.CharField( required=False)
    SUM = forms.CharField( required=False)


class join_clause(forms.Form):

    choices = [('INNER JOIN', 'INNER JOIN'),
               ('LEFT JOIN', 'LEFT JOIN'),
               ('RIGHT JOIN', 'RIGHT JOIN'),
               ('FULL JOIN', 'FULL JOIN')]
    joins = forms.ChoiceField(choices=choices)


class limit_clause(forms.Form):
    limit = forms.IntegerField(initial=2)


class null_clause(forms.Form):
    choices = [('IS NULL', 'IS NULL'),
               ('IS NOT NULL', 'IS NOT NULL')]
    sel = [('name', 'name'),
           ('age', 'age'),
           ('yearsofexp', 'yearsofexp'),
           ('emp_id', 'emp_id')]
    col = forms.ChoiceField(choices=sel)
    NULL = forms.ChoiceField(choices=choices)