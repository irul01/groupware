PWD=`pwd`
PROJECT_DIR="/home/ssung/Projects/Groupware"
cd $PROJECT_DIR

rm -rf $PROJECT_DIR/db.sqlite*
find . -type d | grep -v venv | grep "__pycache__" | xargs -I{} rm -rf {}
find . -type f | sed -n -r '/[0-9]{4}*.py$' | xargs -I{} rm -rf {}
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --username ssung --email ssungdev@gmail.com
cd $PWD
