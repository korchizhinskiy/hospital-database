from django.db import models
from django.urls import reverse


class Department(models.Model):
    """Department Model"""
    department_id = models.SmallAutoField(primary_key=True)
    department_name = models.CharField(verbose_name='Название', max_length=50)

    def __str__(self):
        return f"{self.department_name.capitalize()}"

    class Meta:
        db_table = 'department'
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'


class Specialization(models.Model):
    """Specialization Model"""
    specialization_id = models.SmallAutoField(primary_key=True)
    specialization_name = models.CharField(verbose_name='Название',
                                           max_length=50)

    def __str__(self):
        return f"{self.specialization_name.capitalize()}"

    class Meta:
        db_table = 'specialization'
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class Day(models.Model):
    """Day of week Model"""
    day_id = models.SmallAutoField(primary_key=True)
    day_name = models.CharField(verbose_name='День недели', max_length=12)

    def __str__(self):
        return f"{self.day_name}"

    class Meta:
        db_table = 'day'
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class Chart(models.Model):
    """Chart Model"""
    chart_id = models.SmallAutoField(primary_key=True)
    chart_doctor_id = models.ForeignKey('Doctor', on_delete=models.CASCADE,
                                        verbose_name='Врач')
    chart_day_id = models.ForeignKey('Day', on_delete=models.CASCADE,
                                     verbose_name='День недели')
    chart_work_time_start = models.TimeField(verbose_name='Время начала работы')
    chart_work_time_end = models.TimeField(verbose_name='Время окончания работы')

    def __str__(self):
        return f"{self.chart_doctor_id.doctor_first_name}" \
               f" {self.chart_doctor_id.doctor_last_name}" \
               f" {self.chart_day_id.day_name}: {self.chart_work_time_start}" \
               f" - {self.chart_work_time_end}"

    class Meta:
        db_table = 'chart'
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'


class Doctor(models.Model):
    """Doctor Model"""
    doctor_id = models.SmallAutoField(primary_key=True)
    doctor_first_name = models.CharField(verbose_name='Имя', max_length=30)
    doctor_last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    doctor_second_name = models.CharField(verbose_name='Отчество', max_length=30,
                                          blank=True, null=True)
    doctor_age = models.SmallIntegerField(verbose_name='Возраст')
    doctor_department_id = models.ForeignKey('Department', on_delete=models.PROTECT,
                                             verbose_name='Отделение')
    doctor_specialization_id = models.ForeignKey('Specialization',
                                                 on_delete=models.PROTECT,
                                                 verbose_name='Специализация')
    doctor_experience = models.SmallIntegerField(verbose_name='Опыт работы')

    def __str__(self):
        return f"Врач-{self.doctor_specialization_id.specialization_name.lower()}" \
               f" {self.doctor_first_name.capitalize()} {self.doctor_last_name.capitalize()}"

    def get_absolute_url(self):
        return reverse('doctor', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'doctor'
        unique_together = ['doctor_first_name', 'doctor_last_name', 'doctor_second_name']
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Desease(models.Model):
    """Desease Model"""
    desease_id = models.SmallAutoField(primary_key=True)
    desease_name = models.CharField(max_length=150, verbose_name='Болезнь')
    recipe_text = models.TextField(verbose_name='Текст рецепта',
                                   null=True, blank=True)

    def __str__(self):
        return f"{self.desease_name}"

    class Meta:
        db_table = 'desease'
        verbose_name = 'Болезнь'
        verbose_name_plural = 'Болезни'


class MedicalHistory(models.Model):
    """Medical History Model"""
    medical_history_id = models.AutoField(primary_key=True)
    medical_patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE,
                                           verbose_name='Пациент')
    medical_history_start = models.DateField(verbose_name='Дата заболевания')
    medical_history_end = models.DateField(verbose_name='Дата выздоровления',
                                           blank=True, null=True)
    medical_history_desease_id = models.ForeignKey('Desease',
                                                   on_delete=models.CASCADE,
                                                   verbose_name='Болезнь')

    def __str__(self):
        return f"{self.medical_patient_id.patient_first_name}" \
               f" {self.medical_patient_id.patient_last_name}" \
               f" {self.medical_history_start} -" \
               f" {self.medical_history_end if self.medical_history_end else 'н.в.'}"

    class Meta:
        db_table = 'medical_history'
        verbose_name = 'История болезней'
        verbose_name_plural = 'Истории болезней'


class Patient(models.Model):
    """Patient Model"""
    patient_id = models.SmallAutoField(primary_key=True)
    patient_first_name = models.CharField(verbose_name='Имя', max_length=30)
    patient_last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    patient_second_name = models.CharField(verbose_name='Отчество', max_length=30,
                                           blank=True, null=True)
    patient_age = models.SmallIntegerField(verbose_name='Возраст')

    def __str__(self):
        return f"Пациент {self.patient_first_name} {self.patient_last_name}"

    def get_absolute_url(self):
        return reverse('patient', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'patient'
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        unique_together = [
                           'patient_first_name',
                           'patient_last_name',
                           'patient_second_name'
                           ]


class Visit(models.Model):
    """Visit Model"""
    visit_id = models.SmallAutoField(primary_key=True)
    visit_doctor_id = models.ForeignKey('Doctor', on_delete=models.CASCADE,
                                        verbose_name='Врач')
    visit_patient_id = models.ForeignKey('Patient', on_delete=models.CASCADE,
                                         verbose_name='Пациент')
    visit_datetime = models.DateTimeField()

    def __str__(self):
        return f"Посещение {self.visit_doctor_id.doctor_last_name} -" \
               f" {self.visit_patient_id.patient_last_name} |" \
               f" {self.visit_datetime}"

    class Meta:
        db_table = 'visit'
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
