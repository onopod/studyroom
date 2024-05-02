rm -f api/migrations/0001_initial.py
/usr/bin/python3 manage.py makemigrations
/usr/bin/python3 manage.py migrate

echo -e "\nユーザーテーブル\n"
echo -e "\n新規登録\n"
echo -e "\n更新\n"
echo -e "\n削除\n"
echo -e "\n一覧\n"
echo -e "\n詳細\n"
echo -e "\n覧細\n"

