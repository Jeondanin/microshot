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
# Create your views here.
def Process(request):
    print('process Start')
    result_file_name = DeepLabv3FineTuning.predict.predict("Doc_2271_1_Position(01)-Image Export-01.jpg")
    res_img = get_response_image(result_file_name)
    res = []
    res.append({"thumb": res_img,
        "srcset:": res_img,
        "src": res_img,
        "status":"ok"
        })
    if True:
        result = {'response':res}
    else:
        result = {"test":"ng"}
    return JsonResponse(result)

def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = base64.encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img
