select trial_id,trial_name,phase,therapeutic_area,cast(start_date as date) start_date,cast(target_end_date as date) target_end_date,status from {{ source('healthcare','clinical_trials') }}
