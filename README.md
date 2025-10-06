# ✈️ Aviation Safety Analysis

### Interactive Dashboard  
🔗 **Explore the Tableau Visualization:** [View Dashboard on Tableau Public](https://public.tableau.com/views/Aviation_Analysis_17595907339060/DashboardVisualization?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## 🧭 Overview

This project analyzes **global aviation accident data** collected by the **National Transportation Safety Board (NTSB)** from **1962 to 2023** to assess safety risks and identify factors associated with higher accident occurrences.  

The analysis determines which **aircraft types, models, and engine configurations** are most prone to accidents and explores how **weather conditions** and **phases of flight** influence accident severity.

By understanding these patterns, aviation organizations and policymakers can make **data-driven decisions** to enhance flight safety, guide aircraft purchasing choices, and improve operational risk management.

---

## 💼 Business Problem

The aviation industry continually strives to reduce accident rates and improve safety standards. However, with thousands of recorded incidents spanning six decades, it can be challenging to determine where the greatest risks lie.

This analysis addresses key questions:
- Which aircraft makes and models have recorded the highest and lowest number of accidents?  
- How do weather conditions and flight phases influence accident severity?  
- What patterns exist over time — do they show improvement or recurring issues?  

By identifying these patterns, aviation safety authorities, airlines, and manufacturers can **prioritize risk mitigation efforts**, **enhance training**, and **refine maintenance procedures**.

---

## 🧾 Data

**Source:** NTSB Aviation Accident Database  
**File:** `Aviation_Data.csv`  
**Records:** 90,348  
**Variables:** 31  

Key data fields include:
- Date and location of each accident  
- Aircraft make, model, and engine type  
- Phase of flight (e.g., takeoff, climb, cruise, landing)  
- Weather conditions  
- Aircraft damage level  
- Injury severity (fatal, serious, minor, none)  

After inspection:
- 1,390 duplicate entries were removed  
- Missing values were handled and categories standardized to improve data integrity  

---

## ⚙️ Methods

The project applies **descriptive analytics** and **data visualization** techniques using:
- 🐍 **Python (Pandas, Matplotlib, Seaborn)**
- 📊 **Tableau** for interactive dashboards

Key steps:
1. **Data Cleaning** – removing duplicates, handling missing values, and standardizing categories  
2. **Exploratory Data Analysis (EDA)** – examining patterns by aircraft make, flight phase, weather, and severity  
3. **Visualization** – creating bar charts, trend lines, and severity comparisons to uncover insights  

---

## 📈 Results

1. **Accidents by Phase of Flight**  
   - The **landing phase** recorded the highest number of accidents (~16,000), followed by **takeoff (~12,500)** and **cruise (~10,000)**.  
   - Transitional phases pose the greatest safety risks.

2. **Aircraft Makes and Models**  
   - Certain manufacturers had higher accident counts, possibly linked to design or operational usage.  
   - Some models showed consistently lower accident rates, reflecting strong safety performance.

3. **Accident Severity and Damage**  
   - Severe aircraft damage strongly correlates with **fatal or serious injuries**.  
   - Minor damage events typically result in **non-fatal outcomes**.

4. **Weather Conditions**  
   - Most accidents occurred in **clear weather**, suggesting human/mechanical causes dominate.  
   - Poor weather increased the proportion of **fatal accidents**.

5. **Trends Over Time**  
   - Accident occurrences have **declined steadily since the 1990s**, reflecting technological and regulatory safety advancements.

---

## 🧩 Conclusion

The findings highlight that most aviation accidents occur during **landing and takeoff**, underscoring the need for:
- Enhanced **pilot training and automation support**  
- Improved **safety procedures** during critical phases  
- Manufacturer-operator collaboration to address recurring vulnerabilities  

While most accidents happen in clear weather, **poor weather conditions** still contribute significantly to fatal outcomes, reinforcing the importance of **advanced weather monitoring** and **pilot decision-support systems**.  

The overall **decline in accident rates** demonstrates the effectiveness of safety improvements, though continued vigilance remains essential.

---

## 🔮 Next Steps

Future analyses could include:
- **Predictive modeling** of accident likelihood based on flight, aircraft, and weather features  
- Development of a **quantitative risk index** for comparing aircraft safety  
- **Geospatial analysis** to identify accident hotspots  
- Deeper exploration of **maintenance practices**, **aircraft age**, and **mechanical reliability**

Together, these steps would provide deeper insights to support **data-driven decision-making** in aviation safety and policy development.

---

### 🧠 Tools Used
- **Python**: Pandas, Matplotlib, Seaborn  
- **Tableau**: Interactive data visualization  
- **Excel**: Data preprocessing and inspection  
