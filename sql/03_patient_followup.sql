SELECT p.patient_id,p.patient_name,p.trial_id,
       COUNT(v.visit_id) AS total_visits,
       SUM(CASE WHEN v.status='Pending' THEN 1 ELSE 0 END) AS pending_visits
FROM patients p
LEFT JOIN visits v ON v.patient_id=p.patient_id
GROUP BY p.patient_id,p.patient_name,p.trial_id
HAVING SUM(CASE WHEN v.status='Pending' THEN 1 ELSE 0 END)>0
ORDER BY pending_visits DESC;
