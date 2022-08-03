import requests

from ..configuration import SERVICE_URL
from ..src.baseclasses.response import Response
from ..src.schemas.user import User


# def test_equal():
#     resp = requests.get(url=SERVICE_URL)
#     print('\n', resp.json())


def test_getting_users_list():
    response = requests.get(url=SERVICE_URL)
    test_object = Response(response)
    test_object.asser_status_code(300).validate(User)



 # z =  {
 #     'meta': {
 #         'pagination': {
 #             'total': 2749,
 #             'pages': 275,
 #             'page': 1,
 #             'limit': 10,
 #             'links': {
 #                 'previous': None,
 #                 'current': 'https://gorest.co.in/public/v1/users?page=1',
 #                 'next': 'https://gorest.co.in/public/v1/users?page=2'
 #             }
 #         }
 #     },
 #     'data': [
 #         {
 #             'id': 2781,
 #             'name': 'Anaadi Mehra',
 #             'email': 'anaadi_mehra@grant.org',
 #             'gender': 'female',
 #             'status': 'inactive'
 #         },
 #         {
 #             'id': 2780,
 #             'name': 'Mrs. Divjot Pillai',
 #             'email': 'mrs_pillai_divjot@mann-luettgen.org',
 #             'gender': 'male',
 #             'status': 'inactive'
 #         },
 #         {
 #             'id': 2779,
 #             'name': 'Yogendra Kaur',
 #             'email': 'kaur_yogendra@yundt.net',
 #             'gender': 'female',
 #             'status': 'inactive'
 #         },
 #         {
 #             'id': 2778,
 #             'name': 'Vrund Guha',
 #             'email': 'vrund_guha@beahan.biz',
 #             'gender': 'female',
 #             'status': 'active'
 #         },
 #         {
 #             'id': 2777,
 #             'name': 'Miss Brahmdev Mukhopadhyay',
 #             'email': 'miss_mukhopadhyay_brahmdev@boehm-leuschke.biz',
 #             'gender': 'female',
 #             'status': 'inactive'
 #         },
 #         {
 #             'id': 2776,
 #             'name': 'Bodhan Chattopadhyay',
 #             'email': 'bodhan_chattopadhyay@hilll.org',
 #             'gender': 'female',
 #             'status': 'active'
 #         },
 #         {
 #             'id': 2775,
 #             'name': 'Bodhan Rana',
 #             'email': 'rana_bodhan@dubuque-cummerata.net',
 #             'gender': 'male',
 #             'status': 'active'
 #         },
 #         {
 #             'id': 2774,
 #             'name': 'Javas Malik',
 #             'email': 'malik_javas@thiel.org',
 #             'gender': 'male',
 #             'status': 'inactive'
 #         },
 #         {
 #             'id': 2773,
 #             'name': 'Vidur Gowda III',
 #             'email': 'iii_gowda_vidur@kulas-ritchie.net',
 #             'gender': 'male',
 #             'status': 'inactive'
 #         },
 #         {
 #             'id': 2771,
 #             'name': 'Param Ahluwalia',
 #             'email': 'ahluwalia_param@brown.net',
 #             'gender': 'male',
 #             'status': 'inactive'
 #         }
 #     ]
 # }
