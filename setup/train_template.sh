FLASK_APP=app.py flask run

curl -v -X POST 'http://localhost:5000/storage/upload' \
  -F "file=@data/train/train_template.png"

python3 train_template.py

curl -v 'http://localhost:5000/template/create' \
  --request POST \
  --header "Content-Type: application/json" \
  --data-binary @train_template.json
