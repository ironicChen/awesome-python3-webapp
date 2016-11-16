from www import orm
from www.models import User
import asyncio


async def test(loop):
    await orm.create_pool(user='www-data', password='www-data', db='awesome', loop=loop)

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

    await orm.close_pool()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([test(loop)]))
    loop.close()
