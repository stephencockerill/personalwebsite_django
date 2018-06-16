import glob
import markdown
import os
import requests

from django.http import HttpResponse
from django.shortcuts import render

from utils import BlogPostManager

blog_post_manager = BlogPostManager()

def index(request):
    context = {
        'nav_links': _nav_links(),
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'nav_links': _nav_links(),
        'experiences': [
            {
                'company': 'Lucid Design Group',
                'url': 'https://lucidconnects.com/',
                'title': 'Software Engineer',
                'start_date': 'August 2017',
                'end_date': 'Present',
            },
            {
                'company': 'Jitterbit Inc.',
                'url': 'https://www.jitterbit.com/',
                'title': 'Solutions Engineer',
                'start_date': 'January 2016',
                'end_date': 'July 2017',
            },
            {
                'company': 'Tata Consultancy Services',
                'url': 'https://www.tcs.com/',
                'title': 'Software Engineer',
                'start_date': 'July 2015',
                'end_date': 'December 2015',
            },
        ],
        'skills': [
            {
                'name': 'Python',
                'strength': '75',
            },
            {
                'name': 'HTML',
                'strength': '45',
            },
            {
                'name': 'CSS',
                'strength': '20',
            },
            {
                'name': 'Git',
                'strength': '40',
            },
            {
                'name': 'Bash',
                'strength': '30',
            },
            {
                'name': 'SQL',
                'strength': '60',
            },
        ],
        'educations': [
            {
                'school': 'Kickstart Coding',
                'majors': ['Python, Django, React, HTML &amp; More'],
                'minors': []
            },
            {
                'school': 'University of Delaware',
                'majors': ['Bachelor of Electrical Engineering'],
                'minors': [
                    'Minor in Computer Science',
                    'Minor in Sustainable Energy Technology',
                ]
            },
        ]
    }
    return render(request, 'about.html', context)

def projects(request):
    context = {
        'nav_links': _nav_links(),
        'projects': [
            {
                'name': 'Business Intelligence Pipeline',
                'description': '''Developed integrations of various data
                    sources into a shared data store for business intelligence
                    analytics.''',
                'stack': '''Python, Redshift, Pandas, MariaDB, Airflow,
                    Salesforce, Periscope Data''',
                'img': 'stiking_background_1.png',
            },
            {
                'name': 'Canonical Model',
                'description': '''Designed "Canonical" models for standard
                    business objects to easily integrate between software
                    systems.''',
                'stack': 'XML, XSD, REST, SOAP, JSON, Jitterbit',
                'img': 'stiking_background_2.png',
            },
        ],
    }
    return render(request, 'projects.html', context)

def blog(request):
    context = {
        'nav_links': _nav_links(),
        'feed': blog_post_manager.get_feed(),
    }
    return render(request, 'blog.html', context)

def blog_post(request, post_id):
    context = {
        'nav_links': _nav_links(),
        'post': blog_post_manager.get_post(post_id),
    }
    return render(request, 'blog_post.html', context)

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)


def _nav_links():
    return [
        {
            'path': '/',
            'title': 'Home',
        },
        {
            'path': '/about',
            'title': 'About',
        },
        {
            'path': '/projects',
            'title': 'Projects',
        },
        {
            'path': '/blog',
            'title': 'Blog',
        }
    ]

