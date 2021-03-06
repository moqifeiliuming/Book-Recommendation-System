"""
Django settings for book project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&7#ihc_c=k)@=7c#b-g1r&$%cc(!^*t6i5lg#&se%v#=ji&yv7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'book.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'book.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # ??????????????????MySQL??????????????????
        'NAME': 'douban',  # ???????????????
        'USER': 'root',  # ??????????????????
        'PASSWORD': 'root',  # ????????????
        'HOST': 'localhost',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4', }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
static = os.path.dirname(os.path.abspath(__file__))
static = os.path.join(static, "../")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static/"),
]
#STATIC_ROOT = "static/"
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# ?????????????????????????????????????????????

TINYMCE_DEFAULT_CONFIG = {

    # ??????????????????,???????????????????????????
    'theme': 'advanced',
    # 'theme': 'simple',
    # ??????????????????????????????(RTF=rich text format)?????????
    'width': 800,
    'height': 600,

    # ??????
    'language': 'zh',

    # ??????????????????????????????
    'style_formats': [
        # title=????????????
        # styles=?????????css??????
        # inline:xxx = ???????????????????????????????????????????????????
        # block:xxx = ???????????????????????????????????????????????????
        {'title': 'Bold text', 'inline': 'b'},
        {'title': 'Red text', 'inline': 'span', 'styles': {'color': '#ff0000'}},
        {'title': 'Red header', 'block': 'h1', 'styles': {'color': '#ff0000'}},
        {'title': 'Example 1', 'inline': 'span', 'classes': 'example1'},
        {'title': 'Example 2', 'inline': 'span', 'classes': 'example2'},
        {'title': 'Table styles'},
        {'title': 'Table row 1', 'selector': 'tr', 'classes': 'tablerow1'}
    ],
}