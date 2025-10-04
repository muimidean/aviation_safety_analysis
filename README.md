# Aviation Safety Analysis
### Overview

This project analyzes global aviation accident data collected by the National Transportation Safety Board (NTSB) from 1962 to 2023 to assess safety risks and identify factors associated with higher accident occurrences. The analysis aims to determine which aircraft types, models, and engine configurations are most prone to accidents, as well as to uncover patterns in accident severity, weather conditions, and phases of flight.

By understanding these trends, aviation organizations and policymakers can make data-driven decisions to enhance flight safety, guide aircraft purchasing choices, and improve operational risk management.

# Business Problem
The aviation industry continually strives to reduce accident rates and improve safety standards. However, with thousands of recorded incidents spanning over six decades, it can be challenging to determine where the greatest risks lie.
This analysis seeks to address the following key questions:
-Which aircraft makes and models have recorded the highest and lowest number of accidents?
-How do weather conditions and flight phases influence accident severity?
-What patterns exist over time, and do they indicate improvement or recurring safety issues?
-By identifying these patterns, aviation safety authorities, airlines, and manufacturers can prioritize risk mitigation efforts, focus training initiatives, and refine maintenance procedures.

# Data

The dataset, Aviation_Data.csv, was obtained from the NTSB aviation accident database.
It contains 90,348 records and 31 variables, including:
-Date and Location of each accident
-Aircraft Make, Model, and Engine Type
-Phase of Flight (e.g., takeoff, climb, cruise, landing)
-Weather Conditions
-Aircraft Damage Level
-Injury Severity (fatal, serious, minor, or none)

After inspection, 1,390 duplicate entries were removed, and missing values were handled appropriately to improve data integrity.

#Methods

The analysis employs descriptive analytics and data visualization techniques using Python libraries such as Pandas, Matplotlib, and Seaborn. Key steps included:
-Data Cleaning: Removing duplicates, handling missing values, and standardizing categories.
-Exploratory Data Analysis (EDA): Examining patterns by aircraft make, flight phase, weather condition, and severity.
-Visualization: Creating bar charts, trend lines, and severity comparisons to uncover relationships and trends.

# Results
1. Accidents by Phase of Flight
The landing phase recorded the highest number of accidents (~16,000), followed by takeoff (~12,500) and cruise (~10,000) phases. This suggests that the most critical safety risks occur during transitional phases rather than steady flight.
2. Aircraft Makes and Models
Certain aircraft manufacturers exhibited higher accident counts, indicating possible relationships between design, operational usage, and incident frequency. Conversely, a few models demonstrated consistently lower accident records, suggesting stronger safety performance.
3. Accident Severity and Damage
A strong correlation was observed between severe aircraft damage and fatal or serious injury outcomes. Minor damage cases were more likely to result in non-fatal or no-injury events.
4. Weather Conditions
Most accidents occurred under clear weather, implying that human or mechanical factors may outweigh environmental influences. However, poor weather conditions still showed a higher proportion of fatal accidents.
5. Trends Over Time
Overall accident occurrences have declined steadily since the early 1990s, reflecting the impact of advancements in aviation technology, regulation, and safety management systems (SMS).

# Conclusion
The findings from this analysis highlight that the majority of aviation accidents occur during the landing and takeoff phases, emphasizing the need for increased pilot training, automation support, and safety procedures during these critical moments. The results also reveal that certain aircraft types and models are associated with higher accident frequencies, which suggests that manufacturers and operators should collaborate to address recurring design or operational vulnerabilities. Moreover, while most accidents occur under clear weather conditions, the data indicates that poor weather still contributes to a higher likelihood of fatal outcomes, reinforcing the importance of advanced weather monitoring and pilot decision-making tools. The overall decline in accident trends over time reflects the success of safety improvements and regulatory interventions, yet ongoing vigilance is essential to maintain and further this progress.

# Next steps
Future analyses could extend this research to develop predictive models that assess accident likelihood based on factors such as aircraft type, flight phase, and weather conditions. Building a quantitative risk index would also allow for more objective comparisons of aircraft safety performance across manufacturers and engine types. Additionally, incorporating geospatial analysis could identify regional accident hotspots and provide valuable insight for targeted safety measures. Further exploration into the relationship between maintenance practices, aircraft age, and accident frequency would enhance understanding of mechanical reliability and lifecycle safety. Together, these next steps would provide deeper insights to support data-driven decision-making in aviation safety management and policy development.
