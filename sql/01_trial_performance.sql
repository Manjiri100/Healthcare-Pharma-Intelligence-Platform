SELECT t.trial_id, t.trial_name, t.phase,
       COUNT(DISTINCT p.patient_id) AS enrolled_patients,
       COUNT(v.visit_id) AS scheduled_visits,
       SUM(CASE WHEN v.status='Completed' THEN 1 ELSE 0 END) AS completed_visits,
       ROUND(100.0*SUM(CASE WHEN v.status='Completed' THEN 1 ELSE 0 END)/NULLIF(COUNT(v.visit_id),0),1) AS visit_completion_pct
FROM clinical_trials t
LEFT JOIN patients p ON p.trial_id=t.trial_id
LEFT JOIN visits v ON v.trial_id=t.trial_id
GROUP BY t.trial_id,t.trial_name,t.phase
ORDER BY visit_completion_pct;
