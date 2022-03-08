# Azure Cache for Redis
# tutorial: https://docs.microsoft.com/en-us/azure/azure-cache-for-redis/cache-python-get-started

import redis

myHostname = 'dgi-psi.redis.cache.windows.net'
myPassword = '5zTXngbXCiScbMUafkZV0z3wCIyYsCTC9AzCaJvJNhQ='

r = redis.StrictRedis(host=myHostname, port=6380, db=0, password=myPassword, ssl=True)

print('Setting foo=bar...')
r.set('foo', 'bar')
print('Getting foo:')
foo = r.get('foo')
print(f" >> {foo}")