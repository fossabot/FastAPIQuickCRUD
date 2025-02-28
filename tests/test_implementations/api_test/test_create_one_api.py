import json
import random
import uuid
from datetime import date, timedelta, datetime, timezone

from starlette.testclient import TestClient

from src.fastapi_quickcrud import sqlalchemy_to_pydantic
from src.fastapi_quickcrud.crud_router import crud_router_builder
from src.fastapi_quickcrud.crud_router import CrudService
from src.fastapi_quickcrud.misc.exceptions import ConflictColumnsCannotHit
from src.fastapi_quickcrud.misc.type import CrudMethods
from tests.test_implementations.api_test import get_transaction_session, app, UntitledTable256

UntitledTable256_service = CrudService(model=UntitledTable256)

UntitledTable256Model = sqlalchemy_to_pydantic(UntitledTable256,
                                               crud_methods=[
                                                   CrudMethods.UPSERT_ONE
                                               ],
                                               exclude_columns=['bytea_value', 'xml_value', 'box_valaue'])
# Model Test
# api_model = UntitledTable256Model.__dict__['POST']
# assert api_model
# create_one_model = api_model[CrudMethods.UPSERT_ONE].__dict__
# assert create_one_model['requestModel'] or create_one_model['responseModel']
# create_one_request_model = deepcopy(create_one_model['requestModel'].__dict__['__fields__'])
# create_one_response_model = deepcopy(create_one_model['responseModel'].__dict__['__fields__'])
# Request Test
# assert create_one_request_model.pop('on_conflict', False)
# for k, v in create_one_request_model.items():
#     sql_schema = UntitledTable256.__dict__[v.name].comparator
#
#     if sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif not sql_schema.nullable and sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif sql_schema.nullable:
#         assert not v.required
#     elif not sql_schema.nullable:
#         assert v.required
#     elif not sql_schema.nullable and not sql_schema.server_default or not sql_schema.default:
#         assert v.required
#     else:
#         print(f"{v.name=}")
#         print(f"{v.required=}")
#         print(f"{v.default=}")

# Response Test
# for k, v in create_one_response_model.items():
#     sql_schema = UntitledTable256.__dict__[v.name].comparator
#
#     if sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif not sql_schema.nullable and sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif sql_schema.nullable:
#         assert not v.required
#     elif not sql_schema.nullable:
#         assert v.required
#     elif not sql_schema.nullable and not sql_schema.server_default or not sql_schema.default:
#         assert v.required
#     else:
#         print(f"{v.name=}")
#         print(f"{v.required=}")
#         print(f"{v.default=}")

test_create_one = crud_router_builder(db_session=get_transaction_session,
                                      crud_service=UntitledTable256_service,
                                      crud_models=UntitledTable256Model,
                                      prefix="/test_creation_one",
                                      tags=["test"]
                                      )
UntitledTable256Model = sqlalchemy_to_pydantic(UntitledTable256,
                                               crud_methods=[
                                                   CrudMethods.UPSERT_MANY,
                                               ],
                                               exclude_columns=['bytea_value', 'xml_value', 'box_valaue'])
# # Model Test
# api_model = UntitledTable256Model.__dict__['POST']
# assert api_model
# create_many_model = api_model[CrudMethods.UPSERT_MANY].__dict__
# assert create_many_model['requestModel'] or create_many_model['responseModel']
# create_many_request_model = deepcopy(create_many_model['requestModel'].__dict__['__fields__'])
# create_many_response_model = deepcopy(create_many_model['responseModel'].__dict__['__fields__'])
#
# # Request Model Test
# assert create_many_request_model.pop('on_conflict', None)
# insert_many_model = create_many_request_model['insert'].sub_fields[0].outer_type_.__dict__['__fields__']
# for k, v in insert_many_model.items():
#     sql_schema = UntitledTable256.__dict__[v.name].comparator
#
#     if sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif not sql_schema.nullable and sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif sql_schema.nullable:
#         assert not v.required
#     elif not sql_schema.nullable:
#         assert v.required
#     elif not sql_schema.nullable and not sql_schema.server_default or not sql_schema.default:
#         assert v.required
#     else:
#         print(f"{v.name=}")
#         print(f"{v.required=}")
#         print(f"{v.default=}")
#
# # Response Model Test
# for k, v in create_many_response_model.items():
#     create_many_response_model_item = v.type_.__dict__['__fields__']
#     for k, v in create_many_response_model_item.items():
#         sql_schema = UntitledTable256.__dict__[v.name].comparator
#
#         if sql_schema.server_default or sql_schema.default:
#             assert not v.required
#         elif not sql_schema.nullable and sql_schema.server_default or sql_schema.default:
#             assert not v.required
#         elif sql_schema.nullable:
#             assert not v.required
#         elif not sql_schema.nullable:
#             assert v.required
#         elif not sql_schema.nullable and not sql_schema.server_default or not sql_schema.default:
#             assert v.required
#         else:
#             print(f"{v.name=}")
#             print(f"{v.required=}")
#             print(f"{v.default=}")

