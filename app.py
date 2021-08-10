import face_recognition as fr
import cv2
import numpy as np
import urllib
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

def url_to_image(url):
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def encode(url):
    img = url_to_image(url)

    face_locations = fr.face_locations(img)
    unknown_face_encodings = fr.face_encodings(img, face_locations)
    faces = {}
    for i in range(len(unknown_face_encodings)):
        val = 'face' + str(i)
        faces[val] = unknown_face_encodings[i].tolist()

    return faces


class getEncodes(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("url")
        args = parser.parse_args()
        url = args["url"]
        try:
            encodes = encode(url)
        except:
            return "Face not found", 302
        if encodes != None:
            return encodes, 200
        return encodes, 300


api.add_resource(getEncodes, '/encode')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
