SELECT date_of, student_name, group_number, subject, estimate
FROM estimates
JOIN students as s ON student_id = s.id
JOIN groups as g ON group_id = g.id
JOIN subjects as sub ON subject_id = sub.id
WHERE subject = "History" AND group_number = 3
ORDER BY student_name