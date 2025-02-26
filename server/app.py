from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate


from models import db, Message


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
  if request.method == 'GET':
    messages = [message.to_dict() for message in Message.query.all()]
    return make_response(jsonify(messages), 200)
  
  elif request.method == 'POST':
     body = request.json.get('body')
     username = request.json.get('username')
     if not body or not username:
        return make_response({'error': 'Body and Username are required fields'}, 400)


     new_message = Message(
        
        body = body,
        username = username,
     )
     db.session.add(new_message)
     db.session.commit()
     return make_response(jsonify(new_message.to_dict()), 201)
 
  return make_response('error: Database error: ', 500)


@app.route('/messages/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def messages_by_id(id):
    print(f"Looking for message with id: {id}") 
    message = Message.query.filter_by(id=id).first()  # Using filter_by() is more concise
    if not message:
        return make_response({'error': 'Message not found'}, 404)

    if request.method == 'GET':
        # Return the message details directly as a dictionary
        content = {
            'message_body': message.body,
            'message_username': message.username
        }
        return make_response(jsonify(content), 200)

    elif request.method == 'PATCH':
        body = request.json.get('body') 
        username = request.json.get('username')

        # Ensure body or username is present if a PATCH request is made
        if not body and not username:
            return make_response({'error': 'At least one of body or username is required to update.'}, 400)

        # Update message if fields are provided
        if body:
            message.body = body
        if username:
            message.username = username
        
        db.session.commit()

        # Return the updated message
        return make_response(jsonify(message.to_dict()), 200)

    elif request.method == 'DELETE':
        db.session.delete(message)
        db.session.commit()
        return make_response({'message': 'Deleted successfully'}, 200)



# @app.route('/messages/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
# def messages_by_id(id):
#     print(f"Looking for message with id: {id}") 
#     message = Message.query.filter_by(id=id).first()  # Using filter_by() is more concise
#     if not message:
#         return make_response({'error': 'Message not found'}, 404)

#     if request.method == 'GET':
#         # Return the message details directly as a dictionary
#         content = {
#             'message_body': message.body,
#             'message_username': message.username
#         }
#         return make_response(jsonify(content), 200)

#     elif request.method == 'PATCH':
#         body = request.json.get('body') 
#         username = request.json.get('username')

#         # Ensure body or username is present if a PATCH request is made
#         if not body and not username:
#             return make_response({'error': 'At least one of body or username is required to update.'}, 400)

#         # Update message if fields are provided
#         if body:
#             message.body = body
#         if username:
#             message.username = username
        
#         db.session.commit()

#         # Return the updated message
#         return make_response(jsonify(message.to_dict()), 200)

#     elif request.method == 'DELETE':
#         db.session.delete(message)
#         db.session.commit()
#         return make_response({'message': 'Deleted successfully'}, 200)

if __name__ == '__main__':
    app.run(port=5555)








# from flask import Flask, request, make_response, jsonify
# from flask_cors import CORS
# from flask_migrate import Migrate


# from models import db, Message

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# CORS(app)
# migrate = Migrate(app, db)

# db.init_app(app)

# @app.route('/messages')
# def messages():
#     return ''

# @app.route('/messages/<int:id>')
# def messages_by_id(id):
#     return ''

# if __name__ == '__main__':
#     app.run(port=5555)
