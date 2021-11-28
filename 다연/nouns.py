import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == '__main__':
    t_file_name=open('C:/Users/USER/Desktop/Contents_List.txt','r',encoding='utf-8')
    # contents 리스트를 불러와 title_list변수에 저장
    title_list=[]
    for line in t_file_name.readlines():
        title_list.append(line[:-1])
    t_file_name.close()
    
    dataset=pd.read_csv("C:/Users/USER/Desktop/pre_도쿄(네이버).csv")
    
    # 형태소별로 분류
    tagger=Okt()
    
    for title in title_list:
        # 각 타이틀에 대한 341개 문서의 DTM을 표현하기 위해 객체 선언
        cv=CountVectorizer() 
        # 각 문서들의 말뭉치를 저장할 리스트 선언
        corpus=[] 
        
        for doc_num in range(341):
            # 각 말뭉치에서 명사 리스트를 만든다
            noun_list=tagger.nouns(dataset['title'].loc[doc_num])
            # 문자열로 저장해야하기 때문에 join함수로 공백을 구분해 corpus에 append한다.
            corpus.append(' '.join(noun_list))
            # fit_transform 함수를 통해 DTM을 한번에 생성
            DTM_Array=cv.fit_transform(corpus).toarray()
            # feature_names 함수를 통해 DTM의 각 열이 어떤 단어에 해당하는지 알 수 있다
            feature_names=cv.get_feature_names()
            
            # 추출해낸 데이터를 DataFrame 형식으로 변환
            DTM_DataFrame=pd.DataFrame(DTM_Array, columns=feature_names)
            
            #최종적으로 DTM을 csv파일로 저장
            DTM_DataFrame.to_csv("C:/Users/USER/Desktop/DTM.csv", encoding='utf-8-sig')
