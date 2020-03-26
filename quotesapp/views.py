from django.core.mail import  BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import QueryForm, FilterForm
import requests, datetime
import sys


def searchView(request):
    if request.method == 'GET':
        form = QueryForm()
    else:
        form = QueryForm(request.POST)
        if form.is_valid():
            try:
                query = form.cleaned_data['form_query']
                request.session['form_query'] = query
                search_by = request.POST.get('search_by')
                request.session['search_by'] = search_by
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('success')
    return render(request, "search.html", {'form': form})


def successView(request):
    start = datetime.datetime.now()
    if request.method != 'POST':
        form_filter = FilterForm()
        query = request.session.get('form_query')
        search_by = request.session.get('search_by')
        if search_by=="quote":
            api = 'http://localhost:8983/solr/quotes/select?q=quote%3A%22' + query + '%22&wt=json&rows=100000'
        elif search_by=="author":
            api = 'http://localhost:8983/solr/quotes/select?q=author%3A%22' + query + '%22&wt=json'
        elif search_by=="tag":
            api = 'http://localhost:8983/solr/quotes/select?q=tag%3A%22' + query + '%22&wt=json'
        response = requests.get(api)
        data = response.json()
        data = data['response']['docs']
        len_data = len(data)
        end = datetime.datetime.now()
        duration = (end - start).total_seconds()
        duration = '{:g}'.format(float('{:.3g}'.format(duration)))
        
        
        return render(request, 'success.html', {
                'data': data,
                'duration': duration,
                'len_data': len_data
            })
    else:
        form_filter = FilterForm(request.POST)
        if form_filter.is_valid():
            filter_by = request.POST.get('filter_by')
            print(filter_by)



