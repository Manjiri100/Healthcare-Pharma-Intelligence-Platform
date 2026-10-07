select v.*,p.patient_name,p.age,p.status as patient_status from {{ ref('stg_visit') }} v left join {{ ref('stg_patient') }} p on v.patient_id=p.patient_id
