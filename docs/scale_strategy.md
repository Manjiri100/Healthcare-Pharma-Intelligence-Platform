# Enterprise Scale Strategy

The project separates small reviewable sample data from generated bulk data. The default synthetic environment contains **50,000 patients, 25 clinical trials, 150 sites, 1,000,000 visits and 100,000 adverse events**.

Bulk data is generated in partitioned CSV files and excluded from GitHub. This demonstrates a repeatable pattern for scaling analytical workloads without turning the repository into a multi-gigabyte data dump.

Example larger run:

```bash
python generator/generate_healthcare_data.py --patients 100000 --trials 50 --sites 300 --visits 5000000 --adverse-events 500000
```

The 1M+ scale is a **synthetic portfolio environment / technical capability demonstration**, not a claim about production clinical-data volumes handled in employment.
