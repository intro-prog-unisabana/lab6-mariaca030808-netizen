#Función primera
def student_averages(data):
    my_dict = {}
    for estudiante, promedio in data.items():
        total= 0
        count= 0
        for nota in promedio.values():
            total += nota
            count += 1
        prom = round(total / count)
        my_dict[estudiante] =prom
    return my_dict
#Función segunda
def assignment_averages(prome):
    my_dict2 = {}
    assignments = prome[list(prome.keys())[0]].keys()
    for trabajo in assignments:
        total= 0
        count=0
        for student in prome:
            total += prome[student][trabajo]
            count += 1
        average = round(total / count)
        my_dict2[trabajo] =average
    return my_dict2