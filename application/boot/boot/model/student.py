from pweb_orm import PwebModel, pweb_orm


class Student(PwebModel):
    name = pweb_orm.Column("name", pweb_orm.String(150), nullable=False)
    roll = pweb_orm.Column("roll", pweb_orm.Integer(), nullable=False)
    registration = pweb_orm.Column("registration", pweb_orm.Integer(), nullable=False)
    technology = pweb_orm.Column("technology", pweb_orm.String(20), nullable=False)
    semester = pweb_orm.Column("semester", pweb_orm.String(150), nullable=False)
    collegeName = pweb_orm.Column("collegeName", pweb_orm.String(150), nullable=False)
    email = pweb_orm.Column("email", pweb_orm.String(150), nullable=False)
    password = pweb_orm.Column("password", pweb_orm.String(250), nullable=False)
    address = pweb_orm.Column("address", pweb_orm.Text())