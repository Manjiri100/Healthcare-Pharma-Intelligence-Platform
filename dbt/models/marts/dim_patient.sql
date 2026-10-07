select * from {{ ref('stg_patient') }} qualify row_number() over(partition by patient_id order by enrolment_date desc)=1
