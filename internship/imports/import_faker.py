from faker import Faker
from ..models import Student, Internship_Assignment,Internship

def import_faker():
    faker = Faker()

    for i in range(2, 10):
        student_id=str(i-1)
        unh_id=str(i-1)
        last_name=faker.last_name()
        first_name=faker.first_name()
        major=faker.last_name()
        school_email=faker.email()
        degree=faker.last_name()
        linkedin=faker.url()

        student_instance = Student(
            student_id=student_id,
            unh_id=unh_id,last_name=last_name,first_name=first_name,
            school_email=  school_email, major = major,
            degree=  degree, linkedin = linkedin
        )
        student_instance.save()

        internship_id=str(i-1)
        position=faker.job()
        pay=faker.random_int(10,50)
        organization_name=faker.company()
        organization_url=faker.url()
        organization_address=faker.address()
        supervisor_name=faker.first_name()
        supervisor_position=faker.job()
        supervisor_email=faker.company_email()
        supervisor_phone=faker.phone_number()

        intern_instance = Internship(
            internship_id=internship_id,
            position=position,
            pay=pay,
            organization_name=organization_name,
            organization_url=organization_url,
            organization_address=organization_address,
            supervisor_name=supervisor_name,
            supervisor_position=supervisor_position,
            supervisor_email=supervisor_email,
            supervisor_phone=supervisor_phone
        )
        intern_instance.save()

        course_id=faker.last_name()
        student_credits=faker.random_int(1,3);
        semester=faker.month_name()
        year=faker.year()
        instructor=faker.first_name()
        start_date=faker.date()
        end_date=faker.date()

        internAssign_instance = Internship_Assignment(
            student_id = Student.objects.get(student_id = student_id),
            internship_id = Internship.objects.get(internship_id = internship_id),
            course_id=course_id,credits=student_credits,
            semester=semester,
            year=year,
            instructor=instructor,
            start_date=start_date,end_date=end_date
        )
        internAssign_instance.save()
