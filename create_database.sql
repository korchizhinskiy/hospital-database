CREATE DATABASE hospital;

CREATE TABLE department (
  department_id smallserial PRIMARY KEY,
  department_name varchar(50) NOT NULL,
  department_state_count smallint NOT NULL
);

CREATE TABLE specialization (
  specialization_id smallserial PRIMATY KEY,
  specialization_name varchar(50) NOT NULL,
  specialization_state_count smallint NOT NULL
);

CREATE TABLE day (
  day_id smallserial PRIMARY KEY,
  day_name varchar(12) NOT NULL
);

CREATE TABLE work_time (
  work_time_id smallserial PRIMARY KEY,
  work_time_start timestamp NOT NULL,
  work_time_end timestamp NOT NULL
);

CREATE TABLE chart (
  chart_id smallserial PRIMARY KEY,
  chart_day_id smallint FOREIGN KEY day(day_id),
  chart_work_time_id smallint FOREIGN KEY work_time(work_time_id)
)

CREATE TABLE doctor (
  doctor_id smallserial PRIMARY KEY,
  doctor_first_name varchar(30) NOT NULL,
  doctor_last_name varchar(30) NOT NULL,
  doctor_second_name varchar(30),
  doctor_age smallint NOT NULL,
  doctor_department_id smallint FOREIGN KEY department(department_id),
  doctor_specialization_id smallint FOREIGN KEY specialization(specialization_id),
  doctor_experience smallint NOT NULL
);

CREATE TABLE schedule (
  schedule_id smallserial PRIMARY KEY,
  schedule_doctor_id smallint FOREIGN KEY doctor(doctor_id),
  schedule_chart_id smallint FOREIGN KEY chart(chart_id)
);

CREATE TABLE recipe (
  recipe_id smallserial PRIMARY KEY,
  recipe_text text NOT NULL
);

CREATE TABLE desease (
  desease_id smallserial PRIMARY KEY,
  desease_name varchar(150) NOT NULL,
  desease_recipe smallint FOREIGN KEY recipe(recipe_id)
);

CREATE TABLE medical_history (
  medical_history_id smallserial PRIMARY KEY,
  medical_history_start date NOT NULL,
  medical_history_end date,
  medical_history_desease_id smallint FOREIGN KEY desease(desease_id)
);

CREATE TABLE patient (
  patient_id smallserial PRIMARY KEY,
  patient_first_name varchar(30) NOT NULL,
  patient_last_name varchar(30) NOT NULL,
  patient_second_name varchar(30),
  patient_age smallint NOT NULL,
  patient_medical_history smallint FOREIGN KEY medical_history(medical_history_id)
);

CREATE TABLE visit(
  visit_id smallserial PRIMARY KEY,
  visit_doctor_id smallint FOREIGN KEY doctor(doctor_id),
  visit_patient_id smallint FOREIGN KEY patient(parient_id),
  visit_datetime datetime NOT NULL
);



