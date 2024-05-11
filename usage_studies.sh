d=http://localhost:8000/api/
#d=https://onopod-1.paiza-user-basic.cloud:8000/api/
curl --get ${d}studies/in/ --data-urlencode id=ONO123 --data-urlencode name=ONO
curl --get ${d}studies/out/ --data-urlencode id=ONO123 --data-urlencode name=ONO
curl --get ${d}studies/in/ --data-urlencode id=ONO123 --data-urlencode name=ONO
curl --get ${d}studies/out/ --data-urlencode id=ONO123 --data-urlencode name=ONO
curl --get ${d}studies/in/ --data-urlencode id=ONO123 --data-urlencode name=ONO
curl --get ${d}studies/out/ --data-urlencode id=ONO123 --data-urlencode name=ONO
sqlite3 db.sqlite3 -echo "select * from api_user order by created_at desc limit 10"
sqlite3 db.sqlite3 -echo "select * from api_study order by user_id, start_at limit 10"
sqlite3 db.sqlite3 -echo "select * from api_command order by created_at desc limit 10"
