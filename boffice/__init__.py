import os

VERSION = (0, 1, 0)


def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    return version


# Cheeky setting that allows each template to be accessible by two paths.
# Eg: the template 'oscar/templates/oscar/base.html' can be accessed via both
# 'base.html' and 'oscar/base.html'.  This allows Oscar's templates to be
# extended by templates with the same filename
BOFFICE_MAIN_TEMPLATE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'templates/boffice')

BOFFICE_CORE_APPS = [
    'boffice',
    'boffice.cliente',
    'boffice.template',
    'boffice.tassa',
    'boffice.movimento',
    'boffice.documento',
]


def get_core_apps(overrides=None):
    """
    Return a list of oscar's apps amended with any passed overrides
    """
    if not overrides:
        return BOFFICE_CORE_APPS

    def get_app_label(app_label, overrides):
        pattern = app_label.replace('boffice.apps.', '')
        for override in overrides:
            if override.endswith(pattern):
                if 'dashboard' in override and 'dashboard' not in pattern:
                    continue
                return override
        return app_label

    apps = []
    for app_label in BOFFICE_CORE_APPS:
        apps.append(get_app_label(app_label, overrides))
    return apps
