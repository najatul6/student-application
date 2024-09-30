from boot.service.student_service import StudentService
from pweb import Blueprint

student_url_prefix = "/student"
student_controller = Blueprint(
    "student_controller",
    __name__,
    url_prefix=student_url_prefix
)
student_service = StudentService()


@student_controller.route("/create", methods=['POST', 'GET'])
def create():
    return student_service.create()


@student_controller.route("/details/<int:id>", methods=['GET'])
def details(id: int):
    return student_service.details(id)


@student_controller.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id: int = None):
    return student_service.update(id)


@student_controller.route("/delete/<int:id>", methods=['GET'])
def delete(id: int):
    return student_service.delete(id)


@student_controller.route("/", methods=['GET'])
@student_controller.route("/list", methods=['GET'])
def list():
    return student_service.list()