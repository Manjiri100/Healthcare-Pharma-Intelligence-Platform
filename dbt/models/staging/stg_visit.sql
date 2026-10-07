select visit_id,patient_id,trial_id,site_id,visit_type,cast(scheduled_date as date) scheduled_date,cast(completed_date as date) completed_date,status from {{ source('healthcare','visits') }}
