from django.shortcuts import render, get_object_or_404
from accounts.models import User
from accounts.forms import SearchForm
from django.core import serializers

from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils import gen_page_list
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

    paginator = Paginator(all_users, 5)
    page = request.GET.get('page', 1)
    current_page = request.GET.get('page')
    last_page = paginator.num_pages
    paginator_gen_list = gen_page_list(int(page), paginator.num_pages)
    try:
        all_users = paginator.page(page)
    except PageNotAnInteger:
        all_users = paginator.page(1)
    except EmptyPage:
        all_users = paginator.page(paginator.num_pages)

    return render(request, "all_accounts.html", {"all_accounts": all_users,
                                                 "search_form": search_form,
                                                 "last_page": last_page,
                                                 "paginator_gen_list": paginator_gen_list,
                                                 "current_page": current_page})


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

                search_result = User.objects.filter(**my_filter)
                items_count = int(len(search_result))
                items_per_page = 10
                total_pages = math.ceil(items_count/items_per_page)
                if request.GET.get('page'):
                    current_page = int(request.GET.get('page'))
                else:
                    current_page = 1

                search_result2 = None
                if current_page == 1 and current_page == total_pages:
                    search_result2 = User.objects.filter(**my_filter)[0:items_count]
                elif current_page == 1:
                    search_result2 = User.objects.filter(**my_filter)[0:items_per_page]
                elif current_page > 1 and current_page == total_pages:
                    search_result2 = User.objects.filter(**my_filter)[(current_page-1)*10:items_count]
                elif current_page > 1:
                    search_result2 = User.objects.filter(**my_filter)[(current_page-1)*10:current_page*10]

                # print('search_result ->', search_result)
                # print('search_result2 ->', search_result2)
                # print('search_result ->', type(list(search_result.values())))
                # print('search_result2 ->', type(search_result2))
                result_obj = {"items_count": items_count,
                              "current_page": current_page,
                              "data": list(search_result2.values())}
                # search_result_json = serializers.serialize('json', User.objects.filter(**my_filter))
                search_result_json = json.dumps(result_obj, default=str)
                # print(len(search_result))
                # print('query>', search_result.query)     #sql request
                # data = json.loads(request.body)
                # print("my filter --->", my_filter)
                # print('after filter 2 >', search_result)
                # print('after filter json>', search_result_json)
                # print('after filter json>', type(search_result_json))

                return HttpResponse(search_result_json, content_type='application/json')
    # else:
    #     # my_json = serializers.serialize('json', User.objects.all())
    #     all_acc = User.objects.all()
    #
    #     total_pages = int(len(all_acc) / 5)
    #
    #     if request.GET.get('page'):
    #         current_page = request.GET.get('page')
    #     else:
    #         current_page = "1"
    #     result_obj = {"total_pages": total_pages,
    #                   "current_page": current_page,
    #                   "data": list(all_acc.values())}
    #     # return HttpResponse(my_json, content_type='application/json')
    #     return HttpResponse(json.dumps(result_obj, default=str))


