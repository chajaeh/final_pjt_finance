from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserUpdateSerializer
import json
from .models import User
from heapq import heappop, heappush
from finance.models import DepositProducts, LoanProducts, LoanOptions
from articles.models import Article, Comment

@api_view(['PUT'])
def update_detail(request):
  user = request.user
  serializer = UserUpdateSerializer(user, data=request.data, partial=True)
  if serializer.is_valid(raise_exception=True):
    serializer.save()
    return Response(serializer.data,status=status.HTTP_200_OK)
  
@api_view(['PUT'])
def add_deposit(request):
  user = request.user
  if user.financial_products == '':
    financial_products = user.financial_products + request.data['fin_prdt_cd']
  else:
    financial_products = user.financial_products + ', ' + request.data['fin_prdt_cd']
  serializer = UserUpdateSerializer(user, data={'financial_products' : financial_products}, partial=True)
  if serializer.is_valid(raise_exception=True):
    print(serializer)
    serializer.save()
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def recommend(request):
    current_user = request.user
    age = current_user.age
    asset = current_user.asset
    salary = current_user.salary
    users = User.objects.all()
    products_dict = {}
    for user in users:
      if user.financial_products != "":
        financial_products = user.financial_products.split(',')
        if 0.9 * age <= user.age <= 1.1 * age:
          for product_code in financial_products:
            product_code = product_code.strip() 
            if product_code not in products_dict:
              products_dict[product_code] = 1
            else:
              products_dict[product_code] += 1
        if 0.9 * asset <= user.asset <= 1.1 * asset:
          for product_code in financial_products:
            product_code = product_code.strip() 
            if product_code not in products_dict:
              products_dict[product_code] = 1
            else:
              products_dict[product_code] += 1
        if 0.9 * salary <= user.salary <= 1.1 * salary:
          for product_code in financial_products:
            product_code = product_code.strip() 
            if product_code not in products_dict:
              products_dict[product_code] = 1
            else:
              products_dict[product_code] += 1
    pq = []          
    for (key, value) in products_dict.items():
      heappush(pq, (-value, key))
    result = []
    for i in range(10):
      if pq:
        count, fin_prdt_cd = heappop(pq)
        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        result.append({'fin_prdt_nm' : product.fin_prdt_nm, 'fin_prdt_cd' : fin_prdt_cd})
    return Response(result)

@api_view(['POST'])
def recommend_loan(request):
  credit_agency = request.data['creditAgency']
  credit_grade = request.data['creditGrade']
  options = LoanOptions.objects.all()
  standard = []
  subtraction = []
  for option in options:
    if option.product.cb_name == credit_agency:
      if option.crdt_lend_rate_type_nm == '기준금리':
        grade_value = getattr(option, credit_grade, None)
        if grade_value != -1:
          heappush(standard, (grade_value, option.id))
      if option.crdt_lend_rate_type_nm == '가감조정금리':
        grade_value = getattr(option, credit_grade, None)
        if grade_value != -1:
          dictionary = {option.product.kor_co_nm : (grade_value, option.id)}
          check = False
          for dictionaries in subtraction:
            [company_name] = dictionaries.keys()
            [(grade_val, option_id)] = dictionaries.values()
            if company_name == option.product.kor_co_nm and grade_value < grade_val:
              subtraction.remove(dictionaries)
              subtraction.append(dictionary)
              check = True
              break
            elif company_name == option.product.kor_co_nm and grade_value >= grade_val:
              check = True
              break
          if not check:
            subtraction.append(dictionary)
  stand = heappop(standard)
  stand_interest_current_grade = stand[0]
  stand_option_id = stand[1]
  stand_option = LoanOptions.objects.get(id = stand_option_id)
  stand_company_name = stand_option.product.kor_co_nm
  stand_product_name = stand_option.product.fin_prdt_nm
  stand_interest_average = stand_option.crdt_grad_avg
  standard_object = { 'interest_current_grade' : stand_interest_current_grade, 'company_name' : stand_company_name, 'product_name' : stand_product_name, 'interest_average' : stand_interest_average }
  subtraction_list = []
  for dictionaries in subtraction:
    [company_name] = dictionaries.keys()
    [(grade_val, option_id)] = dictionaries.values()
    subt_option = LoanOptions.objects.get(id=option_id)
    subt_interest_current_grade = grade_val
    subt_company_name = subt_option.product.kor_co_nm
    subt_product_name = subt_option.product.fin_prdt_nm
    subt_interest_average = subt_option.crdt_grad_avg
    subtraction_object = { 'interest_current_grade' : subt_interest_current_grade, 'company_name' : subt_company_name, 'product_name' : subt_product_name, 'interest_average' : subt_interest_average }
    subtraction_list.append(subtraction_object)
  return Response({'standard' : standard_object, 'subtraction' : subtraction_list})


@api_view(['POST'])
def warn(request):
  user = request.user
  user.warned += 1
  user.save()
  return Response({'warn':user.warned},status=status.HTTP_200_OK)

@api_view(['POST'])
def warn_signout(request):
  user = request.user
  signout_user = User.objects.get(username = '탈퇴한 유저')
  user_articles = Article.objects.filter(user = user)
  user_comments = Comment.objects.filter(user = user)
  for article in user_articles:
    article.user = signout_user
    article.save()
  for comment in user_comments:
    comment.user = signout_user
    comment.save()
    print(comment.user)
  user.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)