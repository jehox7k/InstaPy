import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'romancesfoto'
insta_password = 'parangari787'

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

try:
    session.login()

    # settings
    #session.set_upper_follower_count(limit=2500)
    session.set_do_comment(True, percentage=10)
    session.set_comments(['Excelente galeria.', 'muy buenas tus publicaciones. Saludos', 'Buenos tus posts. Felicidades', 'Geniales tus publicaciones.'])
    session.set_dont_include(['friend1', 'friend2', 'friend3'])
    session.set_dont_like(['pizza'])

    # actions
    session.like_by_tags(['natgeo'], amount=1)
    session.set_ignore_users(['taebom', 'fernandoanunez'])
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.like_by_tags(['santiagodechile'], amount=200, interact=True)
    session.like_by_locations(['220705331/guayaquil-ecuador/'], amount=100)
    session.like_by_locations(['26914683/santiago-chile/'], amount=100)
    session.like_by_locations(['216178352/vina-del-mar-chile/'], amount=100)
    session.like_by_locations(['427386520/santiago-metropolitan-region/'], amount=100)
    session.like_by_locations(['1020867845/iglesia-de-dios-de-la-profecia/'], amount=100)
    session.like_by_locations(['250235962/loncura-valparaiso-chile/'], amount=100)
    session.like_by_locations(['222190475/maipu-chile/'], amount=100)
    session.like_by_tags(['chilena'], amount=200, interact=True)
    session.like_by_tags(['chileangirl'], amount=200, interact=True)
    session.like_by_tags(['ecuador'], amount=200, interact=True)
    session.like_by_tags(['ecuatoriana'], amount=200, interact=True)
    session.like_by_tags(['guayaquil'], amount=200, interact=True)
except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
