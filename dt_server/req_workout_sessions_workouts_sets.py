'''
====================================================================================
API : /users/<user_id>/workout_sessions/<workout_session_id>/workouts/<workout_id>/sets
    Path params : 
        user_id : User 고유키
        workout_session_id : WorkoutSession 고유키
        workout_id : Workout 고유키
    Methods : 
        POST : 
            status code: 
                201 : OK    
====================================================================================
'''
import sys
sys.path.append('.')

from base_uri import BaseAPI
import requests
from datetime import datetime, timedelta

def create_workout_set(set, weight, total_reps, set_start_time, set_end_time, res_start_time, res_end_time) : 
    return {
        'set' : set, 
        'weight' : weight, 
        'total_reps' : total_reps, 
        'set_start_time' : set_start_time, 
        'set_end_time' : set_end_time, 
        'res_start_time' : res_start_time, 
        'res_end_time' : res_end_time
    }

def create_workout_metric(rep, peak_velocity_con, mean_velocity_con, peak_power_con, mean_power_con, 
                          peak_foce_con, mean_foce_con, peak_acceleration_con, mean_acceleration_con, 
                          peak_velocity_ecc, mean_velocity_ecc, peak_power_ecc, mean_power_ecc, peak_foce_ecc, mean_foce_ecc, 
                          peak_acceleration_ecc, mean_acceleration_ecc, rep_duration_con, rep_duration_ecc, top_stay_duration, 
                          bottom_stay_duration, rep_duration, RSI, RFD
                          ) : 
    return {
        'rep' : rep, 
        'peak_velocity_con' : peak_velocity_con, 
        'mean_velocity_con' : mean_velocity_con, 
        'peak_power_con' : peak_power_con,
        'mean_power_con' : mean_power_con, 
        'peak_foce_con' : peak_foce_con,
        'mean_foce_con' : mean_foce_con, 
        'peak_acceleration_con' : peak_acceleration_con,
        'mean_acceleration_con' : mean_acceleration_con, 
        'peak_velocity_ecc' : peak_velocity_ecc,
        'mean_velocity_ecc' : mean_velocity_ecc, 
        'peak_power_ecc' : peak_power_ecc,
        'mean_power_ecc' : mean_power_ecc, 
        'peak_foce_ecc' : peak_foce_ecc,
        'mean_foce_ecc' : mean_foce_ecc, 
        'peak_acceleration_ecc' : peak_acceleration_ecc,
        'mean_acceleration_ecc' : mean_acceleration_ecc, 
        'rep_duration_con' : rep_duration_con,
        'rep_duration_ecc' : rep_duration_ecc, 
        'top_stay_duration' : top_stay_duration,
        'bottom_stay_duration' : bottom_stay_duration, 
        'rep_duration' : rep_duration,
        'RSI' : RSI, 
        'RFD' : RFD,
    }

def create_dumydata() : 
    cur_datetime = datetime.now()
    set1_work_start_time = cur_datetime
    set1_work_end_time = set1_work_start_time + timedelta(minutes = 14)    

    set1_rest_start_time = set1_work_end_time
    set1_rest_end_time = set1_rest_start_time + timedelta(minutes = 1) 

    return {
        'workout_set' : create_workout_set(1, 70, 5, set1_work_start_time.isoformat(), set1_work_end_time.isoformat(), set1_rest_start_time.isoformat(), set1_rest_end_time.isoformat()),
        'workout_metrics' : [
            create_workout_metric(1, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
            create_workout_metric(2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
            create_workout_metric(3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
            create_workout_metric(4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
            create_workout_metric(5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
            create_workout_metric(1, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
            create_workout_metric(2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
            create_workout_metric(3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
            create_workout_metric(4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
            create_workout_metric(5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9)
        ]
    }

data = create_dumydata()
user_id = 1
workout_session_id = 1
workout_id = 1

def main() : 
    uri = f'/users/{user_id}/workout_sessions/{workout_session_id}/workouts/{workout_id}/sets' 
    api = BaseAPI(uri)

    api.post(data)

if __name__ == '__main__' : 
    main()