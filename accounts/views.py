from django.shortcuts import render, get_object_or_404
from accounts.models import User
from accounts.forms import SearchForm
from django.core import serializers

from django.http import HttpResponse

import json
import math


def accounts(request):
    boss = User.objects.get(id=1)
    children = User.objects.filter(parent_id=1)

    return render(request, "home.html", {"boss": boss,
                                         "children": children})


def single_account(request, account_id):
    account = get_object_or_404(User, pk=account_id)
    children = User.objects.filter(parent_id=account_id)

    return render(request, "single_account.html", {"account": account,
                                                   "children": children})


def all_accounts(request):
    all_users = User.objects.all()
    search_form = SearchForm()
    return render(request, "all_accounts.html", {"all_accounts": all_users,
                                                 "search_form": search_form})


def all_accounts_page_load(request):
    if request.is_ajax():
        my_json = serializers.serialize('json', User.objects.all())
        return HttpResponse(my_json, content_type='application/json')


def search(request):
    if request.is_ajax():
        if request.method == "POST":
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                my_filter = {}
                if search_form.cleaned_data["first_name"]:
                    my_filter["first_name__startswith"] = search_form.cleaned_data["first_name"].title()

                if search_form.cleaned_data["last_name"] != '':
                    my_filter["last_name__startswith"] = search_form.cleaned_data["last_name"].title()

                if search_form.cleaned_data["year"] != "year":
                    my_filter['date_joined__startswith'] = search_form.cleaned_data["year"]

                if search_form.cleaned_data["position"] != "Choose position":
                    my_filter["position"] = search_form.cleaned_data["position"]

                if type(search_form.cleaned_data["salary_min"]) == int \
                        or type(search_form.cleaned_data["salary_max"]) == int:
                    if type(search_form.cleaned_data["salary_min"]) == int \
                            and type(search_form.cleaned_data["salary_max"]) == int:
                        my_filter["salary__range"] = (search_form.cleaned_data["salary_min"],
                                                      search_form.cleaned_data["salary_max"])
                    elif type(search_form.cleaned_data["salary_min"]) == int \
                            and type(search_form.cleaned_data["salary_max"]) != int:
                        my_filter["salary__gte"] = search_form.cleaned_data["salary_min"]
                    elif type(search_form.cleaned_data["salary_min"]) != int \
                            and type(search_form.cleaned_data["salary_max"]) == int:
                        my_filter["salary__lte"] = search_form.cleaned_data["salary_max"]

                if request.GET.get('page'):
                    current_page = int(request.GET.get('page'))
                else:
                    current_page = 1

                if request.GET.get('order_by'):
                    s = request.GET.get('order_by').split(' ')
                    sort = s[0]
                else:
                    sort = 'id'

                if len(request.GET.get('order_by').split(' ')) == 2:
                    search_result = User.objects.filter(**my_filter).order_by(sort).reverse()
                elif len(request.GET.get('order_by').split(' ')) == 1:
                    search_result = User.objects.filter(**my_filter).order_by(sort)
                else:
                    search_result = User.objects.filter(**my_filter).order_by("id")

                items_count = search_result.count()
                items_per_page = 10
                total_pages = math.ceil(items_count/items_per_page)

                if current_page == 1 and current_page == total_pages:
                    search_result = search_result[0:items_count]
                elif current_page == 1:
                    search_result = search_result[0:items_per_page]
                elif current_page > 1 and current_page == total_pages:
                    search_result = search_result[(current_page-1)*10:items_count]
                elif current_page > 1:
                    search_result = search_result[(current_page-1)*10:current_page*10]

                result_obj = {"items_count": items_count,
                              "current_page": current_page,
                              "data": list(search_result.values())}

                search_result_json = json.dumps(result_obj, default=str)
                # print('query>', search_result.query)     #sql request

                return HttpResponse(search_result_json, content_type='application/json')



