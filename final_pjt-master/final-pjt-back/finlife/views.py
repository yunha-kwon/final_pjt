import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SaveOptionsSerializer, SaveProductsSerializer
from .models import DepositProducts, DepositOptions, SaveOptions, SaveProducts, Anonymous
from rest_framework import status
from .recommendations import recommend_save_products, recommend_deposit_products

api_key = settings.API_KEY
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    lst = ['020000', '030200', '030300']
    for i in lst:
        params = {
            'auth' : api_key,
            'topFinGrpNo' : i,
            'pageNo' : 1
        }
        response = requests.get(URL, params=params).json()   
        result = []
        res_data = response['result']
        baseList = res_data['baseList']
        optionList = res_data['optionList']        

        for bl in baseList:
            serializer = DepositProductsSerializer(data=bl)
            if serializer.is_valid():
                serializer.save()
                result.append(serializer)

        for ol in optionList:
            product = DepositProducts.objects.get(fin_prdt_cd=ol['fin_prdt_cd'])
            serializer = DepositOptionsSerializer(data=ol)
            if serializer.is_valid():
                serializer.save(product=product)
                result.append(serializer)

    return Response({'message': 'okay'})


@api_view(['GET'])
def save_save_products(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    lst = ['020000', '030200', '030300', '050000', '060000']
    for i in lst:
        params = {
            'auth' : api_key,
            'topFinGrpNo' : i,
            'pageNo' : 1
        }
        response = requests.get(URL, params=params).json()   
        result = []
        res_data = response['result']
        baseList = res_data['baseList']
        optionList = res_data['optionList']        
        for bl in baseList:
            serializer = SaveProductsSerializer(data=bl)
            if serializer.is_valid():
                serializer.save()
                result.append(serializer.data)
        for ol in optionList:
            product = SaveProducts.objects.filter(fin_prdt_cd=ol['fin_prdt_cd']).first()
            if product == None:
                continue
            serializer = SaveOptionsSerializer(data=ol)
            if serializer.is_valid():
                serializer.save(product=product)
                result.append(serializer.data)

    return Response({'message': 'okay'})


# 전체 정기예금 상품 목록 출력
@api_view(['GET'])
def deposit_products(request):
    products = DepositProducts.objects.all()
    serializers = DepositProductsSerializer(products, many=True)
    return Response(serializers.data)


# 특정 상품의 옵션 리스트 출력
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializers = DepositOptionsSerializer(options, many=True)
    return Response(serializers.data)


# 전체 적금 상품 목록 출력
@api_view(['GET'])
def save_products(request):
    products = SaveProducts.objects.all()
    serializers = SaveProductsSerializer(products, many=True)
    return Response(serializers.data)

# 특정 상품 옵션 리스트 출력
@api_view(['GET'])
def save_product_options(request, fin_prdt_cd):
    options = SaveOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializers = SaveOptionsSerializer(options, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def recommend_products(request, user_id):
    try:
        user = Anonymous.objects.get(pk=user_id)
        deposit_products = recommend_deposit_products(user)
        save_products = recommend_save_products(user)

        save_serializer = SaveProductsSerializer(save_products, many=True)
        deposit_serializer = DepositProductsSerializer(deposit_products, many=True)

        return Response({
            'id': user_id,
            'deposit_products': deposit_serializer.data,
            'save_products': save_serializer.data
        })
    
    except Anonymous.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)
    

def find_matching_ids(info, dummy_data):
    matching_id = 0
    
    for data in dummy_data:
        # print(data)
        is_match = True
        
        for key, value in info.items():
            if data.get(key) != value:
                is_match = False
                break
        if is_match:
            matching_id = (data['id'])
    
    return matching_id

@api_view(['POST'])
def update(request):
    if request.method == 'POST':
        data = request.data
        info = data.get('info')

        dummy_data = Anonymous.objects.values()  

        res = find_matching_ids(info, dummy_data)
        # print(res)

        return Response({"matching_id": res, "message": "Info received successfully"}, status=200)
    
    return Response({"message": "Info received successfully"}, status=200)

