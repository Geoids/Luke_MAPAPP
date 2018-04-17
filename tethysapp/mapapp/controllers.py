from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from tethys_sdk.gizmos import DatePicker

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    # Date Picker Options
    date_picker = DatePicker(name='date1',
                             display_text='Date',
                             autoclose=True,
                             format='MM d, yyyy',
                             start_date='2/15/2014',
                             start_view='decade',
                             today_button=True,
                             initial='February 15, 2014')

    date_picker_error = DatePicker(name='data2',
                                   display_text='Date',
                                   initial='10/2/2013',
                                   disabled=True,
                                   error='Here is my error text.')



    context = {

        'date_picker': date_picker,
        'date_picker_error': date_picker_error,
    }

    return render(request, 'mapapp/home.html', context)\


@login_required()
def map(request):
    """
    Controller for the app home page.
    """


    context = {

    }

    return render(request, 'mapapp/map.html', context)

def data(request):
    """
    Controller for the app home page.
    """


    context = {

    }

    return render(request, 'mapapp/data.html', context)





def about(request):
    """
    Controller for the app home page.
    """


    context = {

    }

    return render(request, 'mapapp/about.html', context)
