from .models import Chart


def get_doctor_worktime(doctor_id: int) -> dict:
    """Get doctor worktime"""
    doctor_chart = Chart.objects.get(chart_doctor_id=doctor_id)
    

    return {
            'doctor_worktime_start': doctor_chart.chart_work_time_start,
            'doctor_worktime_end': doctor_chart.chart_work_time_end,
            }
    
    
    
