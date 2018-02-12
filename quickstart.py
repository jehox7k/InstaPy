from instapy import InstaPy

insta_username = 'romancesfoto'
insta_password = ''

# set headless_browser=True if you want to run InstaPy on a server
try:
    # set these if you're locating the library in the /usr/lib/pythonX.X/ directory
    # Settings.database_location = '/path/to/instapy.db'
    # Settings.browser_location = '/path/to/chromedriver'
    
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False,
                      multi_logs=True)
    session.login()

    # set up all the settings
    #session.set_upper_follower_count(limit=2500)
    session.set_do_comment(True, percentage=80)
    session.set_comments(['Excelente galeria', 'muy buenas tus publicaciones', 'Buenos tus posts', 'Geniales tus publicaciones'])
    #session.set_dont_include(['friend1', 'friend2', 'friend3'])
    #session.set_dont_like(['pizza', 'girl'])

    #session.set_dont_unfollow_active_users(enabled=True, posts=6)
    #session.unfollow_users(amount=100, onlyInstapyMethod = 'FIFO', sleep_delay=10 )

    session.set_ignore_users(['taebom', 'fernandoanunez'])

    # do the actual liking

    #session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
    session.like_by_tags(['chileangirl'], amount=100)

    session.like_by_locations(['758392441/caracas/'], amount=100)
    session.like_by_locations(['216143032/la-guaira-venezuela/'], amount=100)
    session.like_by_locations(['215994674/tucacas-falcon-venezuela/'], amount=100)
    session.like_by_locations(['213922485/morrocoy-falcon-venezuela/'], amount=100)
    session.like_by_locations(['267435277113211/parque-nacional-el-avila-caracas-venezuela/'], amount=100)
    session.like_by_locations(['26914683/santiago-chile/'], amount=100)
    session.like_by_locations(['216178352/vina-del-mar-chile/'], amount=100)
    session.like_by_locations(['427386520/santiago-metropolitan-region/'], amount=100)
    session.like_by_locations(['1020867845/iglesia-de-dios-de-la-profecia/'], amount=100)
    session.like_by_locations(['250235962/loncura-valparaiso-chile/'], amount=100)
    session.like_by_locations(['222190475/maipu-chile/'], amount=100)

finally:
    # end the bot session
    session.end()
