from django.shortcuts import render
from urllib.request   import urlopen
from register.models  import *
from register.forms   import *
import re

def main(request):
    error = None
    success = False

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            code     = form.cleaned_data['code']

            userlist = urlopen("https://www.skywanderersgame.com/userlist.php").read().decode()
            userlist = "<span>Le_minaw</span><span>Daddash</span>"
            if "<span>%s</span>" % username in userlist:
                try:
                    db_code = ActivationCode.objects.get(code=code)
                    if db_code.active:
                        user = Member(username=username, user_rank=db_code.code)
                        user.save()
                        db_code.active = False
                        db_code.save()
                        success = True

                    else:
                        error = "This activation code has already been used."
                except ActivationCode.DoesNotExists:
                    error = "Invalid activation code!"
            else:
                error = "This username is not registered on the Skywanderers forums!"
    else:
        form = RegisterForm()

    return render(request, "register/main.html", locals())

def result(request):
    pass
    #return json
