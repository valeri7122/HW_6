SELECT student_name, group_number
FROM students
JOIN groups ON groups.id = group_id
WHERE group_number = 2
ORDER BY student_name