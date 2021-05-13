# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy

from create_profile.models import CreateNeighbour, CreateBusiness, LikeModel, LikeBusinesModel


def index(request):
    # Главная
    if request.user.is_authenticated:
        # при авторизации сообщение пользоваиелям у кого встречные лайки соседей
        posts_n = LikeModel.objects.filter(first_id=request.user.id).values()
        if len(posts_n) > 0:
            for post_n in posts_n:
                messages.success(request, 'Вас лайкнул пользователь: ' + post_n['like_second'])
                messages.success(request, ' Напишите ему: ' + post_n['email_second'])

        # при авторизации сообщение пользоваиелям у кого встречные лайки бизнес
        posts_b = LikeBusinesModel.objects.filter(first_id=request.user.id).values()
        if len(posts_b) > 0:
            for post_b in posts_b:
                messages.success(request, 'Вас лайкнул бизнес пользователь: ' + post_b['like_second'])
                messages.success(request, 'Почта для связи: ' + post_b['email_second'])

        return render(request, 'index.html', {'user':request.user})
    else:
        return render(request, 'index.html', )

@login_required(login_url=reverse_lazy('login'))
def all_filter_search(request):
    # выводим все анкеты
    list_tmp_13 = 0
    catalog_filter = CreateNeighbour.objects.values_list('id',
                                                          'name',
                                                          'gender',
                                                          'gender_neighb',
                                                          'sel_city',
                                                          'sel_distr',
                                                          'presence_animals',
                                                          'presence_flat',
                                                          'attitude_animals',
                                                          'attitude_smok',
                                                          'about_me',
                                                          'image',
                                                          'user_neig',)

    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    # формируем масив лдя прорисовки в шблоне
    for all_goods_s in catalog_filter:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods:

            p = CreateNeighbour(gender=tmp_s[2])
            gender = p.get_gender_display()

            p = CreateNeighbour(gender_neighb=tmp_s[3])
            gender_neighb = p.get_gender_neighb_display()

            p = CreateNeighbour(sel_city=tmp_s[4])
            sel_city = p.get_sel_city_display()

            p = CreateNeighbour(sel_distr=tmp_s[5])
            sel_distr = p.get_sel_distr_display()

            p = CreateNeighbour(attitude_animals=tmp_s[8])
            attitude_animals = p.get_attitude_animals_display()

            p = CreateNeighbour(attitude_smok=tmp_s[9])
            attitude_smok = p.get_attitude_smok_display()

            list_tmp = list(tmp_s)
            list_tmp[2] = gender
            list_tmp[3] = gender_neighb
            list_tmp[4] = sel_city
            list_tmp[5] = sel_distr
            list_tmp[8] = attitude_animals
            list_tmp[9] = attitude_smok
            user_like = LikeModel.objects.filter(first_id=tmp_s[12]).filter(second_id=request.user.id).values_list('id') # лайки в шаблоне
            flag = 0
            if len(user_like) > 0:
                flag = '1'
            else:
                flag = '0'
            list_tmp.append(flag)
            list_tmp = tuple(list_tmp)

            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s
        tmp_categ_name.append(tmp_categ_name_list) # формируем массив со всеми анкетами

    return render(request, 'all_neighb.html', {'serxh_filer': tmp_categ_name})


@login_required(login_url=reverse_lazy('login'))
def filter_search(request):
    # поиск соседей по 3 фильтрам

    gender_start = 1
    gender_end = 2
    cities_start = 1
    cities_end = 6
    districts_start = 1
    districts_end = 7
    if request.POST.get('gender') != None:
        gender_start = request.POST.get('gender')
    if request.POST.get('gender') != None:
        gender_end = request.POST.get('gender')
    if request.POST.get('cities') != None:
        cities_start = request.POST.get('cities')
    if request.POST.get('cities') != None:
        cities_end = request.POST.get('cities')
    if request.POST.get('districts') != None:
        districts_start = request.POST.get('districts')
    if request.POST.get('districts') != None:
        districts_end = request.POST.get('districts')
    # фильтры
    catalog_filter = CreateNeighbour.objects.filter(gender__gte=gender_start).filter(gender__lte=int(gender_end)) \
        .filter(sel_city__gte=cities_start).filter(sel_city__lte=int(cities_end)) \
        .filter(sel_distr__gte=districts_start).filter(sel_distr__lte=int(districts_end)) \
        .values_list('id',
                     'name',
                     'gender',
                     'gender_neighb',
                     'sel_city',
                     'sel_distr',
                     'presence_animals',
                     'presence_flat',
                     'attitude_animals',
                     'attitude_smok',
                     'about_me',
                     'image',
                     'user_neig',)

    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in catalog_filter:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods:

            p = CreateNeighbour(gender=tmp_s[2])
            gender = p.get_gender_display()

            p = CreateNeighbour(gender_neighb=tmp_s[3])
            gender_neighb = p.get_gender_neighb_display()

            p = CreateNeighbour(sel_city=tmp_s[4])
            sel_city = p.get_sel_city_display()

            p = CreateNeighbour(sel_distr=tmp_s[5])
            sel_distr = p.get_sel_distr_display()

            p = CreateNeighbour(attitude_animals=tmp_s[8])
            attitude_animals = p.get_attitude_animals_display()

            p = CreateNeighbour(attitude_smok=tmp_s[9])
            attitude_smok = p.get_attitude_smok_display()

            list_tmp = list(tmp_s)
            list_tmp[2] = gender
            list_tmp[3] = gender_neighb
            list_tmp[4] = sel_city
            list_tmp[5] = sel_distr
            list_tmp[8] = attitude_animals
            list_tmp[9] = attitude_smok
            user_like = LikeModel.objects.filter(first_id=tmp_s[12]).filter(second_id=request.user.id).values_list('id')
            flag = 0
            if len(user_like) > 0:
                flag = '1'
            else:
                flag = '0'
            list_tmp.append(flag)
            list_tmp = tuple(list_tmp)

            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s
        tmp_categ_name.append(tmp_categ_name_list)


    return render(request, 'filter_search.html', {'serxh_filer': tmp_categ_name,})

