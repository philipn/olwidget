#!/usr/bin/env python
import os

from distutils.command.install import INSTALL_SCHEMES
from distutils.core import setup

root = os.path.abspath(os.path.dirname(__file__))
os.chdir(root)

VERSION = '0.46-custom2'

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

setup(name='django-olwidget',
    version=VERSION,
    description="OpenLayers mapping widget for Django",
    author='Charlie DeTar',
    author_email='cfd@media.mit.edu',
    url='http://olwidget.org',
    packages=['olwidget'],
    package_dir={'': 'django-olwidget'},
    package_data={'olwidget': [
         'templates/olwidget/editable_layer.html',
         'templates/olwidget/admin_olwidget.html',
         'templates/olwidget/info_layer.html',
         'templates/olwidget/multi_layer_map.html',
         'templates/admin/olwidget_change_list.html',
         'static/olwidget/css/olwidget.css',
         'static/olwidget/js/cloudmade.js',
         'static/olwidget/js/olwidget.js',
         'static/olwidget/img/popup_icons.png',
         'static/olwidget/img/jquery_ui_license.txt',
         'static/olwidget/img/extra_edit_icons.png',
         'static/olwidget/img/extra_edit_icons.xcf']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    include_package_data=True,
    zip_safe=False,
)
