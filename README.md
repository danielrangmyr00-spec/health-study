# Health Study – Del 2

- Kod strukturerad i moduler (`src/`)
- Klass **HealthAnalyzer** för blodtrycksanalys
- BMI beräknas som extra feature
- Linjär regression via NumPy:
  \[
  β = (X^TX)^{-1}X^Ty
  \]
- Visualiseringar: ålder → BP, BMI → BP, BP per åldersgrupp

## Körning
1. Aktivera venv
2. `pip install -r requirements.txt`
3. Öppna notebook → **Restart & Run All**

Dataset läses relativt: `data/health_study_dataset.csv`
Python: **3.13.7**
