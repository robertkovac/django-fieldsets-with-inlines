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

1. Include `FieldsetsInlineMixin` in your admin.py:

```python
from fieldsets_with_inlines import FieldsetsInlineMixin,
```

1. Add changes to your existing ModelAdmin classes in your admin.py:

* add `FieldsetsInlineMixin` to your admin.ModelAdmin declarations:
```
class TestAdmin(FieldsetsInlineMixin, admin.ModelAdmin)
```

* rename your `fieldsets` property to `fieldsets_with_inlines`

* in `fieldsets_with_inlines` property insert inlines beetween fieldsets
where you want them to be rendered

* remove `inlines` property


## Before and After

### Code before changes

```python
class TestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Objekt', {
            'fields': [
                ('ID_RNO', 'id', 'kljuc', 'slug'),
                'naziv',
                'kategorija']}),
        ('Kontaktni podatki', {
            'fields': [
                ('kontaktna_oseba', 'email', 'poslji_obvestila')]}),
        ('Dostop', {
            'fields': [
                'users',
                ('cas_vpisa', 'zadnja_sprememba', 'cas_zadnje_posodobitve')]}),
    ]
    inlines = [KontaktInline, LastnistvoInline, OdjavaInline]
```

### Code after changes

```python
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
