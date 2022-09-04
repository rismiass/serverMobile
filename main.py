from flask import Flask, request, jsonify, make_response
from data import db_session
from data.users import User
from data.courses import Course
from const import *
import base64


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ryasov_secret_key'
db_session.global_init("db/datebase.db")
db_sess = db_session.create_session()


@app.route('/sign-up', methods=['POST'])
def main():
    if request.method == 'POST':
        if not request.json:
            return make_response(jsonify({'status': 'Empty request'}), 400)
        elif not all(key in request.json for key in
                     ['email', 'password', 'name', 'surname', 'phone']):
            return make_response(jsonify({'status': 'Bad request'}), 400)
        else:
            email, password = request.json['email'], request.json['password']
            name, surname = request.json['name'], request.json['surname']
            phone = request.json['phone']
            db_sess = db_session.create_session()
            if db_sess.query(User).filter(User.email == email).first():
                return make_response(jsonify({'status': 'User already exists'}), 409)
            user = User(
                name=name,
                surname=surname,
                email=email, phone=phone
            )
            user.set_password(password)
            db_sess.add(user)
            db_sess.commit()

            return make_response(jsonify({'status': 'register successful', 'token': encoded_information({"user_id": user.id}, password)}), 201)


@app.route('/sign-in', methods=['POST'])
def main2():
    if request.method == 'POST':
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == request.json['email']).first()
        if not user:
            return make_response(jsonify({"token": " "}))
        if user and user.check_password(request.json['password']):
            return make_response(jsonify({'token': encoded_information({"user_id": user.id}, request.json['password'])}), 201)
        else:
            return make_response(jsonify({"token": " "}))


@app.route('/get-profile', methods=['GET'])
def profile():
    return jsonify({"id": 1, "name": "Константин ", "surname": "Сапрыкин",
                    "patronymic": "Дмитриевич",
                    "email": "saprikostya@gmail.com", "phone": "+79818590069",
                    "aboutSelf": "Обо мне нет никакой информации",
                    "historyWork": "1. ООО “Канцсвет” - 2 месяца;\n 2. ООО “Бухгалодон” - 3 месяца;", "photo": 88})


@app.route('/ads', methods=['GET'])
def ads():
    lst = [{"id": 1, "profession": "Официант", "salary": "250 рублей/час",
            "working_days": "Пятница, Воскресенье", "image": 2131165370},
           {"id": 2, "profession": "Администратор", "salary": "350 рублей/час",
            "working_days": "Вторник, Четверг", "image": 2131165275},
           {"id": 3, "profession": "Няня", "salary": "200 рублей/час",
            "working_days": "Понедельник, Среда", "image": 2131165358},
           {"id": 4, "profession": "Промоутер", "salary": "150 рублей/час",
            "working_days": "Среда, Суббота", "image": 2131165359}]
    return jsonify(lst)


@app.route('/chats', methods=['GET'])
def chats():
    lst = [{"id": 1, "sender": "Mcdonalds", "lastMessage": "Здравствуйте! Приглашаем вас...", "image": 2131165322},
           {"id": 2, "sender": "МТС", "lastMessage": "Здравствуйте! Приглашаем вас...", "image": 2131165334},
           {"id": 3, "sender": "Детский мир", "lastMessage": "Здравствуйте! Приглашаем вас...", "image": 2131165371}]
    return jsonify(lst)


@app.route('/courses', methods=['GET'])
def chourses():
    @app.route('/api/all_problems', methods=['GET'])
    def all_courses():
        if request.method == 'GET':
            db_sess = db_session.create_session()
            list_courses = []
            for i in db_sess.query(Course).all()[:15]:
                dictionary = {'id': i.id, 'title': i.title, 'photo': str(base64.b64encode(i.photo))[1:-1]}
                list_courses.append(dictionary)
            return make_response(jsonify({'courses': list_courses, 'status': 'OK'}), 201)
    #lst = [{"id": 1, "title": "Профильная математика", "price": "10 000 рублей", "image": 2131165323},
    #       {"id": 2, "title": "Русский язык", "price": "350 рублей/час", "image": 2131165361},
    #       {"id": 3, "title": "Английский язык", "price": "500 рублей/час", "image": 2131165295},
    #       {"id": 4, "title": "Дизайн", "price": "2000 рублей/часс", "image": 2131165289}]
    #return jsonify(lst)




if __name__ == '__main__':
    app.run()
