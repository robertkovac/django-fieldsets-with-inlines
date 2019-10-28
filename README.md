# Fieldsets with inlines
### Mixin inlines and fieldsets in Django admin.


## Installation

    pip install django-fieldsets-with-inlines

## Quick start

1. Add "fieldsets_with_inlines" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'fieldsets_with_inlines',
    ]

1. Include FieldsetsInlineMixin in your admin.py

    from fieldsets_with_inlines import FieldsetsInlineMixin,

1. Add changes to your existing ModelAdmin classes in your admin.py::

    class TestAdmin(FieldsetsInlineMixin, admin.ModelAdmin)

* rename your fieldsets property to fieldsets_with_inlines

* insert inline where you want them

**With fieldsets-with-inlines inlines are not automaticaly rendered after your
fieldsets! Every inline that you want rendered should be added to your
fieldsets_with_inlines property.**


## Before and After

* Code before changes

    class TestAdmin(admin.ModelAdmin):
        fieldsets_with_inlines = [
            ('Objekt', {'fields': [
                ('ID_RNO', 'id', 'kljuc', 'slug'),
                'naziv',
                'kategorija']}),
            ('Naslov', {'fields': [
                ('obcina', 'obmocje'),
                ('naseljeulica', 'hisna_stevilka', 'hisna_stevilka_pripona'),
                ('ulica', 'kraj', 'posta')]}),
            ('Ponudnik', {
                'fields': [
                    'ponudnik',
                    ('ID_cadis', 'remote_id'),
                    'polovicna_taksa']}),
            ('Kontaktni podatki', {'fields': [
                ('kontaktna_oseba', 'email', 'poslji_obvestila')]}),
            ('Nastanitvena kapaciteta', {'fields': [
             ('stevilo_stalnih_lezisc',), ]}),
            ('Dostop', {'fields': [
                'users',
                ('cas_vpisa', 'zadnja_sprememba', 'cas_zadnje_posodobitve')]}),
            ('Opombe', {'fields': ['opombe']}),
        ]
        inlines = [KontaktInline, LastnistvoInline, OdjavaInline]


* Code after changes

    class TestAdmin(FieldsetsInlineMixin, admin.ModelAdmin):
        fieldsets_with_inlines = [
            ('Objekt', {'fields': [
                ('ID_RNO', 'id', 'kljuc', 'slug'),
                'naziv',
                'kategorija']}),
            ('Naslov', {'fields': [
                ('obcina', 'obmocje'),
                ('naseljeulica', 'hisna_stevilka', 'hisna_stevilka_pripona'),
                ('ulica', 'kraj', 'posta')]}),
            ('Ponudnik', {
                'fields': [
                    'ponudnik',
                    ('ID_cadis', 'remote_id'),
                    'polovicna_taksa']}),
            LastnistvoInline,
            ('Kontaktni podatki', {'fields': [
                ('kontaktna_oseba', 'email', 'poslji_obvestila')]}),
            KontaktInline,
            ('Nastanitvena kapaciteta', {'fields': [
             ('stevilo_stalnih_lezisc',), ]}),
            ('Dostop', {'fields': [
                'users',
                ('cas_vpisa', 'zadnja_sprememba', 'cas_zadnje_posodobitve')]}),
            ('Opombe', {'fields': ['opombe']}),
            OdjavaInline
        ]
        inlines = [KontaktInline, LastnistvoInline, OdjavaInline]
