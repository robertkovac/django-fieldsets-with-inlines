# Fieldsets with inlines
### Mixin inlines and fieldsets in Django admin.

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
- Django: >=2.0

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

```
class TestAdmin(FieldsetsInlineMixin, admin.ModelAdmin)
```

* rename your `fieldsets` property to `fieldsets_with_inlines`

* insert inlines beetween fieldsets where you want them to be rendered

**With fieldsets-with-inlines inlines are not automaticaly rendered after your
fieldsets! Every inline that you want rendered should be added to your
fieldsets_with_inlines property.**

**Inlines property still has to be defined!**


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
        ('Naslov', {
            'fields': [
                ('obcina', 'obmocje'),
                ('naseljeulica', 'hisna_stevilka', 'hisna_stevilka_pripona'),
                ('ulica', 'kraj', 'posta')]}),
        ('Ponudnik', {
            'fields': [
                'ponudnik',
                ('ID_cadis', 'remote_id'),
                'polovicna_taksa']}),
        ('Kontaktni podatki', {
            'fields': [
                ('kontaktna_oseba', 'email', 'poslji_obvestila')]}),
        ('Nastanitvena kapaciteta', {
            'fields': ['stevilo_stalnih_lezisc']}),
        ('Dostop', {
            'fields': [
                'users',
                ('cas_vpisa', 'zadnja_sprememba', 'cas_zadnje_posodobitve')]}),
        ('Opombe', {
            'fields': ['opombe']}),
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
        ('Naslov', {
            'fields': [
                ('obcina', 'obmocje'),
                ('naseljeulica', 'hisna_stevilka', 'hisna_stevilka_pripona'),
                ('ulica', 'kraj', 'posta')]}),
        ('Ponudnik', {
            'fields': [
                'ponudnik',
                ('ID_cadis', 'remote_id'),
                'polovicna_taksa']}),
        LastnistvoInline,
        ('Kontaktni podatki', {
            'fields': [
                ('kontaktna_oseba', 'email', 'poslji_obvestila')]}),
        KontaktInline,
        ('Nastanitvena kapaciteta', {
            'fields': ['stevilo_stalnih_lezisc']}),
        ('Dostop', {
            'fields': [
                'users',
                ('cas_vpisa', 'zadnja_sprememba', 'cas_zadnje_posodobitve')]}),
        ('Opombe', {
            'fields': ['opombe']}),
        OdjavaInline
    ]
    inlines = [KontaktInline, LastnistvoInline, OdjavaInline]
```
