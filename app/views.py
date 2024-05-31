
from django.shortcuts import render
from .microservices import employee_create,employee_view,update_view,delete_record
from .forms import employee_form
# Create your views here.

def create_employee(request):
    
    data = employee_form()
    if request.method == 'POST':
        data = employee_form(request.POST)
        if data.is_valid():
            first_name = data.cleaned_data['first_name']
            last_name = data.cleaned_data['last_name']
            email = data.cleaned_data['email']
            phone_number = data.cleaned_data['phone_number']
            date_of_birth = data.cleaned_data['date_of_birth']
            date_of_hire = data.cleaned_data['date_of_hire']
            position = data.cleaned_data['position']
            department = data.cleaned_data['department']
            salary = data.cleaned_data['salary']
            address = data.cleaned_data['address']
            data = employee_create(first_name,last_name,email,phone_number,date_of_birth,date_of_hire,position,department,salary,address)

    context = {
        'data':data
    }
    return render(request,'create.html',context)

def emp_view(request,id=None):
     records = employee_view(id=id)
     print('employee',records)
     return render(request,'view.html')


def update_data(request,id):

    get_data = update_view(id=id,first_name='chandru',last_name='p',
                           email='chandru@gmail.com',phone_number='9387438',
                           date_of_birth='2024-05-02',date_of_hire='2024-05-02',
                           position='okay',
                           department='any',
                           salary='343',
                           address='addressss'
                           )
    print('get_data',get_data)

    return render(request,'update.html')

def delete_view(request,id=None):
    delete_record(id=id)
    return render(request,'delete.html')

    







     


    


