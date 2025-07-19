# MirrorOrg: Computational Autopsy of Team Collapse

This repository contains the official paper and analysis code for **MirrorOrg™**, a diagnostic framework based on the MirrorMind identity model.

🧠 **Core Idea**  
We model an AI (or human) identity vector as:  
**I = (E, C, X, V, B)**  
Emotion, Cognition, Expression, Value, Bias

🔥 **Conflict Metric**  
Conflict between two agents is measured by cosine distance between identity vectors:

```
Conflict(i, j) = 1 - (Iᵢ • Iⱼ) / (||Iᵢ|| × ||Iⱼ||)
```

📄 **Paper**  
See `./paper/mirrororg_autopsy_paper.pdf` for the full paper (KOR/ENG coming soon).

🧪 **Code Overview**
- `identity_vector_model.py`: sample vector structure
- `conflict_calculator.py`: computes conflict coefficient
- `sample_chat_data.json`: dummy interaction data

---

MirrorOrg bridges research and real-world application, allowing us to quantify emotional patterns and relational breakdowns from natural language logs.
