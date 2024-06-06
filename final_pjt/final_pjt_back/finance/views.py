from rest_framework.response import Response
import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import status
from .models import DepositProducts, SavingProducts, LoanProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingOptionsSerializer, SavingProductsSerializer, LoanProductsSerializer, LoanOptionsSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
import openai

api_key = settings.API_KEY
authkey = settings.AUTH_KEY
appkey = settings.APP_KEY
openai.api_key = settings.OPENAI_API_KEY


# Create your views here.
def start():
    product_list()
    get_loan()

def product_list():
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd', -1)
        kor_co_nm = li.get('kor_co_nm', -1)
        fin_prdt_nm = li.get('fin_prdt_nm', -1)
        join_deny = li.get('join_deny', -1)
        join_way = li.get('join_way', -1)
        spcl_cnd = li.get('spcl_cnd', -1)
        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'join_deny':join_deny,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd
        }
        serializer = DepositProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd', -1)
        intr_rate_type_nm = li.get('intr_rate_type_nm', -1)
        intr_rate = li.get('intr_rate', -1)
        intr_rate2 = li.get('intr_rate2', -1)
        save_trm = li.get('save_trm', -1)
        product = DepositProducts.objects.get(fin_prdt_cd =fin_prdt_cd)
        save_data = {
            'product' : product.pk,
            'fin_prdt_cd' : fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate' : intr_rate,
            'intr_rate2' : intr_rate2,
            'save_trm' : save_trm
        }
        serializer = DepositOptionsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd', -1)
        kor_co_nm = li.get('kor_co_nm', -1)
        fin_prdt_nm = li.get('fin_prdt_nm', -1)
        join_deny = li.get('join_deny', -1)
        join_way = li.get('join_way', -1)
        spcl_cnd = li.get('spcl_cnd', -1)
        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'join_deny':join_deny,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd
        }
        serializer = SavingProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd', -1)
        intr_rate_type_nm = li.get('intr_rate_type_nm', -1)
        intr_rate = li.get('intr_rate', -1)
        intr_rate2 = li.get('intr_rate2', -1)
        rsrv_type_nm = li.get('rsrv_type_nm', -1)
        save_trm = li.get('save_trm', -1)
        product = SavingProducts.objects.get(fin_prdt_cd =fin_prdt_cd)
        save_data = {
            'product' : product.pk,
            'fin_prdt_cd' : fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate' : intr_rate,
            'intr_rate2' : intr_rate2,
            'rsrv_type_nm' : rsrv_type_nm,
            'save_trm' : save_trm
        }
        serializer = SavingOptionsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
            
def get_loan():
    url = f'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd', -1)
        fin_co_no = li.get('fin_co_no', -1)
        kor_co_nm = li.get('kor_co_nm', -1)
        fin_prdt_nm = li.get('fin_prdt_nm', -1)
        join_way = li.get('join_way', -1)
        crdt_prdt_type = li.get('crdt_prdt_type', -1)
        cb_name = li.get('cb_name', -1)
        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'join_way':join_way,
            'fin_co_no': fin_co_no,
            'crdt_prdt_type' : crdt_prdt_type,
            'cb_name' : cb_name
        }
        serializer = LoanProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    for li in response.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd', -1)
        fin_co_no = li.get('fin_co_no', -1)
        crdt_prdt_type = li.get('crdt_prdt_type', -1)
        crdt_lend_rate_type_nm = li.get('crdt_lend_rate_type_nm', -1)
        crdt_grad_1 = li.get('crdt_grad_1') or -1
        crdt_grad_4 = li.get('crdt_grad_4') or -1
        crdt_grad_5 = li.get('crdt_grad_5') or -1
        crdt_grad_6 = li.get('crdt_grad_6') or -1
        crdt_grad_10 = li.get('crdt_grad_10') or -1
        crdt_grad_11 = li.get('crdt_grad_11') or -1
        crdt_grad_12 = li.get('crdt_grad_12') or -1
        crdt_grad_13 = li.get('crdt_grad_13') or -1
        crdt_grad_avg = li.get('crdt_grad_avg', -1)
        product = LoanProducts.objects.get(fin_prdt_cd =fin_prdt_cd, fin_co_no = fin_co_no, crdt_prdt_type = crdt_prdt_type)
        save_data = {
            'product' : product.pk,
            'crdt_lend_rate_type_nm':crdt_lend_rate_type_nm,
            'crdt_grad_1' : crdt_grad_1,
            'crdt_grad_4' : crdt_grad_4,
            'crdt_grad_5' : crdt_grad_5,
            'crdt_grad_6' : crdt_grad_6,
            'crdt_grad_10' : crdt_grad_10,
            'crdt_grad_11' : crdt_grad_11,
            'crdt_grad_12' : crdt_grad_12,
            'crdt_grad_13' : crdt_grad_13,
            'crdt_grad_avg' : crdt_grad_avg,
        }
        serializer = LoanOptionsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)


