CREATE TABLE friend (
    person_id INT,
    friend_id INT,
    score INT
);

INSERT INTO friend (person_id, friend_id, score) VALUES
(1, 2, 80),
(1, 3, 90),
(2, 1, 70),
(2, 3, 85),
(3, 1, 95);

CREATE TABLE person (
    personid INT PRIMARY KEY,
    name VARCHAR(50)
);
INSERT INTO person (personid, name) VALUES
(1, 'Rahul'),
(2, 'Priya'),
(3, 'Kiran'),
(4, 'Sneha');

with score_details as (
select f.person_id,SUM(f.score) as total_friend_score,count(1) as no_of_friends from friend f
INNER JOIN person p ON f.friend_id = p.personid
group by f.person_id
having sum(f.score) > 100
)
select s.*,p.name as person_name
from person p
inner join score_details s on p.personid=s.person_id;