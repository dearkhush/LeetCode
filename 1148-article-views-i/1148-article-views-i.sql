# Write your MySQL query statement below
#select distinct v.viewer_id id from Views v join Views w on w.author_id = v.viewer_id order by v.viewer_id ; 
select distinct author_id as id from views where author_id = viewer_id order by id;