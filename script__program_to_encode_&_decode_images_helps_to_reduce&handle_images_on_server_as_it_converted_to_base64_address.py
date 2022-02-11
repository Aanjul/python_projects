# For refrence https://github.com/Logan1x/Python-Scripts/blob/master/bin/image_encoder.py

import base64
import json
import time

def b64_encode(source_filepath):
with open(source_filepath, 'rb') as f:
		data = f.read()		
	dest = open('ImageData/encodeData.json', 'r')
	flag = json.loads(dest.read())
	
	key = (str(int(time.time()))).decode('utf-8')
	
	d = {"data": base64.b64encode(data).decode('utf-8'), "ext": source_filepath[source_filepath.index('.'):]}
	flag[key] = d
	dest.close()
	
	
	dest = open('ImageData/encodeData.json', 'w')
	json.dump(flag, dest)
	return key

def b64_decode(key, dest_path):
	source = open('ImageData/encodeData.json', 'r')
	flag = json.loads(source.read())
	name = key+str(flag[key]["ext"])
	dest = open(dest_path+name,'wb')
	dest.write(base64.b64decode((flag[key]["data"]).encode('utf-8')))
	dest.close()
	return dest_path+name