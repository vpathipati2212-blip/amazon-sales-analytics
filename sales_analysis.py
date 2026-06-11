import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# LOAD DATA
# ============================================

file_path = "Amazon Sale Report.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("AMAZON SALES ANALYSIS")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

# ============================================
# CLEAN DATA
# ============================================

df = df.drop_duplicates()
df = df.dropna(axis=1, how="all")

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

if "Amount" in df.columns:
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df["Amount"] = df["Amount"].fillna(0)

if "Qty" in df.columns:
    df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")
    df["Qty"] = df["Qty"].fillna(0)

print("\nData cleaned successfully")

# ============================================
# KPI METRICS
# ============================================

if "Amount" in df.columns:

    total_orders = len(df)
    total_revenue = df["Amount"].sum()

    avg_order = (
        total_revenue / total_orders
        if total_orders > 0 else 0
    )

    print("\n" + "=" * 60)
    print("KEY METRICS")
    print("=" * 60)

    print(f"Total Orders : {total_orders:,}")
    print(f"Total Revenue: ₹{total_revenue:,.2f}")
    print(f"Average Order: ₹{avg_order:,.2f}")

# ============================================
# CATEGORY ANALYSIS
# ============================================

if "Category" in df.columns:

    category_sales = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nTop Categories")
    print(category_sales.head(10))

    plt.figure(figsize=(10, 5))
    category_sales.head(10).plot(kind="bar")
    plt.title("Top Categories by Revenue")
    plt.tight_layout()
    plt.savefig("sales_by_category.png")
    plt.close()

# ============================================
# STATE ANALYSIS
# ============================================

if "ship-state" in df.columns:

    state_sales = (
        df.groupby("ship-state")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nTop States")
    print(state_sales.head(10))

    plt.figure(figsize=(10, 5))
    state_sales.head(10).plot(kind="bar")
    plt.title("Top States by Revenue")
    plt.tight_layout()
    plt.savefig("sales_by_state.png")
    plt.close()

# ============================================
# ORDER STATUS
# ============================================

if "Status" in df.columns:

    status_counts = df["Status"].value_counts()

    print("\nOrder Status")
    print(status_counts.head(10))

# ============================================
# SAVE REPORTS
# ============================================

df.to_excel(
    "amazon_sales_report.xlsx",
    index=False
)

print("\nFiles Created:")
print("✓ amazon_sales_report.xlsx")
print("✓ sales_by_category.png")
print("✓ sales_by_state.png")

print("\nPROJECT COMPLETED SUCCESSFULLY")