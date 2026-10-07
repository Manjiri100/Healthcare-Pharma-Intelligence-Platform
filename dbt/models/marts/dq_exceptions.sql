select patient_id,'DUPLICATE_PATIENT_ID' as exception_type from {{ ref('stg_patient') }} group by patient_id having count(*)>1
