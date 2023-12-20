from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from .models import Category, Tag, News, Author, DecorativeImages
from urllib.parse import unquote
import random

current_date = datetime.now()
formatted_date = current_date.strftime("%A, %B %d, %Y")

def news(request, title):
    title  = unquote(title)
    featured_news = News.objects.filter(featured=True)[:10]
    tranding_news = random.sample(
        list(featured_news), min(len(featured_news), 5))
    superuser_author = Author.objects.filter(user__is_superuser=True).first()
    categories = Category.objects.all()
    news = News.objects.filter(title=title).first()
    news_tags = []
    if_tags = news.tags.all()
    if if_tags:
        news_tags = if_tags
    all_tags = Tag.objects.all()
    random_image = DecorativeImages.objects.order_by('?').first()

    context = {
        'featured_news': featured_news,
        'categories': categories,
        'tags': all_tags,
        'tranding_news': tranding_news,
        'news_tags': news_tags,
        'news': news,
        'date': formatted_date,
        'youtube': superuser_author.youtube_url if superuser_author else '',
        'linkedin': superuser_author.linkedin_url if superuser_author else '',
        'facebook': superuser_author.facebook_url if superuser_author else '',
        'twitter': superuser_author.twitter_url if superuser_author else '',
        'tiktok': superuser_author.tiktok_url if superuser_author else '',
        'instagram': superuser_author.instagram_url if superuser_author else '',
        'image': random_image,

    }

    return render(request, 'news/single.html', context)

def home(request):
    featured_news = News.objects.filter(featured=True)[:10]
    tags = Tag.objects.order_by('?')[:10]
    categories = Category.objects.all()

    preview_categories = random.sample(
        list(categories), min(len(categories), 4))

    popular_news = random.sample(
        list(featured_news), min(len(featured_news), 6))

    midpoint = len(popular_news) // 2
    
    popular_new_first_half = popular_news[:midpoint]
    popular_new_second_half = popular_news[midpoint:]

    trending_news = random.sample(
        list(featured_news), min(len(featured_news), 5))

    superuser_author = Author.objects.filter(user__is_superuser=True).first()

    latest_news = News.objects.order_by('-date')[:6]
    midpoint = len(latest_news) // 2

    latest_new_first_half = latest_news[:midpoint]
    latest_new_second_half = latest_news[midpoint:]

    category_news = {}
    for category in categories:
        category_news[category] = News.objects.filter(
            category=category).order_by('-date')[:10]

    random_image = DecorativeImages.objects.order_by('?').first()

    context = {
        'featured_news': featured_news,
        'popular_news': popular_news,
        'popular_new_first_half': popular_new_first_half,
        'popular_new_second_half': popular_new_second_half,
        'latest_new_first_half': latest_new_first_half,
        'latest_new_second_half': latest_new_second_half,
        'trending_news': trending_news,
        'categories': categories,
        'preview_categories': preview_categories,
        'tags': tags,
        'date': formatted_date,
        'category_news': category_news,
        'date': formatted_date,
        'youtube': superuser_author.youtube_url if superuser_author else '',
        'linkedin': superuser_author.linkedin_url if superuser_author else '',
        'facebook': superuser_author.facebook_url if superuser_author else '',
        'twitter': superuser_author.twitter_url if superuser_author else '',
        'tiktok': superuser_author.tiktok_url if superuser_author else '',
        'instagram': superuser_author.instagram_url if superuser_author else '',
        'image': random_image
    }

    return render(request, 'news/index.html', context)


def categories(request):

    featured_news = News.objects.filter(featured=True)[:10]
    categories = Category.objects.all()
    tags = Tag.objects.order_by('?')[:10]
    trending_news = random.sample(
        list(featured_news), min(len(featured_news), 5))
    superuser_author = Author.objects.filter(user__is_superuser=True).first()
    random_image = DecorativeImages.objects.order_by('?').first()

    category_news = {}
    for category in categories:
        category_news[category] = News.objects.filter(
            category=category).order_by('-date')[:10]

    context = {
        'featured_news': featured_news,
        'tags': tags,
        'categories': categories,
        'trending_news': trending_news,
        'category_news': category_news,
        'date': formatted_date,
        'youtube': superuser_author.youtube_url if superuser_author else '',
        'linkedin': superuser_author.linkedin_url if superuser_author else '',
        'facebook': superuser_author.facebook_url if superuser_author else '',
        'twitter': superuser_author.twitter_url if superuser_author else '',
        'tiktok': superuser_author.tiktok_url if superuser_author else '',
        'instagram': superuser_author.instagram_url if superuser_author else '',
        'image': random_image,

    }
    return render(request, 'news/categories.html', context)


