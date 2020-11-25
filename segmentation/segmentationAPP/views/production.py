import os
import sys
sys.dont_write_bytecode = True

from django.http import JsonResponse
import DeepLabv3FineTuning
import time
import requests
import ast
from segmentationAPP import common
import imageio
from PIL import Image
import io
import base64
import json
VOLUME = common.VOLUME
# Create your views here.
def Process(request):
    try:
        print('process Start')
        path_info = json.loads(request.body.decode())
        print(path_info)
        tmp_path = path_info["tmp_path"]
        origin_file_name = path_info["origin_file_name"]
        res = []
        # segmentation
        result_file_name = DeepLabv3FineTuning.predict.predict(tmp_path)

        if not os.path.exists(VOLUME):
                os.makedirs(VOLUME)
                # localhost: C://Users/admin/Desktop/docker/tmp/segmentation
                # staging: /home/ehost/volume/tmp/segmentation
                # production: /home/ehost/volume/tmp/segmentation
        tmp_name = uuid.uuid4().hex + origin_file_name
        tmp_path = os.path.join(VOLUME, tmp_name)
        im.save(tmp_path)
        
        result = {'response':{"error":0, 
                            "result_path":tmp_path}
                }
    except Exception as e:
        print(e)
        result = {'response':{"error":1}}
    return JsonResponse(result)
