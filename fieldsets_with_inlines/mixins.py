from django import forms


class FieldsetsInlineMixin(object):
    change_form_template = 'fieldsets_with_inlines/change_form.html'

    def make_placeholder(self, index, fieldset):
        if isinstance(fieldset, forms.MediaDefiningClass):
            fieldset.fieldset_index = index

            # Placeholder must conform to the rules in
            # the ModelAdmin.fieldsets.
            # https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
            return (None, {'fields': ()})
        return fieldset

    def get_fieldsets(self, request, obj=None):
        if self.fieldsets_with_inlines:
            return [
                self.make_placeholder(index, fieldset)
                for index, fieldset in enumerate(self.fieldsets_with_inlines)]
        return super().get_fieldsets(request, obj)