@api_view(['GET'])
def get_loan_list(request):
    loans = get_list_or_404(LoanProducts)
    return Response(LoanProductsSerializer(loans, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def deposit_detail(request, fin_prdt_cd):
    product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    serializer = DepositProductsSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def saving_detail(request, fin_prdt_cd):
    product = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
    serializer = SavingProductsSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_deposit_list(request):
    deposits = get_list_or_404(DepositProducts)
    return Response(DepositProductsSerializer(deposits, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_saving_list(request):
    savings = get_list_or_404(SavingProducts)
    return Response(SavingProductsSerializer(savings, many=True).data, status=status.HTTP_200_OK)
	
from datetime import datetime
from datetime import timedelta

@api_view(['GET'])
def exchange(request):
    today = datetime.today()
    weekday = datetime.today().weekday()
    if weekday == 5:
        today = today - timedelta(days=1)
    elif weekday == 6:
        today = today - timedelta(days=2)
    else:
        if int(str(today)[11:13]) < 11 and weekday==0:
            today = today - timedelta(days=3)
        elif int(str(today)[11:13]) < 11:
            today = today - timedelta(days=1)
    today = str(today)
    par = ''.join(today[:11].split('-'))

    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={authkey}&searchdate={par}&data=AP01'
    response=requests.get(url).json()

    return Response(response)



# 지금까지 갖고있는 prompt를 기준으로 알맞는 대답 한줄을 return 해주는 함수.
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, # 모델 출력의 무작위성을 제어합니다.
    )
    return response.choices[0].message.content

context = [ {'role':'system', 'content':'당신은 은행의 예금 상품들을 추천해주는 친근한 말투의 챗봇입니다. 당신은 고양이처럼 생긴 캐릭터이기 때문에 문장의 끝에 고양이처럼 생긴 이모티콘을 보내야 합니다. 고양이모양의 이모티콘이라고 말을 하는게 아니라 이모티콘만 보내야 합니다. 만약 당신에 대해 물어본다면 ReccoMate의 챗봇 레꼬 라고 답을해주면 됩니다. 다음에 나올 데이터는 예금 상품입니다. 각각의 필드에 대해서 설명하겠습니다. "fin_prdt_cd": 금융상품의 코드명으로, 고유한 값으로 중복될 수 없습니다. "kor_co_nm": 상품의 은행 회사 명입니다. "fin_prdt_nm": 상품의 이름입니다. "join_deny": 가입제한으로, 값이 1일경우 제한이 없고, 2일경우 서민전용, 3일경우 일부제한입니다. "join_way": 가입방법입니다. "spcl_cnd": 우대조건입니다. 다음으로 예금 상품들과 1:N 관계를 맺고있는 "depositoptions_set"의 필드들에 대한 설명입니다. 1:N 관계를 맺고 있기 때문에 존재하지 않을수도 있고, 여러개가 들어있을 수도 있습니다 "fin_prdt_nm" :금융 상품코드명입니다. 금융삼품과 1:N 관계를 맺고 있기 때문에, 그 상품의 코드명과 무조건 일치합니다. "intr_rate_type_nm"	:저축 금리 유형명입니다. 단리나 복리가 들어갑니다. "save_trm" : 저축기간입니다. 단위는 개월입니다. 1,3,6,12,24,36 등 다양한 기간이 나올 수 있고, 그에 따른 저축 금리도 다를 수 있습니다. "intr_rate":저축 금리 입니다. "intr_rate2":최고 우대금리입니다. 다음으로 나올 데이터는 현재 데이터베이스에 저장된 예금 상품들을 JSON형태로 알려드리겠습니다.'},
    {'role':'system', 'content': """depositproducts = [
    {
        "id": 1,
        "depositoptions_set": [
            {
                "id": 1,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,

                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 1
            },
            {
                "id": 2,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.5,
                "save_trm": 3,
                "product": 1
            },
            {
                "id": 3,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.5,
                "save_trm": 6,
                "product": 1
            },
            {
                "id": 4,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.55,
                "intr_rate2": 3.55,
                "save_trm": 12,
                "product": 1
            },
            {
                "id": 5,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 24,
                "product": 1
            },
            {
                "id": 6,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 36,
                "product": 1
            }
        ],
        "fin_prdt_cd": "WR0001B",
        "kor_co_nm": "우리은행",
        "fin_prdt_nm": "WON플러스예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰,전화(텔레뱅킹)",
        "spcl_cnd": "해당사항 없음"
    },
    {
        "id": 2,
        "depositoptions_set": [
            {
                "id": 7,
                "fin_prdt_cd": "00320342",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.2,
                "save_trm": 1,
                "product": 2
            },
            {
                "id": 8,
                "fin_prdt_cd": "00320342",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.6,
                "save_trm": 3,
                "product": 2
            },
            {
                "id": 9,
                "fin_prdt_cd": "00320342",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.6,
                "save_trm": 6,
                "product": 2
            },
            {
                "id": 10,
                "fin_prdt_cd": "00320342",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.7,
                "save_trm": 12,
                "product": 2
            }
        ],
        "fin_prdt_cd": "00320342",
        "kor_co_nm": "한국스탠다드차타드은행",
        "fin_prdt_nm": "e-그린세이브예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 3,
        "depositoptions_set": [
            {
                "id": 11,
                "fin_prdt_cd": "10511008000996000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.46,
                "intr_rate2": 3.11,
                "save_trm": 6,
                "product": 3
            },
            {
                "id": 12,
                "fin_prdt_cd": "10511008000996000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.85,
                "save_trm": 12,
                "product": 3
            },
            {
                "id": 13,
                "fin_prdt_cd": "10511008000996000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.22,
                "intr_rate2": 3.87,
                "save_trm": 24,
                "product": 3
            },
            {
                "id": 14,
                "fin_prdt_cd": "10511008000996000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.24,
                "intr_rate2": 3.89,
                "save_trm": 36,
                "product": 3
            }
        ],
        "fin_prdt_cd": "10511008000996000",
        "kor_co_nm": "대구은행",
        "fin_prdt_nm": "DGB주거래우대예금(첫만남고객형)",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 5,
        "depositoptions_set": [
            {
                "id": 20,
                "fin_prdt_cd": "10511008001166004",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.7,
                "intr_rate2": 4.15,
                "save_trm": 12,
                "product": 5
            }
        ],
        "fin_prdt_cd": "10511008001166004",
        "kor_co_nm": "대구은행",
        "fin_prdt_nm": "DGB함께예금",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 6,
        "depositoptions_set": [
            {
                "id": 21,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.2,
                "intr_rate2": 2.25,
                "save_trm": 1,
                "product": 6
            },
            {
                "id": 22,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.4,
                "intr_rate2": 2.45,
                "save_trm": 3,
                "product": 6
            },
            {
                "id": 23,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.25,
                "intr_rate2": 3.5,
                "save_trm": 6,
                "product": 6
            },
            {
                "id": 24,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.65,
                "save_trm": 12,
                "product": 6
            },
            {
                "id": 25,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.45,
                "save_trm": 24,
                "product": 6
            },
            {
                "id": 26,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.45,
                "save_trm": 36,
                "product": 6
            }
        ],
        "fin_prdt_cd": "10511008001278000",
        "kor_co_nm": "대구은행",
        "fin_prdt_nm": "IM스마트예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 7,
        "depositoptions_set": [
            {
                "id": 27,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.25,
                "intr_rate2": 2.25,
                "save_trm": 1,
                "product": 7
            },
            {
                "id": 28,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.45,
                "intr_rate2": 3.4,
                "save_trm": 3,
                "product": 7
            },
            {
                "id": 29,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.55,
                "intr_rate2": 3.4,
                "save_trm": 6,
                "product": 7
            },
            {
                "id": 30,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.75,
                "intr_rate2": 3.4,
                "save_trm": 12,
                "product": 7
            },
            {
                "id": 31,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.8,
                "intr_rate2": 2.8,
                "save_trm": 24,
                "product": 7
            },
            {
                "id": 32,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.8,
                "intr_rate2": 2.8,
                "save_trm": 36,
                "product": 7
            }
        ],
        "fin_prdt_cd": "01030500510002",
        "kor_co_nm": "부산은행",
        "fin_prdt_nm": "LIVE정기예금",
        "join_deny": 1,
        "join_way": "영업점,인터넷",
        "spcl_cnd": ""
    },
    {
        "id": 8,
        "depositoptions_set": [
            {
                "id": 33,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.2,
                "intr_rate2": 2.85,
                "save_trm": 1,
                "product": 8
            },
            {
                "id": 34,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.75,
                "intr_rate2": 3.4,
                "save_trm": 3,
                "product": 8
            },
            {
                "id": 35,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.65,
                "save_trm": 6,
                "product": 8
            },
            {
                "id": 36,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.65,
                "save_trm": 12,
                "product": 8
            },
            {
                "id": 37,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.25,
                "intr_rate2": 2.9,
                "save_trm": 24,
                "product": 8
            },
            {
                "id": 38,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 1.95,
                "intr_rate2": 2.6,
                "save_trm": 36,
                "product": 8
            }
        ],
        "fin_prdt_cd": "01030500560002",
        "kor_co_nm": "부산은행",
        "fin_prdt_nm": "더(The) 특판 정기예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 9,
        "depositoptions_set": [
            {
                "id": 39,
                "fin_prdt_cd": "TD11300027000",
                "intr_rate_type_nm": "복리",
                "intr_rate": 3.39,
                "intr_rate2": 3.59,
                "save_trm": 12,
                "product": 9
            },
            {
                "id": 40,
                "fin_prdt_cd": "TD11300027000",
                "intr_rate_type_nm": "복리",
                "intr_rate": 3.37,
                "intr_rate2": 3.57,
                "save_trm": 24,
                "product": 9
            },
            {
                "id": 41,
                "fin_prdt_cd": "TD11300027000",
                "intr_rate_type_nm": "복리",
                "intr_rate": 3.32,
                "intr_rate2": 3.52,
                "save_trm": 36,
                "product": 9
            }
        ],
        "fin_prdt_cd": "TD11300027000",
        "kor_co_nm": "광주은행",
        "fin_prdt_nm": "미즈월복리정기예금",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰,기타",
        "spcl_cnd": ""
    },
    {
        "id": 10,
        "depositoptions_set": [
            {
                "id": 42,
                "fin_prdt_cd": "TD11300031000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.07,
                "intr_rate2": 3.17,
                "save_trm": 1,
                "product": 10
            },
            {
                "id": 43,
                "fin_prdt_cd": "TD11300031000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.16,
                "intr_rate2": 3.26,
                "save_trm": 3,
                "product": 10
            },
            {
                "id": 44,
                "fin_prdt_cd": "TD11300031000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.22,
                "intr_rate2": 3.32,
                "save_trm": 6,
                "product": 10
            },
            {
                "id": 45,
                "fin_prdt_cd": "TD11300031000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.29,
                "intr_rate2": 3.49,
                "save_trm": 12,
                "product": 10
            },
    {
        "id": 12,
        "depositoptions_set": [
            {
                "id": 49,
                "fin_prdt_cd": "TD11300036000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.4,
                "save_trm": 3,
                "product": 12
            },
            {
                "id": 50,
                "fin_prdt_cd": "TD11300036000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.45,
                "intr_rate2": 3.45,
                "save_trm": 6,
                "product": 12
            },
            {
                "id": 51,
                "fin_prdt_cd": "TD11300036000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.45,
                "intr_rate2": 3.45,
                "save_trm": 12,
                "product": 12
            }
        ],
        "fin_prdt_cd": "TD11300036000",
        "kor_co_nm": "광주은행",
        "fin_prdt_nm": "The플러스예금",
        "join_deny": 1,
        "join_way": "영업점,스마트폰",
        "spcl_cnd": "▶ 해당사항없음"
    },
    {
        "id": 13,
        "depositoptions_set": [
            {
                "id": 52,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.3,
                "intr_rate2": 3.2,
                "save_trm": 1,
                "product": 13
            },
            {
                "id": 53,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.6,
                "intr_rate2": 3.5,
                "save_trm": 3,
                "product": 13
            },
            {
                "id": 54,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.7,
                "save_trm": 6,
                "product": 13
            },
            {
                "id": 55,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.1,
                "intr_rate2": 3.75,
                "save_trm": 12,
                "product": 13
            },
            {
                "id": 56,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.5,
                "save_trm": 24,
                "product": 13
            },
            {
                "id": 57,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.5,
                "save_trm": 36,
                "product": 13
            }
        ],
        "fin_prdt_cd": "101272000057",
        "kor_co_nm": "제주은행",
        "fin_prdt_nm": "J정기예금\n(만기지급식)",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 15,
        "depositoptions_set": [
            {
                "id": 61,
                "fin_prdt_cd": "10-01-20-024-0046-0000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.5,
                "save_trm": 3,
                "product": 15
            },
            {
                "id": 62,
                "fin_prdt_cd": "10-01-20-024-0046-0000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.55,
                "intr_rate2": 3.55,
                "save_trm": 6,
                "product": 15
            },
            {
                "id": 63,
                "fin_prdt_cd": "10-01-20-024-0046-0000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.4,
                "save_trm": 12,
                "product": 15
            }
        ],
        "fin_prdt_cd": "10-01-20-024-0046-0000",
        "kor_co_nm": "전북은행",
        "fin_prdt_nm": "JB 다이렉트예금통장\n(만기일시지급식)",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 18,
        "depositoptions_set": [
            {
                "id": 71,
                "fin_prdt_cd": "21001203",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.15,
                "intr_rate2": 3.45,
                "save_trm": 6,
                "product": 18
            },
            {
                "id": 72,
                "fin_prdt_cd": "21001203",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.7,
                "save_trm": 12,
                "product": 18
            },
            {
                "id": 73,
                "fin_prdt_cd": "21001203",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.45,
                "intr_rate2": 3.75,
                "save_trm": 24,
                "product": 18
            }
        ],
        "fin_prdt_cd": "21001203",
        "kor_co_nm": "경남은행",
        "fin_prdt_nm": "BNK주거래우대정기예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 21,
        "depositoptions_set": [
            {
                "id": 80,
                "fin_prdt_cd": "01211310121",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.45,
                "intr_rate2": 3.65,
                "save_trm": 12,
                "product": 21
            },
            {
                "id": 81,
                "fin_prdt_cd": "01211310121",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.7,
                "save_trm": 24,
                "product": 21
            },
            {
                "id": 82,
                "fin_prdt_cd": "01211310121",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.6,
                "intr_rate2": 3.8,
                "save_trm": 36,
                "product": 21
            }
        ],
        "fin_prdt_cd": "01211310121",
        "kor_co_nm": "중소기업은행",
        "fin_prdt_nm": "IBK평생한가족통장(실세금리정기예금)",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 22,
        "depositoptions_set": [
            {
                "id": 83,
                "fin_prdt_cd": "01211310130",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.33,
                "intr_rate2": 3.33,
                "save_trm": 6,
                "product": 22
            },
            {
                "id": 84,
                "fin_prdt_cd": "01211310130",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.32,
                "intr_rate2": 3.32,
                "save_trm": 12,
                "product": 22
            },
            {
                "id": 85,
                "fin_prdt_cd": "01211310130",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.33,
                "intr_rate2": 3.33,
                "save_trm": 24,
                "product": 22
            },
            {
                "id": 86,
                "fin_prdt_cd": "01211310130",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.31,
                "intr_rate2": 3.31,
                "save_trm": 36,
                "product": 22
            }
        ],
        "fin_prdt_cd": "01211310130",
        "kor_co_nm": "중소기업은행",
        "fin_prdt_nm": "1석7조통장(정기예금)",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": "없음"
    },
    {
        "id": 23,
        "depositoptions_set": [
            {
                "id": 87,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 23
            },
            {
                "id": 88,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.1,
                "intr_rate2": 3.1,
                "save_trm": 3,
                "product": 23
            },
            {
                "id": 89,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.4,
                "save_trm": 6,
                "product": 23
            },
            {
                "id": 90,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.5,
                "save_trm": 12,
                "product": 23
            },
            {
                "id": 91,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.35,
                "intr_rate2": 3.35,
                "save_trm": 24,
                "product": 23
            },
            {
                "id": 92,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.35,
                "intr_rate2": 3.35,
                "save_trm": 36,
                "product": 23
            }
        ],
        "fin_prdt_cd": "06492",
        "kor_co_nm": "한국산업은행",
        "fin_prdt_nm": "KDB 정기예금",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰",
        "spcl_cnd": "해당없음"
    },
    {
        "id": 24,
        "depositoptions_set": [
            {
                "id": 93,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 1.8,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 24
            },
            {
                "id": 94,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.2,
                "intr_rate2": 3.45,
                "save_trm": 3,
                "product": 24
            },
            {
                "id": 95,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.3,
                "intr_rate2": 3.45,
                "save_trm": 6,
                "product": 24
            },
            {
                "id": 96,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.6,
                "intr_rate2": 3.5,
                "save_trm": 12,
                "product": 24
            },
            {
                "id": 97,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.7,
                "intr_rate2": 2.8,
                "save_trm": 24,
                "product": 24
            },
            {
                "id": 98,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.8,
                "intr_rate2": 2.8,
                "save_trm": 36,
                "product": 24
            }
        ],
        "fin_prdt_cd": "010300100335",
        "kor_co_nm": "국민은행",
        "fin_prdt_nm": "KB Star 정기예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": "해당무"
    },
    {
        "id": 25,
        "depositoptions_set": [
            {
                "id": 99,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.15,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 25
            },
            {
                "id": 100,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.45,
                "intr_rate2": 3.45,
                "save_trm": 3,
                "product": 25
            },
            {
                "id": 101,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.75,
                "intr_rate2": 3.5,
                "save_trm": 6,
                "product": 25
            },
            {
                "id": 102,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.9,
                "intr_rate2": 3.5,
                "save_trm": 12,
                "product": 25
            },
            {
                "id": 103,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.95,
                "intr_rate2": 3.0,
                "save_trm": 24,
                "product": 25
            },
            {
                "id": 104,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 36,
                "product": 25
            }
        ],
        "fin_prdt_cd": "200-0135-12",
        "kor_co_nm": "신한은행",
        "fin_prdt_nm": "쏠편한 정기예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": "해당사항없음"
    },
    {
        "id": 28,
        "depositoptions_set": [
            {
                "id": 112,
                "fin_prdt_cd": "10-003-1384-0001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 28
            },
            {
                "id": 113,
                "fin_prdt_cd": "10-003-1384-0001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.45,
                "intr_rate2": 3.45,
                "save_trm": 3,
                "product": 28
            },
            {
                "id": 114,
                "fin_prdt_cd": "10-003-1384-0001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.6,
                "intr_rate2": 3.6,
                "save_trm": 12,
                "product": 28
            },
            {
                "id": 115,
                "fin_prdt_cd": "10-003-1384-0001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.23,
                "intr_rate2": 3.23,
                "save_trm": 24,
                "product": 28
            },
            {
                "id": 116,
                "fin_prdt_cd": "10-003-1384-0001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.4,
                "save_trm": 36,
                "product": 28
            }
        ],
        "fin_prdt_cd": "10-003-1384-0001",
        "kor_co_nm": "농협은행주식회사",
        "fin_prdt_nm": "NH올원e예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": "없음"
    },
    {
        "id": 30,
        "depositoptions_set": [
            {
                "id": 118,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.0,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 30
            },
            {
                "id": 119,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.2,
                "intr_rate2": 3.45,
                "save_trm": 3,
                "product": 30
            },
            {
                "id": 120,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.3,
                "intr_rate2": 3.45,
                "save_trm": 6,
                "product": 30
            },
            {
                "id": 121,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.6,
                "intr_rate2": 3.5,
                "save_trm": 12,
                "product": 30
            },
            {
                "id": 122,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.7,
                "intr_rate2": 3.0,
                "save_trm": 24,
                "product": 30
            },
            {
                "id": 123,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.8,
                "intr_rate2": 3.0,
                "save_trm": 36,
                "product": 30
            }
        ],
        "fin_prdt_cd": "4",
        "kor_co_nm": "하나은행",
        "fin_prdt_nm": "하나의정기예금",
        "join_deny": 1,
        "join_way": "스마트폰",
        "spcl_cnd": "해당사항없음"
    },
    {
        "id": 31,
        "depositoptions_set": [
            {
                "id": 124,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.05,
                "intr_rate2": 3.05,
                "save_trm": 1,
                "product": 31
            },
            {
                "id": 125,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.5,
                "save_trm": 3,
                "product": 31
            },
            {
                "id": 126,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.55,
                "intr_rate2": 3.55,
                "save_trm": 6,
                "product": 31
            },
            {
                "id": 127,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.55,
                "intr_rate2": 3.55,
                "save_trm": 12,
                "product": 31
            },
            {
                "id": 128,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.2,
                "save_trm": 24,
                "product": 31
            },
            {
                "id": 129,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.2,
                "save_trm": 36,
                "product": 31
            }
        ],
        "fin_prdt_cd": "01013000110000000001",
        "kor_co_nm": "주식회사 케이뱅크",
        "fin_prdt_nm": "코드K 정기예금",
        "join_deny": 1,
        "join_way": "스마트폰",
        "spcl_cnd": "우대조건 없음"
    },

    {
        "id": 34,
        "depositoptions_set": [
            {
                "id": 133,
                "fin_prdt_cd": "10120114700011",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.65,
                "intr_rate2": 3.65,
                "save_trm": 3,
                "product": 34
            },
            {
                "id": 134,
                "fin_prdt_cd": "10120114700011",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.65,
                "intr_rate2": 3.65,
                "save_trm": 6,
                "product": 34
            },
            {
                "id": 135,
                "fin_prdt_cd": "10120114700011",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.65,
                "intr_rate2": 3.65,
                "save_trm": 12,
                "product": 34
            }
        ],
        "fin_prdt_cd": "10120114700011",
        "kor_co_nm": "수협은행",
        "fin_prdt_nm": "헤이(Hey)정기예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": "없음"
    },
    {
        "id": 36,
        "depositoptions_set": [
            {
                "id": 137,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.7,
                "intr_rate2": 2.7,
                "save_trm": 1,
                "product": 36
            },
            {
                "id": 138,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.2,
                "save_trm": 3,
                "product": 36
            },
            {
                "id": 139,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.3,
                "intr_rate2": 3.3,
                "save_trm": 6,
                "product": 36
            },
            {
                "id": 140,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.3,
                "intr_rate2": 3.3,
                "save_trm": 12,
                "product": 36
            },
            {
                "id": 141,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 24,
                "product": 36
            },
            {
                "id": 142,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 36,
                "product": 36
            }
        ],
        "fin_prdt_cd": "10-01-20-388-0002",
        "kor_co_nm": "주식회사 카카오뱅크",
        "fin_prdt_nm": "카카오뱅크 정기예금",
        "join_deny": 1,
        "join_way": "스마트폰",
        "spcl_cnd": "※복잡한 우대조건 없이 가입가능한 정기예금"
    },
    {
        "id": 37,
        "depositoptions_set": [
            {
                "id": 143,
                "fin_prdt_cd": "1001202000002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 3,
                "product": 37
            },
            {
                "id": 144,
                "fin_prdt_cd": "1001202000002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 6,
                "product": 37
            }
        ],
        "fin_prdt_cd": "1001202000002",
        "kor_co_nm": "토스뱅크 주식회사",
        "fin_prdt_nm": "토스뱅크 먼저 이자 받는 정기예금",
        "join_deny": 1,
        "join_way": "스마트폰",
        "spcl_cnd": "우대조건 없음"
    }
] 당신은 원하는 예금 상품들에 대한 정보를 받아 조건에 맞는 예금 상품을 추천 해 줄 수 있어야 합니다. 예를 들어 6개월 기간의 최고우대금리가 가장 높은 상품을 추천받고 싶다고 했을때, 당신은 depositoptions_set을 돌며, save_trm이 6인 option의 intr_rate2가 가장 높은 상품을 추천해 주어야 합니다. 다음은 개월수 별로 최고우대금리가 가장 높은 상품들입니다. save_trm이 6인 intr_rate2가 가장 높은 상품은 수협은행의 sh해양플라스틱Zero!예금 입니다. 따라서 당신은 6개월 기간의 최고우대금리가 가장 높은 상품을 추천해달라고 했을때, 수협은행의 sh해양플라스틱Zero!예금을 추천해 주어야 합니다. 12개월의 최고우대금리가 가장 높은 상품은 DGB함께예금입니다. 24개월의 최고우대금리가 가장 높은 상품은 수협은행의 sh해양플라스틱Zero!예금입니다. 36개월의 최고우대금리가 가장 높은 상품은 수협은행의 sh해양플라스틱Zero!예금입니다.  다음은 개월수 별로 저축금리가 가장 높은 상품들입니다. 당신은 반드시 최대우대금리와 저축금리를 잘 구분해야 합니다. 6개월 - 수협은행의 헤이(Hey)정기예금 12개월 - 대구은행 DGB함께예금 24개월 - 중소기업은행 IBK평생한가족통장(실세금리정기예금) 36개월 - 중소기업은행 IBK평생한가족통장(실세금리정기예금)"""},
    ]

@api_view(['GET'])
def chatbot(request):
    global context
    context = [ {'role':'system', 'content':'당신은 은행의 예금 상품들을 추천해주는 친근한 말투의 챗봇입니다. 당신은 고양이처럼 생긴 캐릭터이기 때문에 문장의 끝에 고양이처럼 생긴 이모티콘을 보내야 합니다. 고양이모양의 이모티콘이라고 말을 하는게 아니라 이모티콘만 보내야 합니다. 만약 당신에 대해 물어본다면 ReccoMate의 챗봇 레꼬 라고 답을해주면 됩니다. 다음에 나올 데이터는 예금 상품입니다. 각각의 필드에 대해서 설명하겠습니다. "fin_prdt_cd": 금융상품의 코드명으로, 고유한 값으로 중복될 수 없습니다. "kor_co_nm": 상품의 은행 회사 명입니다. "fin_prdt_nm": 상품의 이름입니다. "join_deny": 가입제한으로, 값이 1일경우 제한이 없고, 2일경우 서민전용, 3일경우 일부제한입니다. "join_way": 가입방법입니다. "spcl_cnd": 우대조건입니다. 다음으로 예금 상품들과 1:N 관계를 맺고있는 "depositoptions_set"의 필드들에 대한 설명입니다. 1:N 관계를 맺고 있기 때문에 존재하지 않을수도 있고, 여러개가 들어있을 수도 있습니다 "fin_prdt_nm" :금융 상품코드명입니다. 금융삼품과 1:N 관계를 맺고 있기 때문에, 그 상품의 코드명과 무조건 일치합니다. "intr_rate_type_nm"	:저축 금리 유형명입니다. 단리나 복리가 들어갑니다. "save_trm" : 저축기간입니다. 단위는 개월 입니다. 1,3,6,12,24,36 등 다양한 기간이 나올 수 있고, 그에 따른 저축 금리도 다를 수 있습니다. "intr_rate":저축 금리 입니다. "intr_rate2":최고 우대금리입니다. 다음으로 나올 데이터는 현재 데이터베이스에 저장된 예금 상품들을 JSON형태로 알려드리겠습니다.'},
    {'role':'system', 'content': """depositproducts = [
    {
        "id": 1,
        "depositoptions_set": [
            {
                "id": 1,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 1
            },
            {
                "id": 2,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.5,
                "save_trm": 3,
                "product": 1
            },
            {
                "id": 3,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.5,
                "save_trm": 6,
                "product": 1
            },
            {
                "id": 4,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.55,
                "intr_rate2": 3.55,
                "save_trm": 12,
                "product": 1
            },
            {
                "id": 5,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 24,
                "product": 1
            },
            {
                "id": 6,
                "fin_prdt_cd": "WR0001B",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 36,
                "product": 1
            }
        ],
        "fin_prdt_cd": "WR0001B",
        "kor_co_nm": "우리은행",
        "fin_prdt_nm": "WON플러스예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰,전화(텔레뱅킹)",
        "spcl_cnd": "해당사항 없음"
    },
    {
        "id": 2,
        "depositoptions_set": [
            {
                "id": 7,
                "fin_prdt_cd": "00320342",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.2,
                "save_trm": 1,
                "product": 2
            },
            {
                "id": 8,
                "fin_prdt_cd": "00320342",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.6,
                "save_trm": 3,
                "product": 2
            },
            {
                "id": 9,
                "fin_prdt_cd": "00320342",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.6,
                "save_trm": 6,
                "product": 2
            },
            {
                "id": 10,
                "fin_prdt_cd": "00320342",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.7,
                "save_trm": 12,
                "product": 2
            }
        ],
        "fin_prdt_cd": "00320342",
        "kor_co_nm": "한국스탠다드차타드은행",
        "fin_prdt_nm": "e-그린세이브예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 3,
        "depositoptions_set": [
            {
                "id": 11,
                "fin_prdt_cd": "10511008000996000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.46,
                "intr_rate2": 3.11,
                "save_trm": 6,
                "product": 3
            },
            {
                "id": 12,
                "fin_prdt_cd": "10511008000996000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.85,
                "save_trm": 12,
                "product": 3
            },
            {
                "id": 13,
                "fin_prdt_cd": "10511008000996000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.22,
                "intr_rate2": 3.87,
                "save_trm": 24,
                "product": 3
            },
            {
                "id": 14,
                "fin_prdt_cd": "10511008000996000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.24,
                "intr_rate2": 3.89,
                "save_trm": 36,
                "product": 3
            }
        ],
        "fin_prdt_cd": "10511008000996000",
        "kor_co_nm": "대구은행",
        "fin_prdt_nm": "DGB주거래우대예금(첫만남고객형)",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 5,
        "depositoptions_set": [
            {
                "id": 20,
                "fin_prdt_cd": "10511008001166004",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.7,
                "intr_rate2": 4.15,
                "save_trm": 12,
                "product": 5
            }
        ],
        "fin_prdt_cd": "10511008001166004",
        "kor_co_nm": "대구은행",
        "fin_prdt_nm": "DGB함께예금",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 6,
        "depositoptions_set": [
            {
                "id": 21,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.2,
                "intr_rate2": 2.25,
                "save_trm": 1,
                "product": 6
            },
            {
                "id": 22,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.4,
                "intr_rate2": 2.45,
                "save_trm": 3,
                "product": 6
            },
            {
                "id": 23,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.25,
                "intr_rate2": 3.5,
                "save_trm": 6,
                "product": 6
            },
            {
                "id": 24,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.65,
                "save_trm": 12,
                "product": 6
            },
            {
                "id": 25,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.45,
                "save_trm": 24,
                "product": 6
            },
            {
                "id": 26,
                "fin_prdt_cd": "10511008001278000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.45,
                "save_trm": 36,
                "product": 6
            }
        ],
        "fin_prdt_cd": "10511008001278000",
        "kor_co_nm": "대구은행",
        "fin_prdt_nm": "IM스마트예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 7,
        "depositoptions_set": [
            {
                "id": 27,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.25,
                "intr_rate2": 2.25,
                "save_trm": 1,
                "product": 7
            },
            {
                "id": 28,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.45,
                "intr_rate2": 3.4,
                "save_trm": 3,
                "product": 7
            },
            {
                "id": 29,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.55,
                "intr_rate2": 3.4,
                "save_trm": 6,
                "product": 7
            },
            {
                "id": 30,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.75,
                "intr_rate2": 3.4,
                "save_trm": 12,
                "product": 7
            },
            {
                "id": 31,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.8,
                "intr_rate2": 2.8,
                "save_trm": 24,
                "product": 7
            },
            {
                "id": 32,
                "fin_prdt_cd": "01030500510002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.8,
                "intr_rate2": 2.8,
                "save_trm": 36,
                "product": 7
            }
        ],
        "fin_prdt_cd": "01030500510002",
        "kor_co_nm": "부산은행",
        "fin_prdt_nm": "LIVE정기예금",
        "join_deny": 1,
        "join_way": "영업점,인터넷",
        "spcl_cnd": ""
    },
    {
        "id": 8,
        "depositoptions_set": [
            {
                "id": 33,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.2,
                "intr_rate2": 2.85,
                "save_trm": 1,
                "product": 8
            },
            {
                "id": 34,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.75,
                "intr_rate2": 3.4,
                "save_trm": 3,
                "product": 8
            },
            {
                "id": 35,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.65,
                "save_trm": 6,
                "product": 8
            },
            {
                "id": 36,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.65,
                "save_trm": 12,
                "product": 8
            },
            {
                "id": 37,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.25,
                "intr_rate2": 2.9,
                "save_trm": 24,
                "product": 8
            },
            {
                "id": 38,
                "fin_prdt_cd": "01030500560002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 1.95,
                "intr_rate2": 2.6,
                "save_trm": 36,
                "product": 8
            }
        ],
        "fin_prdt_cd": "01030500560002",
        "kor_co_nm": "부산은행",
        "fin_prdt_nm": "더(The) 특판 정기예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 9,
        "depositoptions_set": [
            {
                "id": 39,
                "fin_prdt_cd": "TD11300027000",
                "intr_rate_type_nm": "복리",
                "intr_rate": 3.39,
                "intr_rate2": 3.59,
                "save_trm": 12,
                "product": 9
            },
            {
                "id": 40,
                "fin_prdt_cd": "TD11300027000",
                "intr_rate_type_nm": "복리",
                "intr_rate": 3.37,
                "intr_rate2": 3.57,
                "save_trm": 24,
                "product": 9
            },
            {
                "id": 41,
                "fin_prdt_cd": "TD11300027000",
                "intr_rate_type_nm": "복리",
                "intr_rate": 3.32,
                "intr_rate2": 3.52,
                "save_trm": 36,
                "product": 9
            }
        ],
        "fin_prdt_cd": "TD11300027000",
        "kor_co_nm": "광주은행",
        "fin_prdt_nm": "미즈월복리정기예금",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰,기타",
        "spcl_cnd": ""
    },
    {
        "id": 10,
        "depositoptions_set": [
            {
                "id": 42,
                "fin_prdt_cd": "TD11300031000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.07,
                "intr_rate2": 3.17,
                "save_trm": 1,
                "product": 10
            },
            {
                "id": 43,
                "fin_prdt_cd": "TD11300031000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.16,
                "intr_rate2": 3.26,
                "save_trm": 3,
                "product": 10
            },
            {
                "id": 44,
                "fin_prdt_cd": "TD11300031000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.22,
                "intr_rate2": 3.32,
                "save_trm": 6,
                "product": 10
            },
            {
                "id": 45,
                "fin_prdt_cd": "TD11300031000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.29,
                "intr_rate2": 3.49,
                "save_trm": 12,
                "product": 10
            },
    {
        "id": 12,
        "depositoptions_set": [
            {
                "id": 49,
                "fin_prdt_cd": "TD11300036000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.4,
                "save_trm": 3,
                "product": 12
            },
            {
                "id": 50,
                "fin_prdt_cd": "TD11300036000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.45,
                "intr_rate2": 3.45,
                "save_trm": 6,
                "product": 12
            },
            {
                "id": 51,
                "fin_prdt_cd": "TD11300036000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.45,
                "intr_rate2": 3.45,
                "save_trm": 12,
                "product": 12
            }
        ],
        "fin_prdt_cd": "TD11300036000",
        "kor_co_nm": "광주은행",
        "fin_prdt_nm": "The플러스예금",
        "join_deny": 1,
        "join_way": "영업점,스마트폰",
        "spcl_cnd": "▶ 해당사항없음"
    },
    {
        "id": 13,
        "depositoptions_set": [
            {
                "id": 52,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.3,
                "intr_rate2": 3.2,
                "save_trm": 1,
                "product": 13
            },
            {
                "id": 53,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.6,
                "intr_rate2": 3.5,
                "save_trm": 3,
                "product": 13
            },
            {
                "id": 54,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.7,
                "save_trm": 6,
                "product": 13
            },
            {
                "id": 55,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.1,
                "intr_rate2": 3.75,
                "save_trm": 12,
                "product": 13
            },
            {
                "id": 56,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.5,
                "save_trm": 24,
                "product": 13
            },
            {
                "id": 57,
                "fin_prdt_cd": "101272000057",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.5,
                "save_trm": 36,
                "product": 13
            }
        ],
        "fin_prdt_cd": "101272000057",
        "kor_co_nm": "제주은행",
        "fin_prdt_nm": "J정기예금\n(만기지급식)",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 15,
        "depositoptions_set": [
            {
                "id": 61,
                "fin_prdt_cd": "10-01-20-024-0046-0000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.5,
                "save_trm": 3,
                "product": 15
            },
            {
                "id": 62,
                "fin_prdt_cd": "10-01-20-024-0046-0000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.55,
                "intr_rate2": 3.55,
                "save_trm": 6,
                "product": 15
            },
            {
                "id": 63,
                "fin_prdt_cd": "10-01-20-024-0046-0000",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.4,
                "save_trm": 12,
                "product": 15
            }
        ],
        "fin_prdt_cd": "10-01-20-024-0046-0000",
        "kor_co_nm": "전북은행",
        "fin_prdt_nm": "JB 다이렉트예금통장\n(만기일시지급식)",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 18,
        "depositoptions_set": [
            {
                "id": 71,
                "fin_prdt_cd": "21001203",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.15,
                "intr_rate2": 3.45,
                "save_trm": 6,
                "product": 18
            },
            {
                "id": 72,
                "fin_prdt_cd": "21001203",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.7,
                "save_trm": 12,
                "product": 18
            },
            {
                "id": 73,
                "fin_prdt_cd": "21001203",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.45,
                "intr_rate2": 3.75,
                "save_trm": 24,
                "product": 18
            }
        ],
        "fin_prdt_cd": "21001203",
        "kor_co_nm": "경남은행",
        "fin_prdt_nm": "BNK주거래우대정기예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 21,
        "depositoptions_set": [
            {
                "id": 80,
                "fin_prdt_cd": "01211310121",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.45,
                "intr_rate2": 3.65,
                "save_trm": 12,
                "product": 21
            },
            {
                "id": 81,
                "fin_prdt_cd": "01211310121",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.7,
                "save_trm": 24,
                "product": 21
            },
            {
                "id": 82,
                "fin_prdt_cd": "01211310121",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.6,
                "intr_rate2": 3.8,
                "save_trm": 36,
                "product": 21
            }
        ],
        "fin_prdt_cd": "01211310121",
        "kor_co_nm": "중소기업은행",
        "fin_prdt_nm": "IBK평생한가족통장(실세금리정기예금)",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰",
        "spcl_cnd": ""
    },
    {
        "id": 22,
        "depositoptions_set": [
            {
                "id": 83,
                "fin_prdt_cd": "01211310130",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.33,
                "intr_rate2": 3.33,
                "save_trm": 6,
                "product": 22
            },
            {
                "id": 84,
                "fin_prdt_cd": "01211310130",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.32,
                "intr_rate2": 3.32,
                "save_trm": 12,
                "product": 22
            },
            {
                "id": 85,
                "fin_prdt_cd": "01211310130",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.33,
                "intr_rate2": 3.33,
                "save_trm": 24,
                "product": 22
            },
            {
                "id": 86,
                "fin_prdt_cd": "01211310130",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.31,
                "intr_rate2": 3.31,
                "save_trm": 36,
                "product": 22
            }
        ],
        "fin_prdt_cd": "01211310130",
        "kor_co_nm": "중소기업은행",
        "fin_prdt_nm": "1석7조통장(정기예금)",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": "없음"
    },
    {
        "id": 23,
        "depositoptions_set": [
            {
                "id": 87,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 23
            },
            {
                "id": 88,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.1,
                "intr_rate2": 3.1,
                "save_trm": 3,
                "product": 23
            },
            {
                "id": 89,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.4,
                "save_trm": 6,
                "product": 23
            },
            {
                "id": 90,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.5,
                "save_trm": 12,
                "product": 23
            },
            {
                "id": 91,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.35,
                "intr_rate2": 3.35,
                "save_trm": 24,
                "product": 23
            },
            {
                "id": 92,
                "fin_prdt_cd": "06492",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.35,
                "intr_rate2": 3.35,
                "save_trm": 36,
                "product": 23
            }
        ],
        "fin_prdt_cd": "06492",
        "kor_co_nm": "한국산업은행",
        "fin_prdt_nm": "KDB 정기예금",
        "join_deny": 1,
        "join_way": "영업점,인터넷,스마트폰",
        "spcl_cnd": "해당없음"
    },
    {
        "id": 24,
        "depositoptions_set": [
            {
                "id": 93,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 1.8,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 24
            },
            {
                "id": 94,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.2,
                "intr_rate2": 3.45,
                "save_trm": 3,
                "product": 24
            },
            {
                "id": 95,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.3,
                "intr_rate2": 3.45,
                "save_trm": 6,
                "product": 24
            },
            {
                "id": 96,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.6,
                "intr_rate2": 3.5,
                "save_trm": 12,
                "product": 24
            },
            {
                "id": 97,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.7,
                "intr_rate2": 2.8,
                "save_trm": 24,
                "product": 24
            },
            {
                "id": 98,
                "fin_prdt_cd": "010300100335",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.8,
                "intr_rate2": 2.8,
                "save_trm": 36,
                "product": 24
            }
        ],
        "fin_prdt_cd": "010300100335",
        "kor_co_nm": "국민은행",
        "fin_prdt_nm": "KB Star 정기예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": "해당무"
    },
    {
        "id": 25,
        "depositoptions_set": [
            {
                "id": 99,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.15,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 25
            },
            {
                "id": 100,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.45,
                "intr_rate2": 3.45,
                "save_trm": 3,
                "product": 25
            },
            {
                "id": 101,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.75,
                "intr_rate2": 3.5,
                "save_trm": 6,
                "product": 25
            },
            {
                "id": 102,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.9,
                "intr_rate2": 3.5,
                "save_trm": 12,
                "product": 25
            },
            {
                "id": 103,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.95,
                "intr_rate2": 3.0,
                "save_trm": 24,
                "product": 25
            },
            {
                "id": 104,
                "fin_prdt_cd": "200-0135-12",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 36,
                "product": 25
            }
        ],
        "fin_prdt_cd": "200-0135-12",
        "kor_co_nm": "신한은행",
        "fin_prdt_nm": "쏠편한 정기예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": "해당사항없음"
    },
    {
        "id": 28,
        "depositoptions_set": [
            {
                "id": 112,
                "fin_prdt_cd": "10-003-1384-0001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 28
            },
            {
                "id": 113,
                "fin_prdt_cd": "10-003-1384-0001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.45,
                "intr_rate2": 3.45,
                "save_trm": 3,
                "product": 28
            },
            {
                "id": 114,
                "fin_prdt_cd": "10-003-1384-0001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.6,
                "intr_rate2": 3.6,
                "save_trm": 12,
                "product": 28
            },
            {
                "id": 115,
                "fin_prdt_cd": "10-003-1384-0001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.23,
                "intr_rate2": 3.23,
                "save_trm": 24,
                "product": 28
            },
            {
                "id": 116,
                "fin_prdt_cd": "10-003-1384-0001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.4,
                "intr_rate2": 3.4,
                "save_trm": 36,
                "product": 28
            }
        ],
        "fin_prdt_cd": "10-003-1384-0001",
        "kor_co_nm": "농협은행주식회사",
        "fin_prdt_nm": "NH올원e예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": "없음"
    },
    {
        "id": 30,
        "depositoptions_set": [
            {
                "id": 118,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.0,
                "intr_rate2": 3.0,
                "save_trm": 1,
                "product": 30
            },
            {
                "id": 119,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.2,
                "intr_rate2": 3.45,
                "save_trm": 3,
                "product": 30
            },
            {
                "id": 120,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.3,
                "intr_rate2": 3.45,
                "save_trm": 6,
                "product": 30
            },
            {
                "id": 121,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.6,
                "intr_rate2": 3.5,
                "save_trm": 12,
                "product": 30
            },
            {
                "id": 122,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.7,
                "intr_rate2": 3.0,
                "save_trm": 24,
                "product": 30
            },
            {
                "id": 123,
                "fin_prdt_cd": "4",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.8,
                "intr_rate2": 3.0,
                "save_trm": 36,
                "product": 30
            }
        ],
        "fin_prdt_cd": "4",
        "kor_co_nm": "하나은행",
        "fin_prdt_nm": "하나의정기예금",
        "join_deny": 1,
        "join_way": "스마트폰",
        "spcl_cnd": "해당사항없음"
    },
    {
        "id": 31,
        "depositoptions_set": [
            {
                "id": 124,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.05,
                "intr_rate2": 3.05,
                "save_trm": 1,
                "product": 31
            },
            {
                "id": 125,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.5,
                "intr_rate2": 3.5,
                "save_trm": 3,
                "product": 31
            },
            {
                "id": 126,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.55,
                "intr_rate2": 3.55,
                "save_trm": 6,
                "product": 31
            },
            {
                "id": 127,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.55,
                "intr_rate2": 3.55,
                "save_trm": 12,
                "product": 31
            },
            {
                "id": 128,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.2,
                "save_trm": 24,
                "product": 31
            },
            {
                "id": 129,
                "fin_prdt_cd": "01013000110000000001",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.2,
                "save_trm": 36,
                "product": 31
            }
        ],
        "fin_prdt_cd": "01013000110000000001",
        "kor_co_nm": "주식회사 케이뱅크",
        "fin_prdt_nm": "코드K 정기예금",
        "join_deny": 1,
        "join_way": "스마트폰",
        "spcl_cnd": "우대조건 없음"
    },

    {
        "id": 34,
        "depositoptions_set": [
            {
                "id": 133,
                "fin_prdt_cd": "10120114700011",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.65,
                "intr_rate2": 3.65,
                "save_trm": 3,
                "product": 34
            },
            {
                "id": 134,
                "fin_prdt_cd": "10120114700011",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.65,
                "intr_rate2": 3.65,
                "save_trm": 6,
                "product": 34
            },
            {
                "id": 135,
                "fin_prdt_cd": "10120114700011",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.65,
                "intr_rate2": 3.65,
                "save_trm": 12,
                "product": 34
            }
        ],
        "fin_prdt_cd": "10120114700011",
        "kor_co_nm": "수협은행",
        "fin_prdt_nm": "헤이(Hey)정기예금",
        "join_deny": 1,
        "join_way": "인터넷,스마트폰",
        "spcl_cnd": "없음"
    },
    {
        "id": 36,
        "depositoptions_set": [
            {
                "id": 137,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 2.7,
                "intr_rate2": 2.7,
                "save_trm": 1,
                "product": 36
            },
            {
                "id": 138,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.2,
                "intr_rate2": 3.2,
                "save_trm": 3,
                "product": 36
            },
            {
                "id": 139,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.3,
                "intr_rate2": 3.3,
                "save_trm": 6,
                "product": 36
            },
            {
                "id": 140,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.3,
                "intr_rate2": 3.3,
                "save_trm": 12,
                "product": 36
            },
            {
                "id": 141,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 24,
                "product": 36
            },
            {
                "id": 142,
                "fin_prdt_cd": "10-01-20-388-0002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 36,
                "product": 36
            }
        ],
        "fin_prdt_cd": "10-01-20-388-0002",
        "kor_co_nm": "주식회사 카카오뱅크",
        "fin_prdt_nm": "카카오뱅크 정기예금",
        "join_deny": 1,
        "join_way": "스마트폰",
        "spcl_cnd": "※복잡한 우대조건 없이 가입가능한 정기예금"
    },
    {
        "id": 37,
        "depositoptions_set": [
            {
                "id": 143,
                "fin_prdt_cd": "1001202000002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 3,
                "product": 37
            },
            {
                "id": 144,
                "fin_prdt_cd": "1001202000002",
                "intr_rate_type_nm": "단리",
                "intr_rate": 3.0,
                "intr_rate2": 3.0,
                "save_trm": 6,
                "product": 37
            }
        ],
        "fin_prdt_cd": "1001202000002",
        "kor_co_nm": "토스뱅크 주식회사",
        "fin_prdt_nm": "토스뱅크 먼저 이자 받는 정기예금",
        "join_deny": 1,
        "join_way": "스마트폰",
        "spcl_cnd": "우대조건 없음"
    }
] 당신은 원하는 예금 상품들에 대한 정보를 받아 조건에 맞는 예금 상품을 추천 해 줄 수 있어야 합니다. 예를 들어 6개월 기간의 최고우대금리가 가장 높은 상품을 추천받고 싶다고 했을때, 당신은 depositoptions_set을 돌며, save_trm이 6인 option의 intr_rate2가 가장 높은 상품을 추천해 주어야 합니다. 다음은 개월수 별로 최고우대금리가 가장 높은 상품들입니다. save_trm이 6인 intr_rate2가 가장 높은 상품은 수협은행의 sh해양플라스틱Zero!예금 입니다. 따라서 당신은 6개월 기간의 최고우대금리가 가장 높은 상품을 추천해달라고 했을때, 수협은행의 sh해양플라스틱Zero!예금을 추천해 주어야 합니다. 12개월의 최고우대금리가 가장 높은 상품은 DGB함께예금입니다. 24개월의 최고우대금리가 가장 높은 상품은 수협은행의 sh해양플라스틱Zero!예금입니다. 36개월의 최고우대금리가 가장 높은 상품은 수협은행의 sh해양플라스틱Zero!예금입니다.  다음은 개월수 별로 저축금리가 가장 높은 상품들입니다. 당신은 반드시 최대우대금리와 저축금리를 잘 구분해야 합니다. 6개월 - 수협은행의 헤이(Hey)정기예금 12개월 - 대구은행 DGB함께예금 24개월 - 중소기업은행 IBK평생한가족통장(실세금리정기예금) 36개월 - 중소기업은행 IBK평생한가족통장(실세금리정기예금)"""},
    ]
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def usercommand(request):
    command = request.data['command']
    context.append({'role':'user', 'content' : command})
    response = get_completion_from_messages(context, model="gpt-3.5-turbo", temperature=0.7)
    context.append({'role' : 'assistant', 'content' : response})
    return Response({'response' : response})
