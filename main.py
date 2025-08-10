# This code is written in python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Added for trend line calculation

# Read the dataset
lwd = pd.read_csv("livwell135.csv")

# =============================================
# PART 7 STEP 2: DATA STORY NARRATIVE
# =============================================

print("\n=== WOMEN'S LITERACY IN SENEGAL: A DATA STORY ===\n")

# SETTING SECTION
print("SETTING:")
print("• Senegal is a West African nation with a population of 17 million")
print("• 52% of women are literate compared to 71% of men (World Bank 2021)")
print("• Rural areas have particularly low literacy rates")
print("• French is the official language but most speak Wolof at home\n")
input("Press Enter to continue to Characters...\n")

# CHARACTERS SECTION
print("CHARACTERS AFFECTED:")
print("• Aissatou (14): Had to leave school to help her family farm")
print("• Fatou (32): Can't read medicine labels for her children")
print(
    "• Mariama (18): Dreams of nursing school but struggles with French texts\n"
)
input("Press Enter to continue to Context...\n")

# CONTEXT SECTION
print("CONTEXT & CHALLENGES:")
print("• 30% of girls marry before 18 (UNICEF)")
print("• Rural schools often lack qualified teachers")
print("• French-language curriculum creates barriers")
print("• Families sometimes prioritize boys' education\n")
input("Press Enter to view the data trends...\n")

# =============================================
# PART 6 STEP 2: DATA VISUALIZATION (MILD OPTION)
# =============================================

# Filter data for Senegal only
senegal_data = lwd[lwd["country_name"] == "Senegal"]

# Print column to verify we have data
print("\nChecking data availability:")
print(senegal_data["ED_litt_p"].describe())

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(senegal_data["year"],
            senegal_data["ED_litt_p"],
            color="purple",
            s=100,
            alpha=0.7)

# Add trend line (only if we have enough data points)
if len(senegal_data) > 1:
            z = np.polyfit(senegal_data["year"], senegal_data["ED_litt_p"], 1)
            p = np.poly1d(z)
            plt.plot(senegal_data["year"], p(senegal_data["year"]), "r--")

# Format the plot
plt.title("Women's Literacy Rate in Senegal (1990-2020)", fontsize=14, pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Percentage of Women Who Are Literate", fontsize=12)
plt.ylim(0, 100)  # Adjusted to accommodate 100% scale
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Show the plot
plt.show()

# =============================================
# RESEARCH QUESTION & CALL TO ACTION
# =============================================

print("\nKEY INSIGHTS FROM THE DATA:")
print("- Literacy rates are improving but remain low")
print("- The gender gap persists across all years")
print("- Progress slowed after 2010\n")

print("RESEARCH QUESTION FOR FUNDING:")
print("How can Senegal accelerate women's literacy gains by:")
print("1) Developing Wolof-language learning materials?")
print("2) Addressing economic barriers to girls' education?")
print("3) Training more female teachers in rural areas?\n")

print("WHY THIS MATTERS:")
print("Educated women lead to:")
print("• 50% reduction in child mortality (UNESCO)")
print("• Increased family incomes")
print("• More women in leadership roles")
print("• Sustainable community development")
