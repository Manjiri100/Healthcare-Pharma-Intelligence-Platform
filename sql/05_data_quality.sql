SELECT patient_id,COUNT(*) AS record_count FROM patients GROUP BY patient_id HAVING COUNT(*)>1;
SELECT p.patient_id,p.trial_id FROM patients p LEFT JOIN clinical_trials t ON p.trial_id=t.trial_id WHERE t.trial_id IS NULL;
SELECT p.patient_id,p.site_id FROM patients p LEFT JOIN sites s ON p.site_id=s.site_id WHERE s.site_id IS NULL;
