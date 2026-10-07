select patient_id,patient_name,age,sex,trial_id,site_id,cast(enrolment_date as date) enrolment_date,status from {{ source('healthcare','patients') }}
