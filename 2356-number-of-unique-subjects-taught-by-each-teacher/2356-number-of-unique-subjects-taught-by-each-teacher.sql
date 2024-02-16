# Write your MySQL query statement below
Select teacher_id, count(Distinct subject_id) as cnt from Teacher group by teacher_id