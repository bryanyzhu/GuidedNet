#!/usr/bin/env python
import os, sys
import subprocess

caffe_bin = '../../../build/tools/caffe'

os.system('mkdir training_ff') 
os.chdir('training_ff') 

# =========================================================

my_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(my_dir)

if not os.path.isfile(caffe_bin):
    print('Caffe tool binaries not found. Did you compile caffe with tools (make all tools)?')
    sys.exit(1)

print('args:', sys.argv[1:])

args = [caffe_bin, 'train', '-model', '../model/train.prototxt', '-solver', '../model/solver.prototxt'] + sys.argv[1:]
cmd = str.join(' ', args)
print('Executing %s' % cmd)

subprocess.call(args)
