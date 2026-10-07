from pathlib import Path
import pandas as pd
DATA=Path(__file__).resolve().parents[1]/'data'/'sample'
FILES={'patients':'patients.csv','trials':'clinical_trials.csv','sites':'sites.csv','visits':'visits.csv','adverse_events':'adverse_events.csv'}
def profile():
    print('Healthcare & Pharma Intelligence — data profile')
    for name,filename in FILES.items():
        df=pd.read_csv(DATA/filename)
        print(f'{name:16} rows={len(df):>3} columns={len(df.columns):>2} missing={int(df.isna().sum().sum()):>2}')
    patients=pd.read_csv(DATA/FILES['patients'])
    print('Duplicate patient IDs:',int(patients['patient_id'].duplicated().sum()))
if __name__=='__main__': profile()
