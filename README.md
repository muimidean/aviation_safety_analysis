# Aviation Safety Analysis

### Tableau Dashboard  
🔗 [View Interactive Visualization](https://public.tableau.com/views/Aviation_Analysis_17595907339060/DashboardVisualization?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## Overview
This project analyzes **global aviation accident data (1962–2023)** from the **National Transportation Safety Board (NTSB)** to identify patterns and risk factors affecting flight safety.  
It focuses on **aircraft type, model, weather**, and **flight phase** to understand when and why accidents occur.

---

## Dataset Summary
- **File:** Aviation_Data.csv  
- **Records:** 90,348 rows and 31 columns  
- **Duplicates Removed:** 1,390  


Key columns include:
`Event.Id`, `Accident.Number`, `Event.Date`, `Location`, `Make`, `Model`,  
`Engine.Type`, `Weather.Condition`, `Broad.phase.of.flight`, and `Injury.Severity`.

**Missing Values:**  
Some columns (e.g., `Latitude`, `Longitude`, `Aircraft.Category`, `Engine.Type`) have missing data ranging from 5% to 60%.  

**Statistical Highlights:**
- Mean engines per aircraft: **1.15**  
- Mean fatalities per accident: **0.65**  
- Mean uninjured count: **5.33**  
- Maximum recorded fatalities: **349**

---

## Tools Used
- **Python:** Pandas, Matplotlib, Seaborn  
- **Tableau:** Interactive visualization and dashboard creation  

---

## Key Findings
- **Landing and takeoff phases** account for most accidents.  
- **Clear weather** accidents dominate, suggesting human or mechanical causes.  
- **Accident rates have declined** since the 1990s due to better safety measures.  

---

## Conclusion
Accidents mainly occur during **critical flight phases**, highlighting the need for enhanced **pilot training, automation**, and **maintenance practices**.  
While clear weather sees the most incidents, **poor weather increases fatality severity**, emphasizing the importance of **weather monitoring systems**.

---

## Next Steps
- Build **predictive models** for accident likelihood  
- Develop a **safety risk index** for aircraft models  
- Use **geospatial analysis** to identify regional accident hotspots  
