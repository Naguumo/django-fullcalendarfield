from django.forms import Field

from fullcalendarfield.widgets import CalendarWidget


class CalendarField(Field):
    widget = CalendarWidget
    hidden_widget = CalendarWidget