=====
Forum
=====

Forum is a Django app for adding reddit like functionality to the website. Users can post on various boards, comment and upvote.

Detailed documentation is yet to be done.

Quick start
-----------

1. Add "forum" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'forum',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('forum/', include('forum.urls')),

3. Run ``python manage.py migrate`` to create the forum models.

4. Start the development server and visit http://127.0.0.1:8000/forum/
