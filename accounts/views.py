from django.shortcuts import render
from accounts.models import User
from django.shortcuts import get_object_or_404


def accounts(request):
    boss = User.objects.get(id=1)
    children = User.objects.filter(parent_id=1)

    # users = User.objects.all().order_by("id")
    # myDict = {}
    #
    # def mix(list_of_users, my_dict):
    #     people_without_boss = list_of_users.filter(user_boss="")
    #     for i in people_without_boss:
    #         my_dict.update({i.username: {}})
    #
    #     def mix2(my_dict):
    #         for key in my_dict:
    #             find_boss_children = list_of_users.filter(user_boss=key)
    #             for b in find_boss_children:
    #                 my_dict[key].update({b.username: {}})
    #             mix2(my_dict[key])
    #     mix2(my_dict)
    #
    # mix(users, myDict)
    #
    # myList = []
    #
    # def make_my_list(my_dict):
    #     for key, val in my_dict.items():
    #         if key not in myList:
    #             myList.append("|    " * users.get(username=key).level + key)
    #         for i in val:
    #             if i not in myList:
    #                 myList.append(i)
    #             make_my_list(val)
    #
    # make_my_list(myDict)
    # zzz = "&emsp;"

    return render(request, "home.html", {"boss": boss, "children": children})


def single_account(request, account_id):
    account = get_object_or_404(User, pk=account_id)
    children = User.objects.filter(parent_id=account_id)

    return render(request, "single_account.html", {"account": account, "children": children})

