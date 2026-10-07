# 🧬 Healthcare & Pharma Intelligence Platform

> **Enterprise-scale synthetic portfolio environment: 1M+ operational records.**

## About the Project

A synthetic healthcare and pharmaceutical analytics project built around a practical business question:

> **How can healthcare and pharma teams identify operational bottlenecks, trial performance issues, patient follow-up risks and data-quality problems from fragmented operational data?**

The project follows a business-first workflow:

**Source Data → Profiling → Data Quality → Investigation → Transformation → Business Insights → Decision Support**

## Project Overview

The sample environment combines five operational datasets: Patients, Clinical Trials, Trial Sites, Patient Visits and Adverse Events.

The project investigates trial performance, site performance, patient follow-up, adverse-event patterns and data-quality issues.

## Sample Data Environment

| Dataset | Records |
|---|---:|
| Patients | 12 |
| Clinical Trials | 4 |
| Trial Sites | 6 |
| Visits | 30 |
| Adverse Events | 10 |

All data is synthetic and created only for portfolio demonstration.

## Analytical Workflow

```text
Operational Sources → Profiling → Data Quality → SQL Investigation
                                      ↓
                                dbt Transformation
                                      ↓
                             Analytical Marts
                                      ↓
                              Decision Support
```

## SQL Investigations

- Trial performance
- Site performance
- Patient visit completion
- Adverse-event monitoring
- Data-quality checks

## Python

Lightweight profiling for row counts, missing values and duplicate identifiers.

## dbt Transformation Layer

**Raw Sources → Staging → Intermediate → Analytical Marts**

Core models include `dim_patient`, `dim_trial`, `dim_site`, `fct_visit`, `fct_adverse_event` and `dq_exceptions`.

## Business Investigation Tickets

1. Trial performance
2. Site performance
3. Patient follow-up
4. Adverse events
5. Data quality

## Skills Demonstrated

SQL • Python • Data Profiling • Data Quality • dbt • Healthcare Analytics • Pharma / Clinical Operations Analytics • Business Investigation • KPI Development • Data Governance

## Repository Structure

```text
Healthcare-Pharma-Intelligence-Platform/
├── business-tickets/
├── data/sample/
├── dbt/
├── docs/
├── python/
├── sql/
├── tests/
└── README.md
```

## 📊 Project Preview

![Healthcare & Pharma Intelligence Platform](docs/project-preview.svg)

> Synthetic portfolio project demonstrating healthcare and pharma operational analytics using SQL, Python, dbt and data-quality controls.

## Important Note

All data is synthetic. This project contains no real patient information and is not clinical evidence or medical advice.
