import face_recognition as fr
import cv2
import numpy as np
import urllib
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)



def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
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
        #add params
        parser.add_argument("url")
        #parse params
        args = parser.parse_args()
        #get params
        url = args["url"]
        try:
            encodes = encode(url)
        except:
            return "Face not found", 302

        if encodes != None:
            return encodes, 200

        return encodes, 300


api.add_resource(getEncodes, '/encodes/get')
app.run(port=5005)
"""
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
"""