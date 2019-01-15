import numpy as np
from math import *
import os.path
import os
import sys
import time
import copy
import json

import numpy as np
import struct


from keras.models import Sequential, model_from_json, load_model

model = load_model("/beegfs/desy/user/amalara/output_varariables/Sequential/model_AK8_pt_300_500/model_crosscheck/mymodel.h5")

f = open("/beegfs/desy/user/amalara/output_varariables/Sequential/model_AK8_pt_300_500/model_crosscheck/mymodel.model", 'rb')



filename = "test_export.model"
