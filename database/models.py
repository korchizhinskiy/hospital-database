from django.db import models


class Doctor(models.Model): 
    """Doctor Model"""
    doctor_id = models.AutoField(primary_key=True)
    doctor_first_name = models.CharField(verbose_name='Имя', max_length=50)
    doctor_last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    doctor_second_name = models.CharField(verbose_name='Отчество', max_length=50,
                                          blank=True, null=True)
    doctor_age = models.IntegerField(verbose_name='Возраст')
    doctor_department_id = models.ForeignKey('Department', on_delete=models.PROTECT, verbose_name='Отделение')
    doctor_specialization_id = models.ForeignKey('Specialization', on_delete=models.PROTECT, verbose_name='Специализация')
    doctor_experience = models.IntegerField(verbose_name='Опыт работы')

    class Meta:
        db_table = 'doctor'
        unique_together = ['doctor_first_name', 'doctor_last_name', 'doctor_second_name']
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

class Department(models.Model):
    """Department Model"""
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(verbose_name='Название', max_length=100)
    department_state_count = models.IntegerField(verbose_name='Количество штата')

    class Meta:
        db_table = 'department'
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

class Specialization(models.Model):
    """Specialization Model"""
    specialization_id = models.AutoField(primary_key=True)
    specialization_name = models.CharField(verbose_name='Название', max_length=100)
    specialization_state_count = models.IntegerField(verbose_name='Количество штата')

    class Meta:
        db_table = 'specialization'
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

class Chart(models.Model):
    """Chart Model"""
    chart_id = models.AutoField(primary_key=True)
    chart_name = models.CharField(verbose_name='День недели', max_length=20)
    chart_work_time = models.ForeignKey('WorkTime', on_delete=models.PROTECT, 
                                        verbose_name='Время работы')

    class Meta:
        db_table = 'chart'
        verbose_name = 'День работы'
        verbose_name_plural = 'Дни работы'

class WorkTime(models.Model):
    """Work Time Model"""
    work_time_id = models.AutoField(primary_key=True)
    work_time_start = models.TimeField(verbose_name='Начало рабочего дня')
    work_time_end = models.TimeField(verbose_name='Конец рабочего дня', 
                                     default='22:00')

    class Meta:
        db_table = 'work_time'
        verbose_name = 'Время работы'
        verbose_name_plural = 'Время работы'

class Schedule(models.Model):
    """Schedule Model"""
    schedule_id = models.AutoField(primary_key=True)
    schedule_chart_id = models.ForeignKey('Chart', on_delete=models.CASCADE, 
                                          verbose_name='График работы')
    schedule_doctor_id = models.ForeignKey('Doctor', on_delete=models.CASCADE,
                                           verbose_name='Доктор')

    class Meta:
        db_table = 'schedule'
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'

class Patient(models.Model):
    """Patient Model"""
    patient_id = models.AutoField(primary_key=True)
    patient_first_name = models.CharField(verbose_name='Имя', max_length=50)
    patient_last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    patient_second_name = models.CharField(verbose_name='Отчество', max_length=50,
                                           blank=True, null=True)
    patient_age = models.IntegerField(verbose_name='Возраст')

    class Meta:
        db_table = 'patient'
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

class DoctorVisit(models.Model):
    """Doctor Visit Model"""
    doctor_visit_id = models.AutoField(primary_key=True)
    doctor_visit_patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE,
                                                verbose_name='Пациент')
    doctor_visit_doctor_id = models.ForeignKey('Doctor', on_delete=models.CASCADE,
                                               verbose_name='Врач')
    doctor_visit_datetime = models.DateTimeField(verbose_name='Время посещения')

    class Meta:
        db_table = 'doctor_visit'
        verbose_name = 'Запись к врачу'
        verbose_name_plural = 'Записи к врачу'

class MedicalHistory(models.Model):
    """Medical History Model"""
    medical_history_id = models.AutoField(primary_key=True)
    medical_history_patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE,
                                                   verbose_name='Пациент')
    medical_history_desease_name = models.CharField(verbose_name='Название болезни',
                                                    max_length=300)
    medical_history_desease_start = models.DateField(verbose_name='Дата заболевания')
    medical_history_desease_end = models.DateField(verbose_name='Дата выздоровления',
                                                   blank=True, null=True)
    medical_history_desease_recipe = models.ForeignKey('DeseaseRecipe',
                                                       null=True,
                                                       on_delete=models.SET_NULL, 
                                                       verbose_name='Рецепт')

    class Meta:
        db_table = 'medical_history'
        verbose_name = 'История болезней'
        verbose_name_plural = 'Истории болезней'

class DeseaseRecipe(models.Model):
    """Desease Recipe Model"""
    desease_recipe_id = models.AutoField(primary_key=True)
    desease_recipe_text = models.TextField(verbose_name='Рецепт')

    class Meta:
        db_table = 'desease_recipe'
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
