![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Magma Viscosity Calculator
 
*For volcanologists and petrologists: select magma composition and enter temperature to instantly estimate melt viscosity using the Vogel-Fulcher-Tammann (VFT) model, with optional water content correction.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Volcanology
 
The user provides three inputs: (1) Magma composition — a dropdown with options 'Basalt', 'Andesite', 'Dacite', 'Rhyolite'; (2) Temperature in °C (range 700–1400°C, step 1°C); (3) Water content in wt% (0–8, step 0.1), default 0. The core logic uses the VFT equation: log10(η) = A + B/(T - C), where viscosity η is in Pa·s and T is in °C. For each magma type the coefficients are (dry): Basalt (A=-3.0, B=2000, C=300), Andesite (A=-2.5, B=4000, C=200), Dacite (A=-2.0, B=6000, C=150), Rhyolite (A=-1.5, B=8000, C=100). These are representative values from published silicate melt viscosity models. Water content correction is applied: subtract (0.4 × H2O_wt%) from the dry log10(η) (linear approximation). The UI shows: a GrNumber input for temperature, a GrDropdown for composition, a GrNumber for water content, and a 'Calculate' button. Outputs: (a) Numerical display of log10(η) and η in Pa·s; (b) A GrPlot line chart of log10(η) vs. temperature for a range of ±50°C around the user input, with fixed composition and water content; (c) A text classification based on log10(η): <2 = 'Very fluid', 2–4 = 'Fluid', 4–6 = 'Viscous', 6–8 = 'Very viscous', >8 = 'Extremely viscous'. No AI/ML component — all calculation is deterministic using the VFT equation and empirical coefficients.
 
## Run it
 
```bash
docker build -t magma-viscosity-calculator .
docker run -p 7860:7860 magma-viscosity-calculator
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
 
Built 2026-09-27.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
