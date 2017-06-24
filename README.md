Secret project C
===================

[![Build Status](https://travis-ci.org/fevsea/projectC.svg?branch=master)](https://travis-ci.org/fevsea/projectC)


## Introduction
**This is a work in progress. Not functional. Yet.**

All kind of documentation, coments etc. are only for personal reference

Name due to historic reasons. Not actually secret.


## Development

### Tech used

- D*j*ango 1.11.2
- LiteSQL
- Python 3.5
- Bootstrap

### Considerations
- Multilanguage (always mark string translatable)
- TDD (Every change should be driven by a test)
- Responsive design

### Usefull commands
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser`

## Translators

- `django-admin makemessages -a`   Collect translatable strings
- Translate .po files (_projectC/locale/XX/LC_MESSAGES/*.po_)
- `django-admin compilemessages`  #-> Generate .po files 

## About
Website initial backbone template: [Start-bootstrap Modern Business](https://startbootstrap.com/template-overviews/modern-business/)