Optical Character Recognition using Deep Learning technologies

Development environment (see [Instructions](https://github.com/sunjl/development-environment))

* Ubuntu 16.04 64bit
* Python 3.5
* CUDA 8.0
* CUDNN 6.0
* OpenCV 3.3
* Tensorflow 1.3
* Keras 2.0


Install dependencies:

```sh
git clone https://github.com/sunjl/caoyuan-ocr.git
cd caoyuan-ocr
sudo pip3 install -r requirements.txt
```

Execute tasks:

```sh
cd keras
python3 ocr.py train
python3 ocr.py gen_test_data
python3 ocr.py evaluate
```

Start server:
```sh
cd web
FLASK_APP=app.py flask run
```

Todo:
* MongoDB CRUD, GridFS
* Flask HTTP JSON API
* Algorithms:
  * Object Detection: Faster-RCNN, R-FCN, SSD, CTPN
  * Semantic Segmentation: FCN
  * Text Recognition: LSTM, CTC, Attention
* Support card/license/identification/receipt/table

Bug:
* train task randomly failed with following error message:
```
Exception ignored in: <bound method BaseSession.__del__ of <tensorflow.python.client.session.Session object at 0x7fa5b2c84400>>
Traceback (most recent call last):
  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/client/session.py", line 701, in __del__
TypeError: 'NoneType' object is not callable
```
