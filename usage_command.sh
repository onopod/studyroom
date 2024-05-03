# bash migrate.sh && bash usage_command.sh
d=http://localhost:8000/api/
j='Content-Type: application/json'
echo -e "\nユーザー新規登録"
curl -X POST ${d}users/ -d id=ONOPOD -d name=小野
echo -e "\nコマンド登録"
curl -X POST -H "${j}" ${d}commands/register/ -d '{"text": "ONOPOD !in"}'
curl -X POST -H "${j}" ${d}commands/register/ -d '{"text": "ONOPOD !out"}'
echo -e "\nコマンド実行"
curl ${d}commands/1/execute/
curl ${d}commands/2/execute/
