Caffe with GuidedNet
============================

This the relase of the CVPR 2017 BNMW workshop version of GuidedNet, "Guided Optical Flow Learning". You can refer to paper for more details at [Openreview](https://openreview.net/forum?id=S1kggAGgb&noteId=S1kggAGgb) or [Arxiv](https://arxiv.org/abs/1702.02295).

The code base is heavily borrowed from [DispNet](https://lmb.informatik.uni-freiburg.de/resources/software.php) and [UnsupFlownet](http://scs.ryerson.ca/~jjyu/). Thanks for open sourcing the code.

Dependencies
=========

OpenCV 3 (Installation can be refered [here](https://github.com/BVLC/caffe/wiki/OpenCV-3.2-Installation-Guide-on-Ubuntu-16.04))

Tested on Ubuntu 16.04 with Titan X GPU, CUDNN 5.1

Compiling
=========

To get started with GuidedNet, first compile caffe, by configuring a

    "Makefile.config" 

then make with 

    $ make -j 6 all

Training
========

(this assumes you compiled the code sucessfully) 

First you need to download and prepare the training data. For that go to the data folder: 

    cd data 

Then run: 

    ./download.sh 

Then prepare FlyingChairs_release.list file, change the directory accordingly. For example, if you want to train with FlowFields proxy ground truth, you need to first generate FlowFields flow estimation by yourself and change:

    FlyingChairs_release/data/00001_img1.ppm  FlyingChairs_release/data/00001_img2.ppm  FlyingChairs_release/data/00001_flow.flo 
to:

    FlyingChairs_release/data/00001_img1.ppm  FlyingChairs_release/data/00001_img2.ppm  FlyingChairs_release/FlowFields/00001_flow.flo 

Then run:

    ./make-lmdbs.sh 

(this will take some time and disk space) 

To train a GuidedNet network, go to this folder:
 
    cd ./GuidedNet/models/FlowNetS_FlowFields/

Then just run: 

    ./train.py 

To train GuidedNet network with unsuervised fine-tuning, go to this folder:
    
    cd ./GuidedNet/models/Unsup_FineTune/

Then just run: 

    ./train.py 

NOTE: You may get better performance if you carefully tune the hyper-params for different datasets, such as loss weights, learning rate etc. 

Testing
========

(this assumes you compiled the code sucessfully) 

E.g. go to this folder:

    cd ./GuidedNet/models/FlowNetS_FlowFields/

First, download pre-trained models:

[FlowNetS trained with FlowFields proxy ground truth for Flying Chairs dataset](https://drive.google.com/open?id=0B-bJpXHBmFWDc1JzQVBfbDdBM2c) 

[FlowNetS trained with FlowFields and unsupervised fine-tuning for Flying Chairs dataset](https://drive.google.com/open?id=0B-bJpXHBmFWDbG5ab2ZvbHhVekk) 

[FlowNetS trained with FlowFields and unsupervised fine-tuning for MPI-Sintel dataset](https://drive.google.com/open?id=0B-bJpXHBmFWDQk50OElxZzJLb1k)

Then prepare image pairs list, as in the example of ``fc_val_im0.txt`` and ``fc_val_im1.txt``.

Change line 157 in run.py to use the correct model. To try out GuidedNet on sample image pairs, run

    ./run.py fc_val_im0.txt fc_val_im1.txt 

This is just an example of testing on Flying Chairs dataset. You can generate your own image pairs list for any dataset.


License and Citation
====================

Please cite this paper in your publications if you use GuidedNet for your research:

    @article{guided_flow_17,
      title={{Guided Optical Flow Learning}},
      author={Yi Zhu and Zhenzhong Lan and Shawn Newsam and Alexander G. Hauptmann},
      journal={arXiv preprint arXiv:1702.022952},
      year={2017}
    }
