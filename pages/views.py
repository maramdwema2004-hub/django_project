
from django.shortcuts import render

def index(request):
    x = {
        'full_name': 'maram ',
        'student_id': '220221961',
        'address': 'Gaza, Palestine',
        'email': 'maramdwema2004@gmail.com',
        'major': 'Web Developer',
        # التاريخ ما زبطت معي و ما مرت علي في المحاضرات و ضلت تعمل ايرور ف سبتها 
    }

    return render(request, 'pages/index.html', x)
