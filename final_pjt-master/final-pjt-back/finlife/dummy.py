import json
from collections import OrderedDict
from itertools import product

# 데이터 생성 함수
def generate_combinations():
    # 각 필드의 가능한 값 정의
    gen_combinations = [(True, False), (False, True)]  # 성별 필드 (남성, 여성)
    age_combinations = [(False, False, False, False, False, False) for _ in range(6)]
    sal_combinations = [(False, False, False, False, False, False) for _ in range(6)]
    whl_combinations = [(False, False, False, False, False, False) for _ in range(6)]
    ten_combinations = [(False, False, False) for _ in range(3)]

    for i in range(6):
        age_combinations[i] = age_combinations[i][:i] + (True,) + age_combinations[i][i+1:]
        sal_combinations[i] = sal_combinations[i][:i] + (True,) + sal_combinations[i][i+1:]
        whl_combinations[i] = whl_combinations[i][:i] + (True,) + whl_combinations[i][i+1:]

    for i in range(3):
        ten_combinations[i] = ten_combinations[i][:i] + (True,) + ten_combinations[i][i+1:]

    # 모든 조합을 생성
    all_combinations = list(product(gen_combinations, age_combinations, sal_combinations, whl_combinations, ten_combinations))

    data = []
    
    for i, (gen, age, sal, whl, ten) in enumerate(all_combinations):
        fields = {}

        # 성별 필드 (남성, 여성)
        fields['gen_one'] = gen[0]
        fields['gen_two'] = gen[1]

        # 나이, 연봉, 자산 필드 (6단계)
        for key, comb in zip(['age', 'sal', 'whl'], [age, sal, whl]):
            for j, value in enumerate(comb):
                fields[f'{key}_{["one", "two", "thr", "fou", "fiv", "six"][j]}'] = value

        # 성향 필드 (3단계)
        for j, value in enumerate(ten):
            fields[f'ten_{["one", "two", "thr"][j]}'] = value

        # 모델 및 pk 설정
        model_data = OrderedDict()
        model_data["model"] = "finlife.anonymous"
        model_data["pk"] = i + 1
        model_data["fields"] = fields

        data.append(model_data)

    return data

# 데이터 생성 및 저장
dummy_data = generate_combinations()

# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = './dummy_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    json.dump(dummy_data, f, ensure_ascii=False, indent=2)

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')
