
class ApiFilterMixin:
    def get_ordering_fields(self):
        ordering = self.request.query_params.get('order', None)
        allowed_fields = [field.lstrip('-') for field in getattr(self, 'allowed_order_field', [])]

        if ordering and ordering.lstrip('-') in allowed_fields:
            return (ordering,)

        return None


    def apply_ordering(self, queryset):
        ordering_fields = self.get_ordering_fields()
        if ordering_fields:
            return queryset.order_by(*ordering_fields)
        return queryset