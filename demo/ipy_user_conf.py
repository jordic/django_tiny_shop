"""
Makes IPython import all of your projects models when shell is started.

1. Save as ipy_user_conf.py in project root
2. ./manage.py shell
3. profit

"""

import IPython.ipapi
ip = IPython.ipapi.get()


def main():
    imported = "\nImported models:\n\n"

    try:
        from django.db.models.loading import get_models
        for m in get_models():
            try:
                ip.ex("from %s import %s" % (m.__module__, m.__name__))
                imported += "%s.%s\n" % (m.__module__, m.__name__)
            except ImportError:
                pass
        print imported
    except ImportError:
        pass


main()