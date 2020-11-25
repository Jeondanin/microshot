import os
import sys
sys.dont_write_bytecode = True

from django.http import JsonResponse
import DeepLabv3FineTuning
import time
import requests
import ast

import imageio
from PIL import Image
import io
import base64
import json

# Create your views here.
def Process(request):
    try:
        print('process Start')
        path_info = json.loads(request.body.decode())
        
        # segmentation
        result_file_name = DeepLabv3FineTuning.predict.predict(path_info)

        result = {'response':{"error":0, 
                            "result_path":result_file_name}
                }
    except Exception as e:
        print(e)
        result = {'response':{"error":1}}
    return JsonResponse(result)
