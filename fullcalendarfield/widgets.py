from django.forms import TextInput


class CalendarWidget(TextInput):
    template_name = 'widgets/CalendarWidget.html'

    class Media:
        css = {
            'all': (
                'js/fullcalendar-4.2.0/packages/core/main.css',
                'js/fullcalendar-4.2.0/packages/bootstrap/main.css',
                'js/fullcalendar-4.2.0/packages/daygrid/main.css',
                'js/fullcalendar-4.2.0/packages/timegrid/main.css',
                'js/fullcalendar-4.2.0/packages/list/main.css'
            )
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js',
            'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js',
            'js/fullcalendar-4.2.0/packages/core/main.js',
            'js/fullcalendar-4.2.0/packages/bootstrap/main.js',
            'js/fullcalendar-4.2.0/packages/interaction/main.js',
            'js/fullcalendar-4.2.0/packages/daygrid/main.js',
            'js/fullcalendar-4.2.0/packages/timegrid/main.js',
            'js/fullcalendar-4.2.0/packages/list/main.js'
        )
