from .models import employee
from app.serializers import employeeserializer


def employee_create(first_name,last_name,email,phone_number,date_of_birth,date_of_hire,position,department,salary,address):
    try:
        record =employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email = email,
            phone_number = phone_number,
            date_of_birth = date_of_birth,
            date_of_hire= date_of_hire,
            position = position,
            department = department,
            salary = salary,
            address = address
        )
        return 'DATA CREATED SUCCFULLY'

       
    except Exception as e:
        return str(e)
    
def employee_view(id=None):
    print('id',id)
    if id:
        record = employee.objects.get(id=id)
        records = employeeserializer(record)
        return records.data
    # else:
    #     record = employee.objects.all()
    #     records = employeeserializer(record,many=True)
    #     return records.data

def update_view(id, first_name,
                last_name, email,      
                phone_number,
                date_of_birth,
                date_of_hire,
                position,
                department,
                salary,
                address,
               ):
    try:

        record = employee.objects.get(id=id)
        if first_name : record.first_name = first_name
        if last_name : record.last_name = last_name
        if email : record.email = email
        if phone_number : 
            record.phone_number = phone_number
        if date_of_birth: record.date_of_birth = date_of_birth
        if date_of_hire : record.date_of_hire = date_of_hire
        if position : record.position = position
        if department: record.department = department
        if salary:
            record.salary = salary
        if address:
            record.address = address
        record.save()
        return {'status_code':1,'record':'updated successfully'}
    except employee.DoesNotExist:
        return {'status_code':0,'data':'Data not found'}

    
def delete_record(id=None):
    record = employee.objects.get(id=id)
    record.delete()
    print('Record deleted succfully')

  