test_create_many = crud_router_builder(db_session=get_transaction_session,
                                       crud_service=UntitledTable256_service,
                                       crud_models=UntitledTable256Model,
                                       prefix="/test_creation_many",
                                       tags=["test"]
                                       )

# Response Mode Test
# response_many = create_many_response_model['__root__'].sub_fields[0].outer_type_.__dict__['__fields__']
# for k, v in response_many.items():
#     assert not v.required

UntitledTable256Model = sqlalchemy_to_pydantic(UntitledTable256,
                                               crud_methods=[
                                                   CrudMethods.POST_REDIRECT_GET
                                               ],
                                               exclude_columns=['bytea_value', 'xml_value', 'box_valaue'])
# Model Test
# api_model = UntitledTable256Model.__dict__['POST']
# assert api_model
# post_redirect_get_model = api_model[CrudMethods.POST_REDIRECT_GET].__dict__
# assert post_redirect_get_model['requestModel'] or post_redirect_get_model['responseModel']
# post_redirect_get_request_model = deepcopy(post_redirect_get_model['requestModel'].__dict__['__fields__'])
# post_redirect_get_response_model = deepcopy(post_redirect_get_model['responseModel'].__dict__['__fields__'])

# Request Model Test

# for k, v in post_redirect_get_request_model.items():
#     sql_schema = UntitledTable256.__dict__[v.name].comparator
#
#     if sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif not sql_schema.nullable and sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif sql_schema.nullable:
#         assert not v.required
#     elif not sql_schema.nullable:
#         assert v.required
#     elif not sql_schema.nullable and not sql_schema.server_default or not sql_schema.default:
#         assert v.required
#     else:
#         print(f"{v.name=}")
#         print(f"{v.required=}")
#         print(f"{v.default=}")

# Response Model Test
# for k, v in post_redirect_get_response_model.items():
#     sql_schema = UntitledTable256.__dict__[v.name].comparator
#
#     if sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif not sql_schema.nullable and sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif sql_schema.nullable:
#         assert not v.required
#     elif not sql_schema.nullable:
#         assert v.required
#     elif not sql_schema.nullable and not sql_schema.server_default or not sql_schema.default:
#         assert v.required
#     else:
#         print(f"{v.name=}")
#         print(f"{v.required=}")
#         print(f"{v.default=}")

# for k, v in post_redirect_get_response_model.items():
#     assert v.required

test_post_and_redirect_get = crud_router_builder(db_session=get_transaction_session,
                                                 crud_service=UntitledTable256_service,
                                                 crud_models=UntitledTable256Model,
                                                 prefix="/test_post_direct_get",
                                                 tags=["test"]
                                                 )

UntitledTable256Model = sqlalchemy_to_pydantic(UntitledTable256,
                                               crud_methods=[
                                                   CrudMethods.FIND_ONE
                                               ],
                                               exclude_columns=['bytea_value', 'xml_value', 'box_valaue'])
# # # Model Test
# api_model = UntitledTable256Model.__dict__['GET']
# assert api_model
# get_one_model = api_model[CrudMethods.FIND_ONE].__dict__
# assert get_one_model['requestModel'] or get_one_model['responseModel']
# get_one_request_model = deepcopy(get_one_model['requestModel'].__dict__['__fields__'])
# get_one_response_model = deepcopy(get_one_model['responseModel'].__dict__['__fields__'])
# primary_key_of_get_sql_schema = get_one_request_model[UntitledTable256.__dict__['primary_key_of_table']]
# assert not primary_key_of_get_sql_schema.required
# get_one_request_model.pop(UntitledTable256.__dict__['primary_key_of_table'], None)
# for k, v in get_one_request_model.items():
#     assert not v.required
# # FIXME some thing may not require
# for k, v in get_one_response_model.items():
#     sql_schema = UntitledTable256.__dict__[v.name].comparator
#
#     if sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif not sql_schema.nullable and sql_schema.server_default or sql_schema.default:
#         assert not v.required
#     elif sql_schema.nullable:
#         assert not v.required
#     elif not sql_schema.nullable:
#         assert v.required
#     elif not sql_schema.nullable and not sql_schema.server_default or not sql_schema.default:
#         assert v.required
#     else:
#         print(f"{v.name=}")
#         print(f"{v.required=}")
#         print(f"{v.default=}")
test_get_data = crud_router_builder(db_session=get_transaction_session,
                                    crud_service=UntitledTable256_service,
                                    crud_models=UntitledTable256Model,
                                    prefix="/test",
                                    tags=["test"]
                                    )
