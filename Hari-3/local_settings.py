# konfigurasi
vi /etc/openstack-dashboard/local_settings.py 
*script
# line 99: change Memcache server

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '$ip_addr:11211',
    },
}

# line 113: add

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# line 126: set Openstack Host

# line 127: comment out and add a line to specify URL of Keystone Host

OPENSTACK_HOST = "$ip_addr"
#OPENSTACK_KEYSTONE_URL = "http://%s/identity/v3" % OPENSTACK_HOST
OPENSTACK_KEYSTONE_URL = "http://$ip_addr:5000/v3"

# line 131: set your timezone

TIME_ZONE = "Asia/Jakarta"

# add to the end

OPENSTACK_KEYSTONE_MULTIDOMAIN_SUPPORT = True
OPENSTACK_KEYSTONE_DEFAULT_DOMAIN = 'Default'

root@dlp ~(keystone)# systemctl restart apache2

http://$ip_addr/horizon/ 
