import pandas as pd;

# 페이지 로딩 시 사용될 디폴트 메서드
def get_default_crime_branch_data():
    category = ['average','main', 'sub']
    dict_data = {}
    try:
        for i in range(0,3):     
            csv_data = pd.read_csv(f'./templates/crime_data/branch/2024/{category[i]}/crime_report_branch_1_2024_{category[i]}_crime_data.csv')
            df = pd.DataFrame(csv_data)
            df = sort_crime_data(df)
            
            df = df.astype(float)

            dict_data[category[i]] = df
        return dict_data       
    except Exception:
        print(FileNotFoundError)   
        return "FILE NOT FOUND"

# 페이지 로딩 시 사용될 디폴트 메서드 아규먼트 추가
def get_selected_crime_branch_data(year:str, branch:int ):
    category = ['average','main', 'sub']
    dict_data = {}
    try:
        for i in range(0,3):     
            csv_data = pd.read_csv(f'./templates/crime_data/branch/{year}/{category[i]}/crime_report_branch_{branch}_{year}_{category[i]}_crime_data.csv')
            df = pd.DataFrame(csv_data)
            df = sort_crime_data(df)
            
            df = df.astype(float)

            dict_data[category[i]] = df
        return dict_data       
    except Exception:
        print(FileNotFoundError)   
        return "FILE NOT FOUND"
 
        
# 인자 값에 따른 데이터 불러오기 메서드
def get_categorize_crime_branch(year:str, branch:int, category:str):
    dict_data = {}
    try:
        csv_data = pd.read_csv(f'./templates/crime_data/branch/{year}/{category}/crime_report_branch_{branch}_{year}_{category}_crime_data.csv')
        df = pd.DataFrame(csv_data)
        df = sort_crime_data(df)
        
        df = df.astype(float)
         
        dict_data[f"{category} ({year} {branch}분기)"] = df
    
        return dict_data
    except Exception:
        print(FileNotFoundError)    
        return "FILE NOT FOUND"

# 인자 값에 따른 데이터 세부 정보를 가져올 메서드
def get_dynamic_subject_crime_data(year:str, branch:int, category:str, subject:str):    
    dict_data = {}
    try:
        csv_data = pd.read_csv(f'./templates/crime_data/branch/{year}/{category}/crime_report_branch_{branch}_{year}_{category}_crime_data.csv')
            
        df = pd.DataFrame(csv_data)
        df = sort_crime_data(df)
        
        diff_df = df[df.columns.difference(["총 계"])] #총계 제외
        
        extraction_data = diff_df.loc[subject]
            
        extraction_data
        return extraction_data    
    except Exception:
        print(Exception)
        
# 분기에 따른 모든 데이터를 가져올 함수
def get_all_total_branch_subject_number_of_transition(category:str,subject:str,):
    branch = [1,2,3,4]
    
    dict_data = {}
        
    try:
        for i in range(0,4):
            csv_data = pd.read_csv(f'./templates/crime_data/branch/2023/{category}/crime_report_branch_{branch[i]}_2023_{category}_crime_data.csv')
            df = pd.DataFrame(csv_data)
            df = sort_crime_data(df)
        
            extraction_df = df.loc[subject]
            
            dict_data[f"{branch[i]}분기"] = extraction_df
        return dict_data    
    except Exception:
        print(Exception)
        
# 분기와 세부주제에 따른 데이터를 가져올 함수
def get_subject_categorize_branch_number_of_transition(category:str,subject:str):
    branch = [1,2,3,4]
    
    dict_data = {}
        
    try:
        for i in range(0,4):
            csv_data = pd.read_csv(f'./templates/crime_data/branch/2023/{category}/crime_report_branch_{branch[i]}_2023_{category}_crime_data.csv')
            df = pd.DataFrame(csv_data)                        
            df = sort_crime_data(df)
                        
            extraction_df = df.loc[:,subject]
            
            dict_data[f"{branch[i]}분기"] = extraction_df
        return dict_data    
    except Exception:
        print(Exception)
    
        
# 데이터 정리 메서드
def sort_crime_data(data : pd.DataFrame):
    try:
        data = data.transpose()
        data.rename(columns=data.iloc[0], inplace=True)
        data = data.drop(data.index[0])
                        
        return data
    except Exception:
        print(FileNotFoundError)    
