from django import forms

SEARCH_BY = [
    ('quote', 'Quote'),
    ('author', 'Author'),
    ('tag', 'Category'),
    ]

FILTER_BY = [
    ('asc', 'Ascending'),
    ('des', 'Descending')
]

class QueryForm(forms.Form):
    form_query = forms.CharField( label='What query do you want to search?',required=False)
    search_by = forms.CharField(label='Search by:', widget=forms.Select(choices=SEARCH_BY))


class FilterForm(forms.Form):
    filter_by = forms.CharField(label='Filter by:', widget=forms.Select(choices=FILTER_BY))
