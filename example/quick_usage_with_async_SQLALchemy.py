import uvicorn
from fastapi import FastAPI
from sqlalchemy import ARRAY, BigInteger, Boolean, CHAR, Column, Date, DateTime, Float, Integer, \
    JSON, LargeBinary, Numeric, SmallInteger, String, Text, Time, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import INTERVAL, JSONB, UUID
from sqlalchemy.orm import declarative_base, sessionmaker, synonym

from src.fastapi_quickcrud import CrudMethods as CrudRouter
from src.fastapi_quickcrud import CrudService
from src.fastapi_quickcrud import crud_router_builder
from src.fastapi_quickcrud import sqlalchemy_to_pydantic

app = FastAPI()

Base = declarative_base()
metadata = Base.metadata

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine('postgresql+asyncpg://postgres:1234@127.0.0.1:5432/postgres', future=True, echo=True,
                             pool_use_lifo=True, pool_pre_ping=True, pool_recycle=7200)
async_session = sessionmaker(bind=engine, class_=AsyncSession)


async def get_transaction_session() -> AsyncSession:
    async with async_session() as session:
        async with session.begin():
            yield session


class ExampleTable(Base):
    __tablename__ = 'example_table'
    __table_args__ = (
        UniqueConstraint('id', 'int4_value', 'float4_value'),
    )
    id = Column(Integer, primary_key=True, info={'alias_name': 'primary_key'},
                server_default=text("nextval('untitled_table_256_id_seq'::regclass)"))
    primary_key = synonym('id')
    bool_value = Column(Boolean, nullable=False, server_default=text("false"))
    bytea_value = Column(LargeBinary)
    char_value = Column(CHAR(10))
    date_value = Column(Date, server_default=text("now()"))
    float4_value = Column(Float, nullable=False)
    float8_value = Column(Float(53), nullable=False, server_default=text("10.10"))
    int2_value = Column(SmallInteger, nullable=False)
    int4_value = Column(Integer, info={'alias_name': 'int4_alias'}, nullable=False)
    int4_alias = synonym('int4_value')
    int8_value = Column(BigInteger, server_default=text("99"))
    interval_value = Column(INTERVAL)
    json_value = Column(JSON)
    jsonb_value = Column(JSONB(astext_type=Text()))
    numeric_value = Column(Numeric)
    text_value = Column(Text, info={'alias_name': 'text_alias'})
    text_alias = synonym('text_value')
    time_value = Column(Time)
    timestamp_value = Column(DateTime)
    timestamptz_value = Column(DateTime(True))
    timetz_value = Column(Time(True))
    uuid_value = Column(UUID(as_uuid=True))
    varchar_value = Column(String)
    array_value = Column(ARRAY(Integer()))
    array_str__value = Column(ARRAY(String()))


UntitledTable256_service = CrudService(model=ExampleTable)

UntitledTable256Model = sqlalchemy_to_pydantic(ExampleTable,
                                               crud_methods=[
                                                   CrudRouter.UPSERT_ONE
                                               ],
                                               exclude_columns=['bytea_value', 'xml_value', 'box_valaue'])

UntitledTable256Model = sqlalchemy_to_pydantic(ExampleTable,
                                               crud_methods=[
                                                   CrudRouter.UPSERT_MANY
                                               ],
                                               exclude_columns=['bytea_value', 'xml_value', 'box_valaue'])

upsert_many_router = crud_router_builder(db_session=get_transaction_session,
                                         crud_service=UntitledTable256_service,
                                         crud_models=UntitledTable256Model,
                                         prefix="/upsert_many",
                                         async_mode=True,
                                         tags=["test"]
                                         )
UntitledTable256Model = sqlalchemy_to_pydantic(ExampleTable,
                                               crud_methods=[
                                                   CrudRouter.POST_REDIRECT_GET
                                               ],
                                               exclude_columns=['bytea_value', 'xml_value', 'box_valaue'])

post_redirect_get_router = crud_router_builder(db_session=get_transaction_session,
                                               crud_service=UntitledTable256_service,
                                               crud_models=UntitledTable256Model,
                                               prefix="/post_redirect_get",
                                               async_mode=True,
                                               tags=["test"]
                                               )

example_table_full_api = sqlalchemy_to_pydantic(ExampleTable,
                                                crud_methods=[
                                                    CrudRouter.FIND_MANY,
                                                    CrudRouter.FIND_ONE,
                                                    CrudRouter.UPSERT_ONE,
                                                    CrudRouter.UPDATE_MANY,
                                                    CrudRouter.UPDATE_ONE,
                                                    CrudRouter.DELETE_ONE,
                                                    CrudRouter.DELETE_MANY,
                                                    CrudRouter.PATCH_MANY,
                                                    CrudRouter.PATCH_ONE,

                                                ],
                                                exclude_columns=['array_str__value', 'bytea_value', 'xml_value',
                                                                 'box_valaue'])

example_table_full_router = crud_router_builder(db_session=get_transaction_session,
                                                crud_service=UntitledTable256_service,
                                                crud_models=example_table_full_api,
                                                async_mode=True,
                                                prefix="/test_CRUD",
                                                tags=["test"]
                                                )

# Base.metadata.create_all(engine)
# unknown reason that will throw error when add the code following
# async def create_table():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#         print('created')
#     print('done')
#     return
#
# asyncio.run(create_table())
# loop.stop()
# loop.close()
# print(loop.is_closed())
[app.include_router(i) for i in [example_table_full_router, post_redirect_get_router, upsert_many_router]]
uvicorn.run(app, host="0.0.0.0", port=8000, debug=False)
