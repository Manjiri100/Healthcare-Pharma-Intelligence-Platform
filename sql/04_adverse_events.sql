SELECT trial_id,severity,COUNT(*) AS event_count
FROM adverse_events
GROUP BY trial_id,severity
ORDER BY event_count DESC;
