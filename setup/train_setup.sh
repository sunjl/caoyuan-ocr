curl -v -X POST 'http://localhost:5000/storage/upload' \
  -F "file=@../data/train/train_template.png"

python3 train_template.py

curl -v 'http://localhost:5000/template/create' \
  --request POST \
  --header "Content-Type: application/json" \
  --data-binary @train_template.json

curl -v -X POST 'http://localhost:5000/storage/upload' \
  -F "file=@../data/train/train_image_01.png"

curl -v 'http://localhost:5000/image/create' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
      "user_id": "59f7e576b2c79a43548402e0",
      "kind": "train",
      "name": "train_image_01",
      "template_id": "5a0026f2b2c79a280e9c1946",
      "storage_id": "5a002aa1b2c79a280e9c1947",
      "filename": "train_image_01.png"
    }'

curl -v 'http://localhost:5000/image/init_regions' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "5a002ae8b2c79a280e9c1949"
    }'

curl -v 'http://localhost:5000/image/crop_regions' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "5a002ae8b2c79a280e9c1949"
    }'

curl -v 'http://localhost:5000/image/resize_regions' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "5a002ae8b2c79a280e9c1949"
    }'

curl -v 'http://localhost:5000/image/draw_regions' \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{
        "id": "5a002ae8b2c79a280e9c1949"
    }'