import json, sys
THRESHOLD = 0.02
with open('metrics_baseline.json') as f: base = json.load(f)['auc']
with open('metrics_blackbox.json') as f: new = json.load(f)['auc']
delta = (new - base) / base
print(f"Δ={delta:.3%}")
if delta <= THRESHOLD:
    print("Interpretable model acceptable")
else:
    print("Black-box chosen – ensure explainability docs")