[app.include_router(i) for i in [test_post_and_redirect_get, test_create_one, test_create_many, test_get_data]]

client = TestClient(app)

primary_key_name = UntitledTable256.primary_key_of_table
unique_fields = UntitledTable256.unique_fields


# Create One API Test

def create_example_data():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    data = '{"float4_value": 0, "int2_value": 0, "int4_value": 0 }'

    response = client.post('/test_creation_one', headers=headers, data=data)
    assert response.status_code == 201
    return response.json()


def test_try_only_input_required_fields():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    data = {"float4_value": 0.0, "int2_value": 0, "int4_value": 0, 'uuid_value':'3fa85f64-5717-4562-b3fc-2c963f66afa6'}

    response = client.post('/test_creation_one', headers=headers, data=json.dumps(data))
    assert response.status_code == 201
    response_result = response.json()
    for k, v in data.items():
        assert response_result[k] == v


def test_try_input_with_conflict_but_conflict_columns_not_hit():
    sample_data = create_example_data()
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    data = {"on_conflict": {"update_columns": ["bool_value", "float8_value", "varchar_value", "interval_value",
                                               "time_value", "int8_value", "jsonb_value", "timetz_value",
                                               "array_str__value", "text_value", "char_value", "uuid_value",
                                               "array_value", "numeric_value", "timestamp_value", "int2_value",
                                               "date_value", "json_value", "timestamptz_value"]}}
    for k, v in sample_data.items():
        data[k] = v
    for k, v in {"float4_value": 99, "int2_value": 99, "int4_value": 99}.items():
        data[k] = v
    # for k, v in {"float4_value": 99.9, "int2_value": 99, "int4_value": 99}.items():
    #     data[k] = v
    try:
        _ = json.dumps(data)
        response = client.post('/test_creation_one', headers=headers, data=json.dumps(data))
    except ConflictColumnsCannotHit as e:
        pass
    assert response.status_code == 409


def test_try_input_with_conflict():
    sample_data = create_example_data()
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    data = {"on_conflict": {"update_columns": ["bool_value", "float8_value", "varchar_value", "interval_value",
                                               "time_value", "int8_value", "jsonb_value", "timetz_value",
                                               "array_str__value", "text_value", "char_value", "uuid_value",
                                               "array_value", "numeric_value", "timestamp_value", "int2_value",
                                               "date_value", "json_value", "timestamptz_value"]}}
    for k, v in sample_data.items():
        data[k] = v
    for k, v in {"float4_value": 0.0, "int2_value": 99, "int4_value": 0}.items():
        data[k] = v
    response = client.post('/test_creation_one', headers=headers, data=json.dumps(data))
    assert response.status_code == 201
    response_result = response.json()
    for k, v in response_result.items():
        if k in data:
            if isinstance(v, str):
                v = v.strip()
            assert json.dumps(data[k]).strip() == json.dumps(v).strip()


def test_try_input_without_conflict():
    sample_data = create_example_data()

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    data = {}
    for k, v in sample_data.items():
        data[k] = v
    for k, v in {"float4_value": 0.0, "int2_value": 99, "int4_value": 0}.items():
        data[k] = v
    # data['on_conflict'] = {'update_columns': []}

    response = client.post('/test_creation_one', headers=headers, data=json.dumps(data))
    assert response.status_code == 409


