from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    usertype = SelectField('Выберите тип пользователя',
                           choices=[('Job Seeker', 'Соискатель работы'),
                                    ('Company', 'Компания')],
                           validators=[DataRequired()])
    username = StringField('Имя пользователя',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Электронная почта',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Это имя пользователя уже занято. Пожалуйста, выберите другое.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Этот адрес электронной почты уже используется. Пожалуйста, выберите другой.')


class LoginForm(FlaskForm):
    usertype = SelectField('Выберите тип пользователя',
                           choices=[('Job Seeker', 'Соискатель работы'),
                                    ('Company', 'Компания')],
                           validators=[DataRequired()])
    email = StringField('Электронная почта',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class ReviewForm(FlaskForm):
    username = StringField('Имя',
                           validators=[DataRequired()])
    review = TextAreaField('Отзыв',
                           validators=[DataRequired()])
    submit = SubmitField('Отправить отзыв')


class JobForm(FlaskForm):
    title = StringField('Название вакансии',
                        validators=[DataRequired(), Length(min=2, max=20)])
    industry = SelectField('Отрасль', choices=[('IT', 'ИТ'),
                                               ('Construction', 'Строительство'),
                                               ('Education', 'Образование'),
                                               ('Food And Beverage', 'Продукты питания и напитки'),
                                               ('Pharmaceutical', 'Фармацевтика'),
                                               ('Entertainment', 'Развлечения'),
                                               ('Manufacturing', 'Производство'),
                                               ('Telecommunication', 'Телекоммуникации'),
                                               ('Agriculture', 'Сельское хозяйство'),
                                               ('Transportation', 'Транспорт'),
                                               ('Computer And Technology', 'Компьютеры и технологии'),
                                               ('Healthcare', 'Здравоохранение'),
                                               ('Media And News', 'СМИ'),
                                               ('Hospitality', 'Гостиничный бизнес'),
                                               ('Energy', 'Энергетика'),
                                               ('Fashion', 'Мода'),
                                               ('Finance And Economic', 'Финансы и экономика'),
                                               ('Advertising And Marketing', 'Реклама и маркетинг'),
                                               ('Mining', 'Горная промышленность'),
                                               ('Aerospace', 'Авиакосмическая промышленность')],
                           validators=[DataRequired()])
    description = TextAreaField('Описание вакансии',
                                validators=[DataRequired()])
    submit = SubmitField('Отправить')


class ApplicationForm(FlaskForm):
    gender = SelectField('Пол', choices=[('Male', 'Мужской'),
                                         ('Female', 'Женский'),
                                         ('Others', 'Другой')],
                         default='Male',
                         validators=[DataRequired()])
    degree = SelectField('Уровень образования',
                         default='eSchool',
                         choices=[('eSchool', 'Школа'),
                                  ('dHighSchool', 'Высшая школа'),
                                  ('cBachelor', 'Бакалавр'),
                                  ('bMaster', 'Магистр'),
                                  ('aPHD', 'Доктор наук')],
                         validators=[DataRequired()])
    industry = SelectField('Отрасль',
                           default='Construction',
                           choices=[('IT', 'ИТ'),
                               ('Construction', 'Строительство'),
                                    ('Education', 'Образование'),
                                    ('Food And Beverage', 'Продукты питания и напитки'),
                                    ('Pharmaceutical', 'Фармацевтика'),
                                    ('Entertainment', 'Развлечения'),
                                    ('Manufacturing', 'Производство'),
                                    ('Telecommunication', 'Телекоммуникации'),
                                    ('Agriculture', 'Сельское хозяйство'),
                                    ('Transportation', 'Транспорт'),
                                    ('Computer And Technology', 'Компьютеры и технологии'),
                                    ('Healthcare', 'Здравоохранение'),
                                    ('Media And News', 'СМИ'),
                                    ('Hospitality', 'Гостиничный бизнес'),
                                    ('Energy', 'Энергетика'),
                                    ('Fashion', 'Мода'),
                                    ('Finance and Economic', 'Финансы и экономика'),
                                    ('Advertising And Marketing', 'Реклама и маркетинг'),
                                    ('Mining', 'Горная промышленность'),
                                    ('Aerospace', 'Авиакосмическая промышленность')],
                           validators=[DataRequired()])
    experience = IntegerField('Опыт работы в годах',
                              validators=[DataRequired()])
    cv = FileField('Обновить резюме', validators=[FileAllowed(['jpg', 'png', 'bmp'])])
    cover_letter = TextAreaField('Сопроводительное письмо',
                                 validators=[DataRequired()])
    submit = SubmitField('Отправить')
