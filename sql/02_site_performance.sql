SELECT s.site_id,s.site_name,s.trial_id,s.planned_patients,s.active_patients,
       COUNT(v.visit_id) AS visits,
       SUM(CASE WHEN v.status='Completed' THEN 1 ELSE 0 END) AS completed_visits
FROM sites s
LEFT JOIN visits v ON v.site_id=s.site_id
GROUP BY s.site_id,s.site_name,s.trial_id,s.planned_patients,s.active_patients
ORDER BY completed_visits DESC;
