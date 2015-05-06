from flask.ext import restful
from flask.ext.restful import marshal_with, reqparse
from route.base import api
from sqlalchemy import func, or_
from geoalchemy2.elements import WKTElement

from model.base import db
from model.station import Station
from model.poi import Poi, poi_marshaller

import json
import requests


class autocompleteAPI(restful.Resource):

    @marshal_with(poi_marshaller)
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('lng', type=float, required=True,
                            help='longitude is required')
        parser.add_argument('lat', type=float, required=True,
                            help='latitude is required')
        parser.add_argument('query', required=True,
                            help='query is required')
        args = parser.parse_args()

        point = WKTElement('POINT({0} {1})'.format(args['lng'], args['lat']),
                           srid=4326)

        looking_for = '%{0}%'.format(args['query'])
        stations = db.session.query(Station).filter(
            or_(Station.name.ilike(looking_for),
                Station.address.ilike(looking_for))
        ).order_by(func.ST_Distance(Station.position, point)).all()

        payload = {'q': args['query'], 'lat': args['lat'], 'lon': args['lng']}
        r = requests.get('http://photon.komoot.de/api/', params=payload)

        poiList = []

        for st in stations:
            poiList.append(Poi(st.name, st.address, st.position))

        responsejson = r.json()
        for feature in responsejson['features']:
            print feature
            address = ''
            if 'street' in feature['properties']:
                address = feature['properties']['street']
            if 'city' in feature['properties']:
                address = address + ' - %s' % feature['properties']['city']
            if 'state' in feature['properties']:
                address = address + ' - %s' % feature['properties']['state']
            if 'country' in feature['properties']:
                address = address + ' - %s' % feature['properties']['country']

            lon = feature['geometry']['coordinates'][0]
            lat = feature['geometry']['coordinates'][1]
            pos = WKTElement('POINT({0} {1})'.format(lon, lat), srid=4326)
            poiList.append(Poi(feature['properties']['name'], address, pos))


        return poiList

api.add_resource(autocompleteAPI, "/ac")
