![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# A/CNK A/NK Peraluminous Classifier
 
*For igneous petrologists and geochemists: enter weight percent of Al₂O₃, CaO, Na₂O, and K₂O to instantly compute A/CNK and A/NK indices and classify the melt as peraluminous, metaluminous, or peralkaline.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geochemistry
 
Inputs: four numeric fields for weight percent of Al₂O₃ (default 15.0), CaO (default 10.0), Na₂O (default 3.0), and K₂O (default 2.0). The tool converts wt% to molar quantities using molecular weights (Al₂O₃=101.96, CaO=56.08, Na₂O=61.98, K₂O=94.20). Then it computes A/CNK = moles Al₂O₃ / (moles CaO + moles Na₂O + moles K₂O) and A/NK = moles Al₂O₃ / (moles Na₂O + moles K₂O). Classification rules: if A/CNK > 1.1 → strongly peraluminous; if 1.0 < A/CNK ≤ 1.1 → weakly peraluminous; if A/CNK < 1.0 and A/NK > 1.0 → metaluminous; if A/NK < 1.0 → peralkaline. Outputs: (1) numeric display of A/CNK rounded to 2 decimals, (2) numeric display of A/NK rounded to 2 decimals, (3) text label with classification, (4) a matplotlib scatter plot (400×400 px) showing the input point on an A/CNK vs A/NK diagram with shaded fields for peraluminous, metaluminous, and peralkaline regions (based on typical boundaries: vertical line at A/CNK=1.0, horizontal line at A/NK=1.0). Axes are labeled and limits set to 0-2 for A/CNK and 0-2 for A/NK. UI layout: four input sliders/numbers in a row, a 'Calculate' button, then outputs arranged in two columns: left column with numeric readouts and text classification, right column with the plot. No AI/ML component; pure geochemical classification using standard petrology equations.
 
## Run it
 
```bash
docker build -t a-cnk-a-nk-peraluminous-classifier .
docker run -p 7860:7860 a-cnk-a-nk-peraluminous-classifier
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-28.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
