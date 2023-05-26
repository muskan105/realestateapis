import django_filters
from .models import Ghar


class GharFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.ChoiceFilter(choices=[('0-100000', 'less than 100000'), ('100000-500000', '100000-500000'), ('500000-1000000', '500000-1000000'), ('1000000+', 'more than 1000000')])

    def filter_price(self, queryset, name, value):
        if '-' in value:
            start_price, end_price = value.split('-')
            start_price = self.parse_price(start_price)
            end_price = self.parse_price(end_price)
            return queryset.filter(price__gte=start_price, price__lte=end_price)
        elif '+' in value:
            start_price = self.parse_price(value.replace('+', ''))
            return queryset.filter(price__gte=start_price)
        else:
            price = self.parse_price(value)
            return queryset.filter(price=price)

    def parse_price(self, price_string):
        if 'Cr' in price_string:
            price = float(price_string.replace('Cr', '').strip()) * 10000000
        elif 'Lac' in price_string:
            price = float(price_string.replace('Lac', '').strip()) * 100000
        else:
            price = float(price_string)
        return price

    class Meta:
        model = Ghar
        fields = ['name', 'price']
        filter_overrides = {
            django_filters.ChoiceFilter: {
                'filter_class': django_filters.CharFilter,
                'method': 'filter_price',
            },
        }
