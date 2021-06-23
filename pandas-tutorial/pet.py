#%%

#1.판다스와 넘파이 임포트하기
import pandas as pd
import numpy as np
from icecream import ic
class Pet(object):

        @staticmethod
        def quiz_2():
                #2. 판다스 버전출력
                ic(pd.__version__)

        @staticmethod
        def quiz_3():
                pass







if __name__ == '__main__':
        p = Pet()
        while 1:
                menu = input('2. 판다스 버전출력\n'
                '3. 판다스 라이브러리 버전 정보 모두 출력\n'
                '4. 주어진 값으로 DataFrame 객체를 생성하시오.\n'
                '5. 객체 상위 3열 까지 출력객체 내부 정보를 출력\n'
                '6.  r객체 상위 3열 까지 출력\n'
                '7. animal과 age 컬럼만 출력\n'
                '8. rorcpdml 3,4,8번 행에 해당하는 animal과 age 값만 출력\n'
                '9. visit 컬럼에서 2초과하는 값 출력\n'
                '10. age에서 NAN 값 출력\n'
                '11. age가 3살 미만 고양이 값 출력\n'
                '12. age가 2살 이상 4살 미만인 값 출력\n'
                '13. f행의 나이를 1.5살로 변경\n'
                '14. 객체 visit의 합 출력\n'
                '15. 동물별로 나이의 평균 출력\n'
                '16. k행을 추가하여 dog , 5.5세, 우선권없음(no), 방문회수 2회 열을 추가\n'
                '16-1. 방금 추가한 열 삭제\n'
                '17. 객체에 있는 동물의 종류의 수 출력\n'
                '18. age 는 내림차순, visits 는 오름차순으로 정렬\n'
                '19. priority 의 yes를 True, no 를 False  로 맵핑 후 출력\n'
                '20. snake 를 python 으로 값을 변경\n'
                '')

                if menu == '0':
                        break

                elif menu == '1':
                        pass

                elif menu == '2':
                        p.quiz_2()

                elif menu == '3':
                        pass

                elif menu == '4':
                        pass

                elif menu == '5':
                        pass

                elif menu == '6':
                        pass
                elif menu == '7':
                        pass

                elif menu == '8':
                        pass
                elif menu == '9':
                        pass

                elif menu == '10':
                        pass

                elif menu == '11':
                        pass

                elif menu == '12':
                        pass
                elif menu == '13':
                        pass
                elif menu == '14':
                        pass

                elif menu == '15':
                        pass

                elif menu == '16':
                        pass
                elif menu == '17':
                        pass

                elif menu == '18':
                        pass
                elif menu == '19':
                        pass

                elif menu == '20':
                        pass
                else:
                        print('Wrong Number')

#%%

#2. 판다스 버전출력
pd.__version__


#%%

#3. 판다스 라이브러리 버전 정보 모두 출력
pd.show_versions()


#%%

#4. 주어진 값으로 DataFrame 객체를 생성하시오
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index = labels)
df

#%%

#5. 객체 내부 정보를 출력
df.describe()

#%%

#6. r객체 상위 3열 까지 출력
df.head(3)

#%%

#7. animal과 age 컬럼만 출력
df.loc[:,['animal','age']]

#%%

#8. rorcpdml 3,4,8번 행에 해당하는 animal과 age 값만 출력
df.iloc[[3,4,8],[1,2]] #df.loc.index[[3,4,8], ['age', 'animal']]


#%%

#9. visit 컬럼에서 2초과하는 값 출력
df[df['visits'] > 2]

#%%

#10. age에서 NAN 값 출력
df[df['age'].isnull()]

#%%

#11. age가 3살 미만 고양이 값 출력
#df['age'][df['age']< 3]
df[(df['age']<3) & (df['animal'] == 'cat')]

#%%

#12. age가 2살 이상 4살 미만인 값 출력
df[df['age'].between(2,4)]


#%%

#13. f행의 나이를 1.5살로 변경
df.loc['f','age'] = 1.5

#%%

#14. 객체 visit의 합 출력
df['visits'].sum()

#%%

#15. 동물별로 나이의 평균 출력
#df[df['animal']== 'cat'][['age']].mean()
df.groupby('animal')['age'].mean()

#%%

# 16. k행을 추가하여 dog , 5.5세, 우선권없음(no), 방문회수 2회 열을 추가
df.loc['k'] = ['dog', 5.5, 2, 'no']
df
#k = pd.DataFrame([['dog', 5.5, 2, 'no']],
#    index=['k'],
#    columns=['animal','visits', 'age', 'priority'])
#df = df.append(k)
#df

#%%

# 16. 방금 추가한 열 삭제
# df = df.drop(index='k', )
# df
df.drop('k', inplace=True)
# del df['k']
df

#%%

# 17. 객체에 있는 동물의 종류의 수 출력
# count = df['animal'].unique()
# print(len(count))
df['animal'].value_counts()

#%%

# 18. age 는 내림차순, visits 는 오름차순으로 정렬
#df['age'].sort_index(ascending=True)
df.sort_values(by=['age', 'visits'], ascending=[False, True])

#%%

df['visits'].sort_index(ascending=False)

#%%

# 19. priority 의 yes를 True, no 를 False  로 맵핑 후 출력
df['priority'] = df['priority'].map({'yes':True, 'no':False})
df

#%%

# 20. snake 를 python 으로 값을 변경
df['animal'] = df['animal'].replace('snake','python')
df

#%%

# 21. 각각의 동물 유형과 방문 횟수에 대해, 평균나이를 찾으시오.
# 즉,각 행은 animal 이고, 각 열은 visit 이며, 값은 평균연령
# (힌트, 피벗 테이블을 활용해야 함)
df = df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')
df

#%%


