"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    notas_arredondadas = []
    for indice in range(0,len(student_scores)):
        notas_arredondadas.append(round(student_scores[indice]))
    return notas_arredondadas


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    notas_arredondadas = round_scores(student_scores)
    contador = 0
    for indice in range(0,len(notas_arredondadas)):
        if notas_arredondadas[indice] <= 40:
            contador = contador + 1
    return contador
   



def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    acimaMedia = []
    notas_arredondadas = round_scores(student_scores)
    for indice in range(0,len(notas_arredondadas)):
        if notas_arredondadas[indice] >= threshold:
            acimaMedia.append(notas_arredondadas[indice])
    return acimaMedia


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    D_inferior = 41
    intervalo = int((highest - 40)/4)
    C_inferior = D_inferior + intervalo 
    B_inferior = D_inferior + 2*intervalo 
    A_inferior = D_inferior + 3*intervalo

    limites_inferiores = []
    #limites_inferiores_arredondados = []

    limites_inferiores.append(D_inferior)
    limites_inferiores.append(C_inferior)
    limites_inferiores.append(B_inferior)
    limites_inferiores.append(A_inferior)
    
    '''
    for indice in range(0,len(limites_inferiores)):
        limites_inferiores_arredondados.append(int(limites_inferiores[indice]))
    '''

    return limites_inferiores


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    notas_arredondadas = []
    for i in range(0,len(student_scores)):
        notas_arredondadas.append(student_scores[i])
    estudantes_notas = []
    
    for indice1 in range(0,len(notas_arredondadas)):
        #for indice2 in range(0,len(student_names)):
        estudantes_notas.append(str(indice1 + 1)+'.'+' '+student_names[indice1]+':'+' '+str(notas_arredondadas[indice1]))
    return estudantes_notas


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for linha in student_info:
        if linha[1] == 100:
            return linha 
    return []
