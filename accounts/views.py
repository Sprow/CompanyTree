from django.shortcuts import render
from accounts.models import User
from django.shortcuts import get_object_or_404


def accounts(request):
    boss = User.objects.get(id=1)
    children = User.objects.filter(parent_id=1)


    return render(request, "home.html", {"boss": boss, "children": children})


def single_account(request, account_id):
    account = get_object_or_404(User, pk=account_id)
    children = User.objects.filter(parent_id=account_id)

    return render(request, "single_account.html", {"account": account, "children": children})

