from datetime import datetime
from sqlmodel import create_engine, Session, SQLModel, select
from api.config import DB_HOST, DB_DATABASE, DB_PASSWORD, DB_PORT, DB_USERNAME, ENV
from api.modules.users.models import User
from api.modules.countries.models import Country

# Your existing engine configuration
engine = create_engine(
    f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}',
    echo=ENV == 'dev',
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def add_initial_data():
    with Session(engine) as session:
        country_count = session.exec(select(Country)).first()
        if not country_count:
            countries_data = [
                Country(
                    id=1,
                    name='España',
                    iso_code='ES',
                    iso_code_alpha_3='ESP',
                    indicative='34',
                    currency='EUR',
                    currency_symbol='€',
                    time_zone='Europe/Madrid',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=2,
                    name='Colombia',
                    iso_code='CO',
                    iso_code_alpha_3='COL',
                    indicative='57',
                    currency='COP',
                    currency_symbol='$',
                    time_zone='America/Bogota',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=3,
                    name='México',
                    iso_code='MX',
                    iso_code_alpha_3='MEX',
                    indicative='52',
                    currency='MXN',
                    currency_symbol='$',
                    time_zone='America/Mexico_City',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=4,
                    name='República Dominicana',
                    iso_code='DO',
                    iso_code_alpha_3='DOM',
                    indicative='1',
                    currency='DOP',
                    currency_symbol='RD$',
                    time_zone='America/Santo_Domingo',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=5,
                    name='El Salvador',
                    iso_code='SV',
                    iso_code_alpha_3='SLV',
                    indicative='503',
                    currency='USD',
                    currency_symbol='$',
                    time_zone='America/El_Salvador',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=6,
                    name='Guatemala',
                    iso_code='GT',
                    iso_code_alpha_3='GTM',
                    indicative='502',
                    currency='GTQ',
                    currency_symbol='Q',
                    time_zone='America/Guatemala',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=7,
                    name='Chile',
                    iso_code='CL',
                    iso_code_alpha_3='CHL',
                    indicative='56',
                    currency='CLP',
                    currency_symbol='$',
                    time_zone='America/Santiago',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=8,
                    name='Argentina',
                    iso_code='AR',
                    iso_code_alpha_3='ARG',
                    indicative='54',
                    currency='ARS',
                    currency_symbol='$',
                    time_zone='America/Argentina/Buenos_Aires',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=9,
                    name='Paraguay',
                    iso_code='PY',
                    iso_code_alpha_3='PRY',
                    indicative='595',
                    currency='PYG',
                    currency_symbol='Gs',
                    time_zone='America/Asuncion',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=10,
                    name='Uruguay',
                    iso_code='UY',
                    iso_code_alpha_3='URY',
                    indicative='598',
                    currency='UYU',
                    currency_symbol='$U',
                    time_zone='America/Montevideo',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=11,
                    name='Ecuador',
                    iso_code='EC',
                    iso_code_alpha_3='ECU',
                    indicative='593',
                    currency='USD',
                    currency_symbol='$',
                    time_zone='America/Guayaquil',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=12,
                    name='Honduras',
                    iso_code='HN',
                    iso_code_alpha_3='HND',
                    indicative='504',
                    currency='HNL',
                    currency_symbol='L',
                    time_zone='America/Tegucigalpa',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=13,
                    name='Panamá',
                    iso_code='PA',
                    iso_code_alpha_3='PAN',
                    indicative='507',
                    currency='PAB',
                    currency_symbol='B/.',
                    time_zone='America/Panama',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=14,
                    name='Perú',
                    iso_code='PE',
                    iso_code_alpha_3='PER',
                    indicative='51',
                    currency='PEN',
                    currency_symbol='S/.',
                    time_zone='America/Lima',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
                Country(
                    id=15,
                    name='Bolivia',
                    iso_code='BO',
                    iso_code_alpha_3='BOL',
                    indicative='591',
                    currency='BOB',
                    currency_symbol='Bs',
                    time_zone='America/La_Paz',
                    created_at=datetime.fromisoformat('2022-10-29 22:42:13'),
                    updated_at=datetime.fromisoformat('2024-11-07 10:41:47'),
                ),
            ]

            for country in countries_data:
                session.add(country)
            session.commit()

        user_count = session.exec(select(User)).first()
        if not user_count:
            now = datetime.now()
            users_data = [
                User(
                    name='Juan',
                    email='juan.perez@email.com',
                    last_name='Pérez',
                    created_at=now,
                    updated_at=now,
                    country_id=1,
                ),
                User(
                    name='María',
                    email='maria.lopez@email.com',
                    last_name='López',
                    created_at=now,
                    updated_at=now,
                    country_id=2,
                ),
                User(
                    name='Carlos',
                    email='carlos.garcia@email.com',
                    last_name='García',
                    created_at=now,
                    updated_at=now,
                    country_id=1,
                ),
                User(
                    name='Ana',
                    email='ana.torres@email.com',
                    last_name='Torres',
                    created_at=now,
                    updated_at=now,
                    country_id=3,
                ),
                User(
                    name='Luis',
                    email='luis.mendoza@email.com',
                    last_name='Mendoza',
                    created_at=now,
                    updated_at=now,
                    country_id=None,
                ),
                User(
                    name='Sofía',
                    email='sofia.ramirez@email.com',
                    last_name='Ramírez',
                    created_at=now,
                    updated_at=now,
                    country_id=2,
                ),
            ]

            for user in users_data:
                session.add(user)
            session.commit()
