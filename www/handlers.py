from www.coreweb import get


@get('/')
def index():
    return 'Hello!'


@get('/name/{name}')
def index2(name):
    return 'Hello %s!' % name
