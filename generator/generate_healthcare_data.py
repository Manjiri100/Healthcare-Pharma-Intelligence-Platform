"""Generate enterprise-scale synthetic healthcare/pharma analytics data."""
from __future__ import annotations
import argparse, csv, random
from datetime import date, timedelta
from pathlib import Path
FIRST=["Aarav","Emily","Noah","Sofia","Daniel","Amelia","Oliver","Mia","Ethan","Grace","Liam","Aisha","Priya","Thomas","Neha","Arjun","Isla","Leo"]
LAST=["Shah","Carter","Williams","Martin","Brown","Wilson","Smith","Jones","Taylor","Evans","Thomas","Khan","Patel","Green","Mehta","Walker","Clarke","Davies"]
COUNTRIES=["United Kingdom","Germany","France","Spain","Netherlands","Ireland","Sweden","Belgium"]
THERAPEUTIC=["Cardiology","Oncology","Neurology","Immunology","Respiratory","Rare Disease","Diabetes","Dermatology"]
def write_csv(path,rows,fields):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
def generate(out,seed=42,patients_n=50000,trials_n=25,sites_n=150,visits_n=1000000,adverse_n=100000):
    random.seed(seed); out=Path(out); out.mkdir(parents=True,exist_ok=True); base=date(2024,1,1)
    trials=[]
    for i in range(1,trials_n+1):
        s=base+timedelta(days=random.randint(0,600)); trials.append({"trial_id":f"TR{i:03d}","trial_name":f"TrialProgram-{i:03d}","phase":random.choice(["Phase I","Phase II","Phase III"]),"therapeutic_area":random.choice(THERAPEUTIC),"start_date":s.isoformat(),"target_end_date":(s+timedelta(days=random.randint(240,600))).isoformat(),"status":random.choice(["Active","Recruiting","Completed"])})
    sites=[]
    for i in range(1,sites_n+1): sites.append({"site_id":f"S{i:04d}","site_name":f"Research Site {i:04d}","country":random.choice(COUNTRIES),"trial_id":f"TR{random.randint(1,trials_n):03d}","planned_patients":random.randint(40,500),"active_patients":random.randint(5,180)})
    patients=[]; pids=[]
    for i in range(1,patients_n+1):
        pid=f"PT{i:06d}"; pids.append(pid); patients.append({"patient_id":pid,"patient_name":f"{random.choice(FIRST)} {random.choice(LAST)}","age":random.randint(18,85),"sex":random.choice(["F","M"]),"trial_id":f"TR{random.randint(1,trials_n):03d}","site_id":f"S{random.randint(1,sites_n):04d}","enrolment_date":(base+timedelta(days=random.randint(0,700))).isoformat(),"status":random.choices(["Active","Completed","Withdrawn"],[70,23,7])[0]})
    write_csv(out/"clinical_trials.csv",trials,list(trials[0])); write_csv(out/"sites.csv",sites,list(sites[0])); write_csv(out/"patients.csv",patients,list(patients[0]))
    vf=["visit_id","patient_id","visit_date","visit_type","status"]; remaining=visits_n; part=1; vid=1
    while remaining:
        n=min(100000,remaining); rows=[]
        for _ in range(n): rows.append({"visit_id":f"V{vid:08d}","patient_id":random.choice(pids),"visit_date":(base+timedelta(days=random.randint(0,900))).isoformat(),"visit_type":random.choice(["Screening","Baseline","Follow-up","Treatment","Close-out"]),"status":random.choices(["Completed","Pending","Missed"],[78,15,7])[0]}); vid+=1
        write_csv(out/f"visits_part_{part:02d}.csv",rows,vf); part+=1; remaining-=n
    af=["event_id","patient_id","event_date","event_type","severity","outcome"]; remaining=adverse_n; aid=1; part=1
    while remaining:
        n=min(100000,remaining); rows=[]
        for _ in range(n): rows.append({"event_id":f"AE{aid:07d}","patient_id":random.choice(pids),"event_date":(base+timedelta(days=random.randint(0,900))).isoformat(),"event_type":random.choice(["Headache","Nausea","Fatigue","Rash","Dizziness","Fever","Injection-site reaction"]),"severity":random.choices(["Mild","Moderate","Severe"],[68,27,5])[0],"outcome":random.choice(["Resolved","Recovering","Ongoing","Hospitalised"])}); aid+=1
        write_csv(out/f"adverse_events_part_{part:02d}.csv",rows,af); part+=1; remaining-=n
    print(f"Generated: {patients_n:,} patients | {trials_n:,} trials | {sites_n:,} sites | {visits_n:,} visits | {adverse_n:,} adverse events")
if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--output",default="data/generated"); p.add_argument("--seed",type=int,default=42); p.add_argument("--patients",type=int,default=50000); p.add_argument("--trials",type=int,default=25); p.add_argument("--sites",type=int,default=150); p.add_argument("--visits",type=int,default=1000000); p.add_argument("--adverse-events",type=int,default=100000); a=p.parse_args(); generate(a.output,a.seed,a.patients,a.trials,a.sites,a.visits,a.adverse_events)
