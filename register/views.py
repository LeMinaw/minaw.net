from django.shortcuts import render
from django.http      import HttpResponse
from django.db        import IntegrityError
from urllib.request   import urlopen
from hashlib          import sha256
from os               import environ
from register.models  import *
from register.forms   import *
from register.data    import ACTIVATION_KEYS
import requests
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
            if "<span>%s</span>" % username in userlist:
                code_crypt = code.encode('utf-8')
                code_crypt = sha256(code_crypt).hexdigest()
                try:
                    db_code = ActivationCode.objects.get(code=code_crypt)
                    if db_code.active:
                        user = Member(username=username, user_rank=db_code.rank)
                        try:
                            user.save()
                            db_code.active = False
                            db_code.save()
                            success = True
                            data = {'username':username, 'user_rank':db_code.rank}
                            r = requests.post("https://www.skywanderersgame.com/private/setrank.php", data=data, auth=('skywdr', environ.get("RANKS_PWD")))
                        except IntegrityError:
                            error = "This username is already using an activation code."
                    else:
                        error = "This activation code has already been used."
                except ActivationCode.DoesNotExist:
                    error = "Invalid activation code!"
            else:
                error = "This username is not registered on the Skywanderers forums!"
    else:
        form = RegisterForm()

    return render(request, "register/main.html", locals())


def load(request):
    if environ.get("LOAD_KEYS") == 'TRUE':
        for code, rank in ACTIVATION_KEYS.items():
            activation_code = ActivationCode(code=code, rank=rank, active=True, active_disc=True)
            try:
                activation_code.save()
            except IntegrityError:
                print("The code %s already exists in base." % code)
        return HttpResponse("done")
    return HttpResponse("nope")
