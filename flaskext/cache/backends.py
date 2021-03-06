from werkzeug.contrib.cache import (NullCache, SimpleCache, MemcachedCache,
                                    GAEMemcachedCache, FileSystemCache)

def null(app, args, kwargs):
    return NullCache()

def simple(app, args, kwargs):
    kwargs.update(dict(threshold=app.config['CACHE_THRESHOLD']))
    return SimpleCache(*args, **kwargs)

def memcached(app, args, kwargs):
    args.append(app.config['CACHE_MEMCACHED_SERVERS'])
    kwargs.update(dict(key_prefix=app.config['CACHE_KEY_PREFIX']))
    return MemcachedCache(*args, **kwargs)

def gaememcached(app, args, kwargs):
    kwargs.update(dict(key_prefix=app.config['CACHE_KEY_PREFIX']))
    return GAEMemcachedCache(*args, **kwargs)

def filesystem(app, args, kwargs):
    args.append(app.config['CACHE_DIR'])
    kwargs.update(dict(threshold=app.config['CACHE_THRESHOLD']))
    return FileSystemCache(*args, **kwargs)

# RedisCache is supported since Werkzeug 0.7.
try:
    from werkzeug.contrib.cache import RedisCache
except ImportError:
    pass
else:
    def redis(app, args, kwargs):
        kwargs.update(dict(host=app.config['CACHE_REDIS_HOST'],
                           port=app.config.get('CACHE_REDIS_PORT', 6379)))
        return RedisCache(*args, **kwargs)
    
