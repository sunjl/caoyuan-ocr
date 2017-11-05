Optical Character Recognition using Deep Learning technologies

Development environment (see [Instructions](https://github.com/sunjl/development-environment))

* Ubuntu 16.04 64bit
* Python 3.5
* CUDA 8.0
* CUDNN 6.0
* OpenCV 3.3
* Tensorflow 1.3
* Keras 2.0
* MongoDB 3.5


Install dependencies:

```sh
git clone https://github.com/sunjl/caoyuan-ocr.git
cd caoyuan-ocr
sudo pip3 install -r requirements.txt
```

Execute tasks:

```sh
python3 ocr.py train
python3 ocr.py gen_test_data
python3 ocr.py evaluate
```

Start server:
```sh
FLASK_APP=app.py flask run
```

Todo:
* Algorithms:
  * Object Detection: Faster-RCNN, R-FCN, SSD, CTPN
  * Semantic Segmentation: FCN
  * Text Recognition: LSTM, CTC, Attention
* Support card/license/identification/receipt/table
