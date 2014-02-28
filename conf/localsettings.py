DEBUG = True

#######################################################################
# These config values vary on an install-by-install basis. If you
# installed using the Ubuntu package, these should be pre-set.
#######################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'localwiki',
        'USER': 'localwiki',
        'PASSWORD': 'LekqVED5cD29vYXAKhAhy9uYtgotHC',
        'HOST': '127.0.0.1',
    }
}

# Get an API key at http://cloudmade.com/start.
CLOUDMADE_API_KEY = '05593ab1cac94076aea63e6adcc842c0'

# For testing, you can start the python debugging smtp server like so:
# sudo python -m smtpd -n -c DebuggingServer localhost:25
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

#######################################################################
# Other config values.
#######################################################################

SITE_THEME = 'sapling'

OLWIDGET_DEFAULT_OPTIONS = {
    'default_lat': 40.002498,
    'default_lon': -75.118033,
    'default_zoom': 14,
    'zoom_to_data_extent_min': 16,

    'layers': ['cloudmade.35165', 've.aerial'],
    'map_options': {
        'controls': ['Navigation', 'PanZoomBar', 'KeyboardDefaults'],
        'theme': '/static/openlayers/theme/sapling/style.css',
    },
    'overlay_style': {'fillColor': '#ffc868',
                      'strokeColor': '#db9e33',
                      'strokeDashstyle': 'solid'},
    'map_div_class': 'mapwidget',
}

DAISYDIFF_URL = 'http://localhost:8080/daisydiff/diff'
DAISYDIFF_MERGE_URL = 'http://localhost:8080/daisydiff/merge'

# list of regular expressions for white listing embedded URLs
EMBED_ALLOWED_SRC = ['.*']

HAYSTACK_SOLR_URL = 'http://localhost:8080/solr'

LOCAL_INSTALLED_APPS = ()

CACHE_BACKEND = 'dummy:///'

# This is auto-generated.
SECRET_KEY = '+7kxj_ztpl^(*2p9-i^j@oe&z2qb)sfvv-ulyz&*gw_d0yj^+z'
