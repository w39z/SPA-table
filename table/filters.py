import django_filters
from django import forms
from django_filters import ChoiceFilter, CharFilter, OrderingFilter, LookupChoiceFilter

from table.models import Item


class ItemFilter(django_filters.FilterSet):

    # column = ChoiceFilter(
    #     choice=(
    #         ('date', 'Дата'),
    #         ('name', 'Наименование'),
    #         ('amount', 'Количество'),
    #         ('distance', 'Расстояние'),
    #     ),
    # )

    order = OrderingFilter(
        fields=(
            ('name', 'Наименование'),
            ('amount', 'Количество'),
            ('distance', 'Расстояние'),
        ),
    )
    date = (django_filters.LookupChoiceFilter(
        lookup_choices=[
            ('exact', 'Равно'),
            ('icontains', 'Содержит'),
            ('gt', 'Больше чем'),
            ('lt', 'Меньше чем'),
        ]
    ))

    name = (django_filters.LookupChoiceFilter(
        lookup_choices=[
            ('exact', 'Равно'),
            ('icontains', 'Содержит'),
            ('gt', 'Больше чем'),
            ('lt', 'Меньше чем'),
        ]
    ))

    amount = (django_filters.LookupChoiceFilter(
        lookup_choices=[
            ('exact', 'Равно'),
            ('icontains', 'Содержит'),
            ('gt', 'Больше чем'),
            ('lt', 'Меньше чем'),
        ]
    ))

    distance = (django_filters.LookupChoiceFilter(
        lookup_choices=[
            ('exact', 'Равно'),
            ('icontains', 'Содержит'),
            ('gt', 'Больше чем'),
            ('lt', 'Меньше чем'),
        ]
    ))

    class Meta:
        model = Item
        fields = ['name', 'date', 'amount', 'distance']

        # exclude = '__all__'
            # ['name', 'date', 'amount', 'distance']