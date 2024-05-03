# bash migrate.sh && bash usage_command.sh
d=http://localhost:8000/api/
j='Content-Type: application/json'
echo -e "\nユーザー新規登録"
curl -X POST ${d}users/ -d id=ONOPOD -d name=小野
echo -e "\nコマンド登録"
curl -X POST -H "${j}" ${d}commands/register/ -d '{"text": "ONOPOD !in"}'
curl -X POST -H "${j}" ${d}commands/register/ -d '{"text": "ONOPOD !out"}'
curl -X POST -H "${j}" ${d}commands/register/ -d '{"text": "ONOPOD !charge"}'
curl -X POST -H "${j}" ${d}commands/register/ -d '{"text": "ONOPOD !subject 簿記2級"}'
curl -X POST -H "${j}" ${d}commands/register/ -d '{"text": "ONOPOD !place A12"}'
curl -X POST -H "${j}" ${d}commands/register/ -d '{"text": "ONOPOD !comment 今日からがんばります！"}'

echo -e "\nコマンド実行"
curl ${d}commands/1/execute/
curl ${d}commands/2/execute/
curl ${d}commands/3/execute/
curl ${d}commands/4/execute/
curl ${d}commands/5/execute/
curl ${d}commands/6/execute/
