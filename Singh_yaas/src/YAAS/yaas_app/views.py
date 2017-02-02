from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.views.generic import TemplateView
from YAAS import settings
from forms import MyRegistrationForm, create_auction_form
from forms import UserEditForm
from yaas_app.models import Auction
from django.contrib import auth
from models import Auction
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils import translation

def a(request):
    try:
        if not request.session["lang"]:
            request.session["lang"] = "en"
            translation.activate(request.session["lang"])
        else:
            translation.activate(request.session["lang"])
    except KeyError:
        request.session["lang"] = "en"
        translation.activate(request.session["lang"])

    if request.user.is_authenticated():
        msg = 'loggedin'
    else:
        msg = ''
    return render_to_response('auction/list.html',
                             {'a_obj' : Auction.objects.all(),
                              'full_name': request.user.username,
                              'language':language,
                              'loggedin':msg},context_instance = RequestContext(request))

def b(request, b_id = 1):
    return render_to_response('auction/detail.html',
                             {'b_obj' : Auction.objects.get(id=b_id)})

def language(request, lang = ''):
    request.session["lang"] = lang
    translation.activate(request.session["lang"])

    return HttpResponseRedirect('/auction/')

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/auction/')
    else:
        return HttpResponseRedirect('/auction/invalid')

def login(request):
    return render_to_response('user/login.html', context_instance = RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/auction/')

def loggedin(request):
    articlelist = Auction.objects.all().order_by("id")

    return render_to_response('user/loggedin.html',
                              {'full_name': request.user.username,
                               'article_list': articlelist})

def invalid_login(request):
    return render_to_response('user/invalid_login.html')

def register_user(request):
    if request.method =='POST':
        form = MyRegistrationForm(request.POST)
        print 'post'
        print form.is_valid()
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/auction/register_success')

    form = MyRegistrationForm()
    return  render_to_response('user/register.html',{'form':form},context_instance = RequestContext(request))

def edit_user(request):
    if request.method == 'POST':
        form = UserEditForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/auction/')
    else:
        form = UserEditForm(user=request.user)
        return render_to_response('user/edit.html',
                              {'form': form, 'full_name': request.user.username },context_instance = RequestContext(request))
def register_success(request):
    return render_to_response('user/register_success.html')

@login_required(login_url='/login/')
def create_auction(request):
    if request.method == 'POST' and request.POST.get('title') and request.POST.get('category') and request.POST.get('price') and request.POST.get('enddate'):
            if int(request.POST.get('price')) <= 0:
                return render_to_response('auction/create.html',
                              {'title': request.POST.get('title'),
                               'category': request.POST.get('category'),
                               'desc': request.POST.get('description'),
                               'edate': request.POST.get('enddate'),
                               'price': request.POST.get('price'),
                               'pinfo':'Price should not be less than 0.'
                               },context_instance = RequestContext(request))
            try:
                timediff = datetime.strptime(str(request.POST['enddate']), "%Y-%m-%d %H:%M") - datetime.now()
                hourdiff = timediff.total_seconds() / 60 / 60

                if hourdiff < 72:
                    return render_to_response('auction/create.html',
                              {'title': request.POST.get('title'),
                               'category': request.POST.get('category'),
                               'desc': request.POST.get('description'),
                               'edate': request.POST.get('enddate'),
                               'price': request.POST.get('price'),
                               'dinfo':'End Date should not be less the 72 hours from now.'
                               },context_instance = RequestContext(request))



                return render_to_response('confirm_auction.html',
                              {'title': request.POST.get('title'),
                               'category': request.POST.get('category'),
                               'desc': request.POST.get('description'),
                               'edate': request.POST.get('enddate'),
                               'price': request.POST.get('price')
                               },context_instance = RequestContext(request))
            except:
                return render_to_response('auction/create.html',
                              {'title': request.POST.get('title'),
                               'category': request.POST.get('category'),
                               'desc': request.POST.get('description'),
                               'edate': request.POST.get('enddate'),
                               'price': request.POST.get('price'),
                               'dinfo':'Check the date format.'
                               },context_instance = RequestContext(request))






            return render_to_response('confirm_auction.html',
                              {'title': request.POST.get('title'),
                               'category': request.POST.get('category'),
                               'desc': request.POST.get('description'),
                               'edate': request.POST.get('enddate'),
                               'price': request.POST.get('price')
                               },context_instance = RequestContext(request))
    elif request.method == 'POST':
        return render_to_response('auction/create.html',
                              {'title': request.POST.get('title'),
                               'category': request.POST.get('category'),
                               'desc': request.POST.get('description'),
                               'edate': request.POST.get('enddate'),
                               'price': request.POST.get('price'),
                               'info':'invalid'
                               },context_instance = RequestContext(request))

    return render_to_response('auction/create.html',
                              {'full_name': request.user.username},context_instance = RequestContext(request))

@login_required(login_url='/login/')
def save_auction(request):
    print request.POST.get('option')
    if request.POST.get('option') == 'yes':
        art=Auction(title = request.POST.get('title'),
                            category = request.POST.get('category'),
                            description = request.POST.get('desc'),
                            price = request.POST.get('price'),
                            startdate = datetime.now().strftime('%Y-%m-%d %H:%M'),
                            enddate=datetime.strptime(request.POST.get('edate'),'%Y-%m-%d %H:%M'),
                            seller =request.user.username
                            )
        art.save()
        return render_to_response('auction/list.html',
                             {'a_obj' : Auction.objects.all(),'info':'Auction was saved'},context_instance = RequestContext(request))

    else:
        return render_to_response('auction/list.html',
                             {'a_obj' : Auction.objects.all(),'info':'Auction was discarded'},context_instance = RequestContext(request))

@login_required(login_url='/login/')
def edit_auction(request, id):

    auc = Auction.objects.get(id=id)
    if request.method == 'POST':
        auc.description = request.POST.get('description')
        auc.save()
        return render_to_response('auction/list.html',
                             {'a_obj' : Auction.objects.all(),'info':'Auction was updated'},context_instance = RequestContext(request))
    return render_to_response('auction/edit.html',
                              {'full_name': request.user.username,
                               'title_v':auc.title,
                               'category_v':auc.category,
                               'desc_v':auc.description,
                               'price_v':auc.price},context_instance = RequestContext(request))

def bid_acution(request, id):
    auc = Auction.objects.get(id=id)
    if request.method == 'POST':
        auc.price = request.POST.get('newprice')
        auc.save()
        return HttpResponseRedirect('/auction/')

    return render_to_response('auction/bid.html',
         {'auc': auc, 'full_name': request.user.username},context_instance = RequestContext(request))

@login_required(login_url='/login/')
def ban_acution(request, id):
    auc = Auction.objects.get(id=id)

    if request.user.is_superuser:
        auc.status = 'banned'
        auc.save()
        return render_to_response('auction/list.html',
                             {'a_obj' : Auction.objects.all(),'info':'Auction was banned by admin'})
    else:
        return render_to_response('auction/list.html',
                                 {'a_obj' : Auction.objects.all(),'info':'You are not the admin for this task.'})


def search_auction(request):
    if request.POST.get('word'):
        auc = Auction.objects.filter(title = request.POST.get('word'))
        if auc:
            return render_to_response('auction/list.html',
                                 {'a_obj' : auc},context_instance = RequestContext(request))
    return render_to_response('auction/list.html',{'info':'No results found'},context_instance = RequestContext(request))
