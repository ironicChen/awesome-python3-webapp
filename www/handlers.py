from www.coreweb import get


@get('/')
def index():
    return 'Hello!'