@login_required(login_url=reverse_lazy('login'))
def all_busines(request):
    # весь бизнес
    # формируем массив со всеми анкетами
    search_filer = CreateBusiness.objects.values_list('name_bus',
                                                       'sel_city',
                                                       'sel_distr',
                                                       'category_bus',
                                                       'about_me',
                                                       'image',
                                                       'user_bus',
                                                       'id',)
    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in search_filer:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods:

            p = CreateBusiness(sel_city=tmp_s[1])
            sel_city = p.get_sel_city_display()

            p = CreateBusiness(sel_distr=tmp_s[2])
            sel_distr = p.get_sel_distr_display()

            list_tmp = list(tmp_s)
            list_tmp[1] = sel_city
            list_tmp[2] = sel_distr
            # лайки
            user_like = LikeBusinesModel.objects.filter(first_id=tmp_s[6]).filter(second_id=request.user.id).values_list('id')
            flag = 0
            if len(user_like) > 0:
                flag = '1'
            else:
                flag = '0'
            list_tmp.append(flag)
            list_tmp = tuple(list_tmp)
            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s
        tmp_categ_name.append(tmp_categ_name_list)# формируем массив со всеми анкетами
    return render(request, 'all_busines.html', {'serxh_filer': tmp_categ_name})

@login_required(login_url=reverse_lazy('login'))
def filter_search_busines(request):
    # поиск по бизнесу
    # поиск по трем фильтрм
    request.POST.get('name_bus')
    cities_start = 1
    cities_end = 6
    districts_start = 1
    districts_end = 7
    if request.POST.get('cities') != None:
        cities_start = request.POST.get('cities')
    if request.POST.get('cities') != None:
        cities_end = request.POST.get('cities')
    if request.POST.get('districts') != None:
        districts_start = request.POST.get('districts')
    if request.POST.get('districts') != None:
        districts_end = request.POST.get('districts')
    name_bus = request.POST.get('name_bus')
    # фильтруем и формируем массив со всеми анкетами
    search_filer = CreateBusiness.objects.filter(sel_city__gte=cities_start).filter(sel_city__lte=int(cities_end)) \
                                        .filter(sel_distr__gte=districts_start).filter(sel_distr__lte=int(districts_end)) \
                                        .filter(category_bus__icontains=name_bus).values_list('name_bus',
                                                                                     'sel_city',
                                                                                     'sel_distr',
                                                                                     'category_bus',
                                                                                     'about_me',
                                                                                     'image',
                                                                                     'user_bus',
                                                                                     'id',)

    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in search_filer:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods:

            p = CreateBusiness(sel_city=tmp_s[1])
            sel_city = p.get_sel_city_display()

            p = CreateBusiness(sel_distr=tmp_s[2])
            sel_distr = p.get_sel_distr_display()

            list_tmp = list(tmp_s)
            list_tmp[1] = sel_city
            list_tmp[2] = sel_distr
            user_like = LikeBusinesModel.objects.filter(first_id=tmp_s[6]).filter(second_id=request.user.id).values_list('id')
            flag = 0
            if len(user_like) > 0:
                flag = '1'
            else:
                flag = '0'
            list_tmp.append(flag)
            list_tmp = tuple(list_tmp)
            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s
        tmp_categ_name.append(tmp_categ_name_list)# формируем массив со всеми анкетами
    return render(request, 'search_busines.html', {'serxh_filer': tmp_categ_name})

def likes(request):
    # likes заносим в таблицу лайкующего и хозяйна анкеты
    test_user = User.objects.filter(id=request.POST.get('first')).values('username', 'email')
    nearly_final = LikeModel(like_first=test_user[0]['username'], email_first=test_user[0]['email'],
                             like_second=request.POST.get('second'), email_second=request.POST.get('email'),
                             first_id=request.POST.get('first'), second_id=request.POST.get('second_id'),
                             id_ancket=request.POST.get('id_ancket'),)
    nearly_final.save(force_insert=True)
    return redirect('/all_neighb/')

def likes_busines(request):
    # likes заносим в таблицу лайкующего и хозяйна анкеты
    test_user = User.objects.filter(id=request.POST.get('first')).values('username', 'email')
    nearly_final = LikeBusinesModel(like_first=test_user[0]['username'], email_first=test_user[0]['email'],
                                    like_second=request.POST.get('second'), email_second=request.POST.get('email'),
                                    first_id=request.POST.get('first'), second_id=request.POST.get('second_id'),
                                    id_ancket=request.POST.get('id_ancket'),)
    nearly_final.save(force_insert=True)
    return redirect('/all_busines/')

def statistics(request):
    # статистика
    all_likes = LikeModel.objects.filter(like_first=request.user).values_list('like_second')
    all_likes_b = LikeBusinesModel.objects.filter(like_first=request.user).values_list('like_second')
    count_us = User.objects.values_list()
    count_users = (len(count_us))
    all_likes_n = (len(all_likes))
    all_likes_bus = (len(all_likes_b))

    return render(request, 'statistics.html', {'count_users':count_users, 'all_likes_n': all_likes_n, 'all_likes_bus': all_likes_bus})