def category(request, name):
    featured_news = News.objects.filter(featured=True)[:10]
    category = Category.objects.filter(name=name).first()
    news = News.objects.filter(category=category.id).order_by('-date')

    items_per_page = 6
    paginator = Paginator(news, items_per_page)
    page = request.GET.get('page')

    try:
        news_page = paginator.page(page)
    except PageNotAnInteger:
        news_page = paginator.page(1)
    except EmptyPage:
        news_page = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    tags = Tag.objects.order_by('?')[:10]
    trending_news = random.sample(
        list(featured_news), min(len(featured_news), 5))
    superuser_author = Author.objects.filter(user__is_superuser=True).first()
    random_image = DecorativeImages.objects.order_by('?').first()

    context = {
        'featured_news': featured_news,
        'tags': tags,
        'categories': categories,
        'name': name,
        'news_page': news_page,
        'trending_news': trending_news,
        'date': formatted_date,
        'youtube': superuser_author.youtube_url if superuser_author else '',
        'linkedin': superuser_author.linkedin_url if superuser_author else '',
        'facebook': superuser_author.facebook_url if superuser_author else '',
        'twitter': superuser_author.twitter_url if superuser_author else '',
        'tiktok': superuser_author.tiktok_url if superuser_author else '',
        'instagram': superuser_author.instagram_url if superuser_author else '',
        'image': random_image,

    }
    return render(request, 'news/category.html', context)


def newsroom(request, option):

    featured_news = News.objects.filter(featured=True)[:10]
    categories = Category.objects.all()
    tags = Tag.objects.order_by('?')[:10]
    trending_news = random.sample(
        list(featured_news), min(len(featured_news), 5))
    superuser_author = Author.objects.filter(user__is_superuser=True).first()
    random_image = DecorativeImages.objects.order_by('?').first()

    if option == "Featured":
        news = News.objects.filter(featured=True).order_by('-date')
    elif option == "Popular":
        news = News.objects.filter(featured=True).order_by('-date')
    else:
        news = News.objects.all().order_by('-date')

    items_per_page = 6
    paginator = Paginator(news, items_per_page)
    page = request.GET.get('page')

    try:
        news_page = paginator.page(page)
    except PageNotAnInteger:
        news_page = paginator.page(1)
    except EmptyPage:
        news_page = paginator.page(paginator.num_pages)

    context = {
        'featured_news': featured_news,
        'tags': tags,
        'categories': categories,
        'name': option,
        'news_page': news_page,
        'trending_news': trending_news,
        'date': formatted_date,
        'youtube': superuser_author.youtube_url if superuser_author else '',
        'linkedin': superuser_author.linkedin_url if superuser_author else '',
        'facebook': superuser_author.facebook_url if superuser_author else '',
        'twitter': superuser_author.twitter_url if superuser_author else '',
        'tiktok': superuser_author.tiktok_url if superuser_author else '',
        'instagram': superuser_author.instagram_url if superuser_author else '',
        'image': random_image,

    }
    return render(request, 'news/newsroom.html', context)


def contact(request):
    superuser_author = Author.objects.filter(user__is_superuser=True).first()
    featured_news = News.objects.filter(featured=True)[:10]
    categories = Category.objects.all()
    tags = Tag.objects.order_by('?')[:10]
    context = {
        'featured_news': featured_news,
        'tags': tags,
        'categories': categories,
        'date': formatted_date,
        'youtube': superuser_author.youtube_url if superuser_author else '',
        'linkedin': superuser_author.linkedin_url if superuser_author else '',
        'facebook': superuser_author.facebook_url if superuser_author else '',
        'twitter': superuser_author.twitter_url if superuser_author else '',
        'tiktok': superuser_author.tiktok_url if superuser_author else '',
        'instagram': superuser_author.instagram_url if superuser_author else '',

    }
    return render(request, 'news/contact.html', context)
