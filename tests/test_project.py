from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'/'sample'
def test_expected_files_exist():
    for f in ['patients.csv','clinical_trials.csv','sites.csv','visits.csv','adverse_events.csv']: assert (DATA/f).exists()
def test_sample_counts():
    assert len(pd.read_csv(DATA/'patients.csv'))==12
    assert len(pd.read_csv(DATA/'clinical_trials.csv'))==4
    assert len(pd.read_csv(DATA/'sites.csv'))==6
    assert len(pd.read_csv(DATA/'visits.csv'))==30
    assert len(pd.read_csv(DATA/'adverse_events.csv'))==10
def test_duplicate_patient_is_present():
    df=pd.read_csv(DATA/'patients.csv')
    assert df['patient_id'].duplicated().sum()==1