def test_update_specific_columns_when_conflict():
    def update_all_fields():
        headers = {
            'accept': 'application/json',
        }
        sample_data = create_example_data()
        response = client.get(f'/test/{sample_data[primary_key_name]}', headers=headers)
        assert response.status_code == 200
        response_data = response.json()
        # upsert the data
        update_column_on_conflict = {
            "update_columns": [
                "int8_value",
                "numeric_value",
                "varchar_value",
                "json_value",
                "float8_value",
                "time_value",
                "timestamp_value",
                "timestamptz_value",
                "array_value",
                "bool_value",
                "array_str__value",
                "int2_value",
                "text_value",
                "uuid_value",
                "char_value",
                "jsonb_value",
                "interval_value",
                "date_value",
                "timetz_value"
            ]
        }
        response_data['on_conflict'] = update_column_on_conflict
        ran_num = random.randint(5, 100)

        bool_value_change = not response_data['bool_value']
        char_value_change = "test"
        date_value_change = str(date.today() - timedelta(days=1))
        float8_value_change = 0.1
        int2_value_change = 100
        int8_value_change = 100
        interval_value_change = float(5400)
        json_value_change = {"hello": "world"}
        jsonb_value_change = {"hello": "world"}
        numeric_value_change = 19
        text_value_change = 'hello world'
        time_value_change = '18:18:18'
        timestamp_value_change = str(datetime.utcnow().isoformat())
        timestamptz_value_change = str(datetime.utcnow().replace(tzinfo=timezone.utc).isoformat())
        timetz_value_change = '18:18:18+00:00'
        uuid_value_change = str(uuid.uuid4())
        varchar_value_change = 'hello world'
        array_value_change = [1, 2, 3, 4]
        array_str__value_change = ['1', '2', '3', '4']
        change = {}

        change['bool_value'] = bool_value_change
        change['char_value'] = char_value_change
        change['date_value'] = date_value_change
        change['float8_value'] = float8_value_change
        change['int2_value'] = int2_value_change
        change['int8_value'] = int8_value_change
        change['interval_value'] = interval_value_change
        change['json_value'] = json_value_change
        change['jsonb_value'] = jsonb_value_change
        change['numeric_value'] = numeric_value_change
        change['text_value'] = text_value_change
        change['time_value'] = time_value_change
        change['timestamp_value'] = timestamp_value_change
        change['timestamptz_value'] = timestamptz_value_change
        change['timetz_value'] = timetz_value_change
        change['uuid_value'] = uuid_value_change
        change['varchar_value'] = varchar_value_change
        change['array_value'] = array_value_change
        change['array_str__value'] = array_str__value_change
        for k, v in change.items():
            response_data[k] = v
        response = client.post('/test_creation_one', headers=headers, data=json.dumps(response_data))
        assert response.status_code == 201
        response_result = response.json()
        for k, v in response_result.items():
            if k in change:
                if isinstance(v, str):
                    v = v.strip()

                assert json.dumps(change[k]).strip() == json.dumps(v).strip()

    def update_partial_fields():
        headers = {
            'accept': 'application/json',
        }

        sample_data = create_example_data()
        response = client.get(f'/test/{sample_data[primary_key_name]}', headers=headers)
        assert response.status_code == 200
        response_data = response.json()
        # upsert the data
        update_column_on_conflict = {
            "update_columns": [
                "varchar_value",
                "json_value",
                "float8_value",
                "time_value",
                "timestamp_value",
                "timestamptz_value",
                "array_value",
                "bool_value",
                "array_str__value",
                "char_value",
                "jsonb_value",
                "interval_value",
                "date_value",
                "timetz_value"
            ]
        }
        response_data['on_conflict'] = update_column_on_conflict
        ran_num = random.randint(5, 100)

        bool_value_change = not response_data['bool_value']
        char_value_change = "test"
        date_value_change = str(date.today() - timedelta(days=1))
        float8_value_change = 0.1
        interval_value_change = float(5400)
        json_value_change = {"hello": "world"}
        jsonb_value_change = {"hello": "world"}
        time_value_change = '18:18:18'
        timestamp_value_change = str(datetime.utcnow().isoformat())
        timestamptz_value_change = str(datetime.utcnow().replace(tzinfo=timezone.utc).isoformat())
        timetz_value_change = '18:18:18+00:00'
        varchar_value_change = 'hello world'
        array_value_change = [1, 2, 3, 4]
        array_str__value_change = ['1', '2', '3', '4']
        change = {}

        change['bool_value'] = bool_value_change
        change['char_value'] = char_value_change
        change['date_value'] = date_value_change
        change['float8_value'] = float8_value_change
        change['interval_value'] = interval_value_change
        change['json_value'] = json_value_change
        change['jsonb_value'] = jsonb_value_change
        change['time_value'] = time_value_change
        change['timestamp_value'] = timestamp_value_change
        change['timestamptz_value'] = timestamptz_value_change
        change['timetz_value'] = timetz_value_change
        change['varchar_value'] = varchar_value_change
        change['array_value'] = array_value_change
        change['array_str__value'] = array_str__value_change
        for k, v in change.items():
            response_data[k] = v
        response = client.post('/test_creation_one', headers=headers, data=json.dumps(response_data))
        assert response.status_code == 201
        response_result = response.json()
        for k, v in response_result.items():
            if k in change:
                if isinstance(v, str):
                    v = v.strip()

                assert json.dumps(change[k]).strip() == json.dumps(v).strip()

    update_all_fields()
    update_partial_fields()

