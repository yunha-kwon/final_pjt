import random
from .models import SaveProducts, DepositProducts
from django.db.models import Q

def recommend_save_products(user):
    products = SaveProducts.objects.all()

    # 모든 조건을 만족하는 상품 필터링
    filters = Q()

    # 나이 조건
    if user.age_one or user.age_two:
        filters |= (Q(save_options__save_trm__lt=24) &
                    Q(fin_prdt_nm__icontains='DREAM') | 
                    Q(fin_prdt_nm__icontains='Dream') |
                    Q(fin_prdt_nm__icontains='자유해지') | 
                    Q(fin_prdt_nm__icontains='첫') | 
                    Q(fin_prdt_nm__icontains='꿈'))
    elif user.age_thr or user.age_fou or user.age_fiv:
        filters |= Q(save_options__save_trm__gte=12)
    elif user.age_six:
        filters |= Q(join_way__icontains='영업점')

    # 연봉 조건
    if user.sal_one or user.sal_two:
        filters |= (Q(save_options__save_trm__lt=12) & Q(save_options__rsrv_type_nm='자유적립식'))

    # 자산 조건
    if user.whl_one or user.whl_two:
        filters |= (Q(save_options__save_trm__lt=12)  & Q(save_options__rsrv_type_nm='자유적립식'))
    elif user.whl_thr or user.whl_fou or user.whl_five or user.whl_six:
        filters |= (Q(save_options__save_trm__gte=12) & Q(save_options__rsrv_type_nm='정액적립식'))

    # 저축 성향 조건
    if user.ten_one:
        filters |= Q(save_options__save_trm__lte=6)
    elif user.ten_two:
        filters |= Q(save_options__save_trm__gt=6, save_options__save_trm__lt=24)
    elif user.ten_thr:
        filters |= Q(save_options__save_trm__gte=24)

    products = products.filter(filters)

    # 랜덤으로 10개 상품 추출
    recommended_products = random.sample(list(products), min(len(products), 5))

    return recommended_products


def recommend_deposit_products(user):
    products = DepositProducts.objects.all()

    # 나이 조건
    age_filter = Q()
    if user.age_one or user.age_two:
        age_filter |= (Q(deposit_options__save_trm__lt=24) &
                    Q(fin_prdt_nm__icontains='DREAM') | 
                    Q(fin_prdt_nm__icontains='Dream') | 
                    Q(fin_prdt_nm__icontains='자유해지') | 
                    Q(fin_prdt_nm__icontains='첫') | 
                    Q(fin_prdt_nm__icontains='꿈'))
    elif user.age_thr or user.age_fou or user.age_fiv:
        age_filter |= Q(deposit_options__save_trm__gte=12)
    elif user.age_six:
        age_filter |= Q(join_way__icontains='영업점')
        

    # 연봉 조건
    salary_filter = Q()
    if user.sal_one or user.sal_two:
        salary_filter |= (Q(deposit_options__save_trm__lt=12))

    # 자산 조건
    wealth_filter = Q()
    if user.whl_one or user.whl_two:
        wealth_filter |= Q(deposit_options__save_trm__lt=12)
    elif user.whl_thr or user.whl_fou or user.whl_five or user.whl_six:
        wealth_filter |= Q(deposit_options__save_trm__gte=12)

    # 저축 성향 조건
    tendency_filter = Q()
    if user.ten_one:
        tendency_filter |= Q(deposit_options__save_trm__lte=6)
    elif user.ten_two:
        tendency_filter |= Q(deposit_options__save_trm__gt=6, deposit_options__save_trm__lt=24)
    elif user.ten_thr:
        tendency_filter |= Q(deposit_options__save_trm__gte=24)

    # # 모든 조건을 만족하는 상품 필터링
    # products = products.filter(age_filter & salary_filter & wealth_filter & tendency_filter)

    # 랜덤으로 10개 상품 추출
    recommended_products = random.sample(list(products), min(len(products), 5))

    return recommended_products
