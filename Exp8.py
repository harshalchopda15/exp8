import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = {
    'Milk': [1, 0, 1, 1],
    'Bread': [1, 1, 1, 0],
    'Butter': [1, 0, 1, 1]
}

df = pd.DataFrame(data)

freq_items = apriori(df, min_support=0.5, use_colnames=True)

rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)

print(freq_items)
print(rules)