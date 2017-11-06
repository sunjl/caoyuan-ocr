```
curl -v -X POST 'http://localhost:5000/storage/upload' \
  -F "file=@data/train/train_template.png"

curl -v -G 'http://localhost:5000/storage/59f6b2ebb2c79a6c3a969331/train_template.png' \
  > ~/download/output.png

curl -v 'http://localhost:5000/storage/delete' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "59f6b2ebb2c79a6c3a969331"
    }'
```