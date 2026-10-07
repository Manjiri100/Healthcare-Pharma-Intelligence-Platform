from pathlib import Path
import subprocess, sys
import pandas as pd

def test_enterprise_generator_small_run(tmp_path):
    script=Path(__file__).parents[1]/"generator"/"generate_healthcare_data.py"
    out=tmp_path/"generated"
    subprocess.run([sys.executable,str(script),"--output",str(out),"--patients","100","--trials","5","--sites","10","--visits","1000","--adverse-events","200"],check=True)
    assert len(pd.read_csv(out/"patients.csv"))==100
    assert len(pd.read_csv(out/"clinical_trials.csv"))==5
    assert len(pd.read_csv(out/"sites.csv"))==10
    visits=pd.concat(pd.read_csv(x) for x in out.glob("visits_part_*.csv"))
    adverse=pd.concat(pd.read_csv(x) for x in out.glob("adverse_events_part_*.csv"))
    assert len(visits)==1000 and len(adverse)==200
    assert visits.patient_id.isin(pd.read_csv(out/"patients.csv").patient_id).all()
