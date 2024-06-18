from flask_restful import Resource
from flask import request
from models import Frontend, GeneralSetting


class FrontendApi(Resource):
    def post(self):
        # Get the JSON data from the request.
        data = request.get_json()
        # Check if the data is valid.
        if not data:
            return {'error': 'Invalid request'}, 400
        # data = data.get('data')
        data_keys = data['data_keys']
        singleQuery = False if 'singleQuery' not in data else data['singleQuery']
        limit = None if 'limit' not in data else data['limit']
        orderById = False if 'orderById' not in data else data['orderById']
        if singleQuery:
            content = Frontend.query.filter_by(data_keys=data_keys).order_by(Frontend.id.desc()).first().to_dict()
        else:
            article = Frontend.query.filter_by(data_keys=data_keys).order_by(Frontend.id.desc()).all()
            if orderById:
                article = Frontend.query.filter_by(data_keys=data_keys).all()
            content = [{'id': e.id, 'data_keys': e.data_keys, 'data_values': eval(e.data_values),
            'created_at': str(e.created_at), 'updated_at': str(e.updated_at)} for e in article]
            if limit:
                content = [content[cnt] for cnt in range(len(content)) if cnt < limit ]
        return content
        
    def get(self, id = None):
        if id is not None:
            content = GeneralSetting.query.get(id)
            if content: return {'id':content.id,'sitename': content.sitename, 'base_color': content.base_color, 'secondary_color': content.secondary_color}
            else: return {'message': 'Setting not found'}, 404
        else:
            content = GeneralSetting.query.get(1)
            if content: return {'id':content.id,'sitename': content.sitename, 'base_color': content.base_color, 'secondary_color': content.secondary_color}
            else: return {'message': 'Setting not found'}, 404
