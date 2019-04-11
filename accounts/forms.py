from django import forms
from accounts.models import User


class SearchForm(forms.Form):
    list_of_all_positions = [("Choose position", "Choose position")]
    try:
        querySet_of_all_positions = User.objects.values('position')
        if len(querySet_of_all_positions) >= 2:
            for i in querySet_of_all_positions:
                for _, val in i.items():
                    list_of_all_positions.append((val, val))
    except:
        pass

    list_of_all_years = []
    list_of_all_years2 = [("year", "year")]
    try:
        querySet_of_all_years = User.objects.values('date_joined')
        if len(querySet_of_all_years) >= 2:
            for i in querySet_of_all_years:
                for key, val in i.items():
                    year = val.year
                    list_of_all_years.append(year)
            for i in range(min(list_of_all_years), max(list_of_all_years)+1):
                list_of_all_years2.append((i, i))
    except:
        pass

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    position = forms.CharField(required=False, widget=forms.Select(choices=list_of_all_positions))
    year = forms.CharField(required=False, widget=forms.Select(choices=list_of_all_years2))
    salary_min = forms.IntegerField(required=False, min_value=0)
    salary_max = forms.IntegerField(required=False, min_value=0)
    page_number = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    total_pages = forms.IntegerField(widget=forms.HiddenInput(), required=False)

