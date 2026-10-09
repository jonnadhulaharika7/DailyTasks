create table icc_worldcup
(
Team_1 Varchar(20),
Team_2 Varchar(20),
Winner Varchar(20)
);
INSERT INTO icc_worldcup values('India','SL','India');
INSERT INTO icc_worldcup values('SL','Aus','Aus');
INSERT INTO icc_worldcup values('SA','Eng','Eng');
INSERT INTO icc_worldcup values('Eng','NZ','NZ');
INSERT INTO icc_worldcup values('Aus','India','India');

select * from icc_worldcup;

select team_name, count(1) as no_of_matches_played, sum(win_flag) as no_of_matches_won, count(1) - sum(win_flag) as no_of_losses
from(
select team_1 as team_name, case when team_1=winner then 1 else 0 end as win_flag
from icc_worldcup
union all
select team_2 as team_name, case when team_2=winner then 1 else 0 end as win_flag
from icc_worldcup)A
group by team_name
order by no_of_matches_won desc
