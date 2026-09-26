import pandas as pd
from pathlib import Path


CLEANED_DIR = Path("../cleaned_datasets")

S1_PATH = CLEANED_DIR / "cleaned_source1.tsv"

s1 = pd.read_csv(
    S1_PATH,
    sep="\t",
    dtype=str,
    keep_default_na=False
)

print("S1:", len(s1))


# ============================================================
# NAME BLOCK SIZES
# ============================================================

name_counts = (
    s1[s1["clean_business_name"] != ""]
    .groupby(
        ["country", "clean_business_name"]
    )
    .size()
)

print("\nNAME BLOCKS")
print("-----------")
print("Unique blocks:", len(name_counts))
print("Median:", name_counts.median())
print("Mean:", name_counts.mean())
print("Max:", name_counts.max())

print("\nLargest name blocks:")
print(name_counts.sort_values(ascending=False).head(30))


# ============================================================
# ADDRESS BLOCK SIZES
# ============================================================

address_counts = (
    s1[s1["clean_business_address"] != ""]
    .groupby(
        ["country", "clean_business_address"]
    )
    .size()
)

print("\nADDRESS BLOCKS")
print("--------------")
print("Unique blocks:", len(address_counts))
print("Median:", address_counts.median())
print("Mean:", address_counts.mean())
print("Max:", address_counts.max())

print("\nLargest address blocks:")
print(address_counts.sort_values(ascending=False).head(30))


# ============================================================
# NAME + LEADING NUMBER
# ============================================================

name_number_counts = (
    s1[
        (s1["clean_business_name"] != "") &
        (s1["leading_number"] != "")
    ]
    .groupby(
        [
            "country",
            "clean_business_name",
            "leading_number"
        ]
    )
    .size()
)

print("\nNAME + LEADING NUMBER BLOCKS")
print("----------------------------")
print("Unique blocks:", len(name_number_counts))
print("Median:", name_number_counts.median())
print("Mean:", name_number_counts.mean())
print("Max:", name_number_counts.max())

print("\nLargest name+number blocks:")
print(
    name_number_counts
    .sort_values(ascending=False)
    .head(30)
)