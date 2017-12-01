from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='ww_2t+1bs0@qb7t_la&4@s_^&b69o=ttfn7f5mb0@6ql0bm@si')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
