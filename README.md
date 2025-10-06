# Aviation Safety Analysis

### Tableau Dashboard  
🔗 [View Interactive Visualization](https://public.tableau.com/views/Aviation_Analysis_17595907339060/DashboardVisualization?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## Overview
This project analyzes **global aviation accident data (1962–2023)** from the **National Transportation Safety Board (NTSB)** to identify patterns and risk factors affecting flight safety.  
It focuses on aircraft type, model, weather, and flight phase to understand when and why accidents occur.

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
The analysis shows clear safety differences across aircraft models and manufacturers. The safest aircraft include the Piper PA-28R-201T, Aero Commander 690, Grumman American AA-1A, Piper PA-60, and Cessna 401B.
Most accidents occurred during the landing and takeoff phases, with fatal injuries peaking in the late 1990s but steadily declining due to improved safety policies.
Cessna and Piper recorded the most accidents, largely because of their widespread general aviation use, while Boeing, Beech, and Bell showed lower frequencies, reflecting stronger safety standards.
Ongoing maintenance, monitoring, and data-driven safety measures remain key to minimizing future aviation accidents.

---

## Next Steps
- Build **predictive models** for accident likelihood  
- Develop a **safety risk index** for aircraft models  
- Use **geospatial analysis** to identify regional accident hotspots  
