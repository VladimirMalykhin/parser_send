from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from questions.models import Results
from questions.forms import PostForm
from scrapy_project.spiders.starting_crawler import crawl, transfer_url, Urls, crawl_one_pages
from questions.asynctask import Resultsasync,start
from django.db import transaction
from _datetime import datetime, timedelta
from questions.checker import *
import csv
import xlwt



# sudo fuser -k 8000/tcp

def list_view(request):
    title = Results.objects.values_list('url', 'title')
    keywords = Results.objects.values_list('url', 'keywords')
    description = Results.objects.values_list('url', 'description')
    h1 = Results.objects.values_list('url', 'h1')
    h2 = Results.objects.values_list('url', 'h2')
    link = Results.objects.values_list('url')
    google_adwords = Results.objects.values_list('url', 'google')
    yandex_metricks = Results.objects.values_list('url', 'yandex')
    return render(request, 'questions/indes.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
        'link': link,
        'h1': h1,
        'h2': h2,
        'google_adwords': google_adwords,
        'yandex_metricks': yandex_metricks
    })


def contacts_view(request):
    return render(request, 'questions/contact.html', {

    })


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['title', 'title_error', 'keywords', 'description', 'description_error', 'h1', 'h2',
                     'url', 'yandex_metricks', 'google_analytics', 'date'])
    users = Results.objects.filter(base_url=Urls.base_url).values_list('title_unique', 'title', 'keywords', 'description_unique', 'description',
                                              'h1', 'h2', 'url', 'yandex', 'google', 'date_add')
    for user in users:
        writer.writerow(user)
    return response


def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('result of parsing')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['title', 'title_error', 'keywords', 'description', 'description_error', 'h1', 'h2',
               'url', 'yandex_metricks', 'google_analytics']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Results.objects.filter(base_url=Urls.base_url).values_list('title_unique', 'title', 'keywords', 'description_unique', 'description',
                                             'h1', 'h2', 'url', 'yandex', 'google')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response


def about_view(request):
    return render(request, 'questions/about.html', {

    })


def result_ruk(request):
    return render(request, 'questions/result_ruk.html', {

    })


def result_ruk_seo(request):
    title = Results.objects.values_list('url', 'title')
    keywords = Results.objects.values_list('url', 'keywords')
    description = Results.objects.values_list('url', 'description')
    h1 = Results.objects.values_list('url', 'h1')
    h2 = Results.objects.values_list('url', 'h2')
    link = Results.objects.values_list('url')
    broken_links = Results.objects.values_list('url', 'broken_link')
    google_adwords = Results.objects.values_list('url', 'google')
    yandex_metricks = Results.objects.values_list('url', 'yandex')
    return render(request, 'questions/result.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
        'broken_links':broken_links,
        'link': link,
        'h1': h1,
        'h2': h2,
        'google_adwords': google_adwords,
        'yandex_metricks': yandex_metricks
    })


def result_ruk_index(request):
    return render(request, 'questions/result_ruk_index.html', {

    })


def exportdate(request):
    return render(request, 'questions/exportdate.html', {

    })


def start_proccess(request):
    pass

    # os.environ.setdefault("SCRAPY_SETTINGS_MODULE", "whereyourscrapysettingsare")


def result_view(request):
    res = Results.objects.filter(base_url=Urls.base_url)
    count = res.count()
    try:
        title_count = res.filter(title="all right").count() / count
    except Exception as e:
        return HttpResponseRedirect('/')
    desc_count = res.filter(description="all right").count() / count
    key_count = res.filter(keywords="all right").count() / count
    broken_count = res.filter(broken_link=200).count() / count
    yandex_count = res.filter(yandex="('Есть',)").count()/count
    google_count = res.filter(google="('Есть',)").count() / count
    vk_count = res.filter(vk="('Есть',)").count() / count
    fb_count = res.filter(facebook="('Есть',)").count() / count
    in_count = res.filter(instagram="('Есть',)").count() / count
    percent = (title_count + desc_count + key_count +
               broken_count + yandex_count + google_count +
               in_count + vk_count + fb_count) / 9 * 100
    print(round(percent,1))
    title = res.values_list('url', 'title')
    keywords = res.values_list('url', 'keywords')
    description = res.values_list('url', 'description')
    h1 = res.values_list('url', 'h1')
    h2 = res.values_list('url', 'h2')
    link = res.values_list('url')
    broken_links = res.values_list('url', 'broken_link')
    google_adwords = res.values_list('url', 'google')
    yandex_metricks = res.values_list('url', 'yandex')
    return render(request, 'questions/result_ruk.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
        'broken_links': broken_links,
        'link': link,
        'h1': h1,
        'h2': h2,
        'google_adwords': google_adwords,
        'yandex_metricks': yandex_metricks
    })

def send_form(request):
    if request.method == 'POST':
        uri = request.POST['url']
        if('http' in uri):
            pass
        else:
            uri = "http://" + uri

        if check_url(uri) is True:
            date_today = datetime.today()

            date_adds = date_today - timedelta(days=1)

            short_url = str(uri).replace("http://", "").replace("https://", "")
            short = short_url.split("/")
            dates = [date_today, date_adds]
            Results.objects.exclude(date_add__in=dates).delete()
            Results.objects.filter(base_url=short[0]).delete()

            if request.POST['site'] is "1":
                crawl(uri, short[0])

            else:
                crawl_one_pages(uri, short[0])

            start(uri, short[0])
            transfer_url(uri, short[0])
            return HttpResponseRedirect('/result/')
        else:
            form = PostForm()
            return render(request, 'questions/form.html', {
                'form': form
            })
    else:
        form = PostForm()
        return render(request, 'questions/form.html', {
            'form': form
        })
