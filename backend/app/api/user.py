from flask import Blueprint, g
from flask_restful import Api, Resource, reqparse
from app.services import UserService
from app.utils import to_dict_msg, login_required

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_api = Api(user_bp)

class UserResource(Resource):
    def __init__(self):
        self.user_service = UserService()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, 
                                 help='用户名不能为空')
        self.reqparse.add_argument('password', type=str, required=True, 
                                 help='密码不能为空')
        self.reqparse.add_argument('email', type=str)
        self.reqparse.add_argument('phone', type=str)

    @login_required
    def get(self):
        """获取当前用户信息"""
        try:
            user = self.user_service.get_user_by_id(g.user_id)
            return to_dict_msg(data=user, message="获取用户信息成功")
        except Exception as e:
            return to_dict_msg(code=500, message=str(e))

    def post(self):
        """创建新用户"""
        args = self.reqparse.parse_args()
        try:
            user = self.user_service.create_user(
                username=args.username,
                password=args.password,
                email=args.email,
                phone=args.phone
            )
            return to_dict_msg(data=user, message="用户创建成功")
        except Exception as e:
            return to_dict_msg(code=500, message=str(e))

    @login_required
    def put(self):
        """更新用户信息"""
        args = self.reqparse.parse_args()
        try:
            user = self.user_service.update_user(
                user_id=g.user_id,
                username=args.username,
                password=args.password,
                email=args.email,
                phone=args.phone
            )
            return to_dict_msg(data=user, message="用户信息更新成功")
        except Exception as e:
            return to_dict_msg(code=500, message=str(e))

    @login_required
    def delete(self):
        """删除用户"""
        try:
            self.user_service.delete_user(g.user_id)
            return to_dict_msg(message="用户删除成功")
        except Exception as e:
            return to_dict_msg(code=500, message=str(e))

# 用户登录接口
class UserLoginResource(Resource):
    def __init__(self):
        self.user_service = UserService()
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, 
                                 help='用户名不能为空')
        self.reqparse.add_argument('password', type=str, required=True, 
                                 help='密码不能为空')

    def post(self):
        """用户登录"""
        args = self.reqparse.parse_args()
        try:
            token = self.user_service.login(
                username=args.username,
                password=args.password
            )
            return to_dict_msg(data={'token': token}, message="登录成功")
        except Exception as e:
            return to_dict_msg(code=401, message=str(e))

user_api.add_resource(UserResource, '/user')
user_api.add_resource(UserLoginResource, '/login')