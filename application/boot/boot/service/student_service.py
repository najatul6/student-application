from pweb import url_for
from boot.form.student_form import StudentCreateForm, StudentUpdateForm, StudentDetailsForm
from boot.model.student import Student
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD


class StudentService:
    form_data_crud = FormDataCRUD(model=Student)

    def create(self):
        params = {"button": "Create", "action": url_for("student_controller.create")}
        form = StudentCreateForm()
        return self.form_data_crud.create(view_name="student/form", form=form, redirect_url=url_for("student_controller.list"), params=params)

    def update(self, model_id: int):
        params = {"button": "Update", "action": url_for("student_controller.update", id=model_id)}
        form = StudentUpdateForm()
        return self.form_data_crud.update(view_name="student/form", model_id=model_id, update_form=form, redirect_url=url_for("student_controller.list"), params=params)

    def details(self, model_id: int):
        form = StudentDetailsForm()
        return self.form_data_crud.details("student/details", model_id=model_id, redirect_url=url_for("student_controller.list"), display_from=form)

    def delete(self, model_id: int):
        return self.form_data_crud.delete(model_id=model_id, redirect_url=url_for("student_controller.list"))

    def list(self):
        search_fields = ["name", "email","roll","semester"]
        return self.form_data_crud.paginated_list(view_name="student/list", search_fields=search_fields)