# Fieldsets with inlines
### Mix inlines and fieldsets in any order in Django admin.

## What is it?

Django administration has nice feature to render related models as inlines
**under** the fieldsets out of the box. Unfortunately there is no easy
way to render inlines between fieldsets.

But when the size of the model becomes bigger, ordering of fieldsets and
related inlines becomes critical for the usability.

This package makes it easy to mix fieldsets and inlines in any order
you want with minimal changes required to your existing code.


## Requirements

- Python: 3.4+
- Django: 2.0+

## Installation

```
pip install django-fieldsets-with-inlines
```

Add `fieldsets_with_inlines` to your INSTALLED_APPS Django settings.py:

```python
INSTALLED_APPS = [
    ...
    'fieldsets_with_inlines',
    ...
]
```

## Usage

In your `admin.py` import `FieldsetsInlineMixin`, rename `fieldsets`
property to `fieldsets_with_inlines` and list inlines right between your
fieldsets. You could also remove `inlines` property:


```python
from fieldsets_with_inlines import FieldsetsInlineMixin

...

class TestAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
    fieldsets_with_inlines = [
        ('Objekt', {
            'fields': [
                ('ID_RNO', 'id', 'kljuc', 'slug'),
                'naziv',
                'kategorija']}),
        LastnistvoInline,
        ('Kontaktni podatki', {
            'fields': [
                ('kontaktna_oseba', 'email', 'poslji_obvestila')]}),
        KontaktInline,
        ('Dostop', {
            'fields': [
                'users',
                ('cas_vpisa', 'zadnja_sprememba', 'cas_zadnje_posodobitve')]}),
        OdjavaInline
    ]
```

