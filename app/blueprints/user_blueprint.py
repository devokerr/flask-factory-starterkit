from flask import jsonify
from flask import current_app
from app.models.user_model import db, User


@current_app.route('/', methods=['GET'])
def create_user():
    # """Endpoint to create a user."""
    new_user = User(user_name='user1')
    db.session.add(new_user)
    db.session.commit()

    return jsonify(network=new_user.to_dict())
