select event_id,patient_id,trial_id,site_id,cast(event_date as date) event_date,event_type,severity,outcome from {{ source('healthcare','adverse_events') }}
