import subprocess
import h5py
import glob
import os


class RunCmd(object):
    def cmd_run(self, cmd):
        self.cmd = cmd
        subprocess.call(self.cmd, shell=True)

# Test the model 

for j in range(1):
      a = RunCmd()
      a.cmd_run('python MARSNet.py \
              --testfile=./GraphProt_CLIP_sequences/ALKBH5_Baltz2012.ls.positives.fa \
              --nega=./GraphProt_CLIP_sequences/ALKBH5_Baltz2012.ls.negatives.fa\
              --model_type=DRSN --predict=True')




