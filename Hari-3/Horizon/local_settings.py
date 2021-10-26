vim /etc/openstack-dashboard/local_settings.py 

# line 99: change Memcache server

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'IP_ADDRESS:11211',
    },
}

# line 113: add

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# line 126: set Openstack Host

# line 127: comment out and add a line to specify URL of Keystone Host

OPENSTACK_HOST = "IP_ADDRESS"
OPENSTACK_KEYSTONE_URL = "http://IP_ADDRESS:5000/v3"

# line 131: set your timezone

TIME_ZONE = "Asia/Jakarta"

# add to the end

OPENSTACK_KEYSTONE_MULTIDOMAIN_SUPPORT = True
OPENSTACK_KEYSTONE_DEFAULT_DOMAIN = 'Default'

root@dlp ~(keystone)# systemctl restart apache2

# Buka dibrowser

http://IP_ADDRESS/horizon/ 
