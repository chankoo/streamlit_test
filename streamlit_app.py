import streamlit as st
import pandas as pd
import random
import datetime
from datetime import timedelta


# --- 2. DEPARTMENT TABLE --- (부서관리)

# 회사 설립일
company_founding_date = datetime.date(2010, 1, 1)

# --- base_structure에 'HR Team' 추가 ---
base_structure = [
    # Level 1
    {
        "DEP_ID": "DEP001",
        "DEP_NAME": "Headquarters",
        "UP_DEP_ID": None,
        "DEPT_TYPE": "본사",
    },
    # Level 2: Divisions
    {
        "DEP_ID": "DEP002",
        "DEP_NAME": "Planning Division",
        "UP_DEP_ID": "DEP001",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP003",
        "DEP_NAME": "Development Division",
        "UP_DEP_ID": "DEP001",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP004",
        "DEP_NAME": "Sales Division",
        "UP_DEP_ID": "DEP001",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP005",
        "DEP_NAME": "Operating Division",
        "UP_DEP_ID": "DEP001",
        "DEPT_TYPE": "현장",
    },
    # Level 3: Offices
    {
        "DEP_ID": "DEP006",
        "DEP_NAME": "Strategy Office",
        "UP_DEP_ID": "DEP002",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP007",
        "DEP_NAME": "Finance Office",
        "UP_DEP_ID": "DEP002",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP008",
        "DEP_NAME": "R&D Office",
        "UP_DEP_ID": "DEP003",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP009",
        "DEP_NAME": "QA Office",
        "UP_DEP_ID": "DEP003",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP010",
        "DEP_NAME": "Marketing Office",
        "UP_DEP_ID": "DEP004",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP011",
        "DEP_NAME": "Domestic Sales Office",
        "UP_DEP_ID": "DEP004",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP012",
        "DEP_NAME": "Global Sales Office",
        "UP_DEP_ID": "DEP004",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP013",
        "DEP_NAME": "Engineering Office",
        "UP_DEP_ID": "DEP005",
        "DEPT_TYPE": "현장",
    },
    {
        "DEP_ID": "DEP014",
        "DEP_NAME": "Production Office",
        "UP_DEP_ID": "DEP005",
        "DEPT_TYPE": "현장",
    },
    # Level 4: Teams
    # Strategy Office 산하
    {
        "DEP_ID": "DEP015",
        "DEP_NAME": "Planning Team",
        "UP_DEP_ID": "DEP006",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP016",
        "DEP_NAME": "Analysis Team",
        "UP_DEP_ID": "DEP006",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP017",
        "DEP_NAME": "HR Team",
        "UP_DEP_ID": "DEP006",
        "DEPT_TYPE": "본사",
    },  # <-- 추가된 팀
    # Finance Office 산하
    {
        "DEP_ID": "DEP018",
        "DEP_NAME": "Accounting Team",
        "UP_DEP_ID": "DEP007",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP019",
        "DEP_NAME": "Treasury Team",
        "UP_DEP_ID": "DEP007",
        "DEPT_TYPE": "본사",
    },
    # R&D Office 산하
    {
        "DEP_ID": "DEP020",
        "DEP_NAME": "Backend Team",
        "UP_DEP_ID": "DEP008",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP021",
        "DEP_NAME": "Frontend Team",
        "UP_DEP_ID": "DEP008",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP022",
        "DEP_NAME": "Mobile Team",
        "UP_DEP_ID": "DEP008",
        "DEPT_TYPE": "본사",
    },
    # QA Office 산하
    {
        "DEP_ID": "DEP023",
        "DEP_NAME": "System QA Team",
        "UP_DEP_ID": "DEP009",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP024",
        "DEP_NAME": "Service QA Team",
        "UP_DEP_ID": "DEP009",
        "DEPT_TYPE": "본사",
    },
    # Marketing Office 산하
    {
        "DEP_ID": "DEP025",
        "DEP_NAME": "Performance Marketing Team",
        "UP_DEP_ID": "DEP010",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP026",
        "DEP_NAME": "Content Marketing Team",
        "UP_DEP_ID": "DEP010",
        "DEPT_TYPE": "본사",
    },
    # Domestic Sales Office 산하
    {
        "DEP_ID": "DEP027",
        "DEP_NAME": "Domestic Sales Team 1",
        "UP_DEP_ID": "DEP011",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP028",
        "DEP_NAME": "Domestic Sales Team 2",
        "UP_DEP_ID": "DEP011",
        "DEPT_TYPE": "본사",
    },
    # Global Sales Office 산하
    {
        "DEP_ID": "DEP029",
        "DEP_NAME": "APAC Sales Team",
        "UP_DEP_ID": "DEP012",
        "DEPT_TYPE": "본사",
    },
    {
        "DEP_ID": "DEP030",
        "DEP_NAME": "EU/NA Sales Team",
        "UP_DEP_ID": "DEP012",
        "DEPT_TYPE": "본사",
    },
    # Engineering Office 산하
    {
        "DEP_ID": "DEP031",
        "DEP_NAME": "Process Engineering Team",
        "UP_DEP_ID": "DEP013",
        "DEPT_TYPE": "현장",
    },
    {
        "DEP_ID": "DEP032",
        "DEP_NAME": "Quality Engineering Team",
        "UP_DEP_ID": "DEP013",
        "DEPT_TYPE": "현장",
    },
    # Production Office 산하
    {
        "DEP_ID": "DEP033",
        "DEP_NAME": "Production Team Alpha",
        "UP_DEP_ID": "DEP014",
        "DEPT_TYPE": "현장",
    },
    {
        "DEP_ID": "DEP034",
        "DEP_NAME": "Production Team Beta",
        "UP_DEP_ID": "DEP014",
        "DEPT_TYPE": "현장",
    },
    {
        "DEP_ID": "DEP035",
        "DEP_NAME": "Production Team Charlie",
        "UP_DEP_ID": "DEP014",
        "DEPT_TYPE": "현장",
    },
]

# (이하 DataFrame 생성 및 DEP_LEVEL 계산, 최종 처리 로직은 이전과 동일합니다)
departments = []
dep_dates = {"DEP001": company_founding_date}


def make_row(dep_id, name, up_id, dept_type, start_date, end_date=None, use_yn="Y"):
    return {
        "DEP_ID": dep_id,
        "DEP_NAME": name,
        "UP_DEP_ID": up_id,
        "DEPT_TYPE": dept_type,
        "DEP_REL_START_DATE": start_date,
        "DEP_REL_END_DATE": end_date,
        "DEP_USE_YN": use_yn,
    }


for dep in base_structure:
    dep_id = dep["DEP_ID"]
    up_id = dep["UP_DEP_ID"]
    dept_type = dep["DEPT_TYPE"]

    if up_id is None:
        rel_start = company_founding_date
    else:
        parent_date = dep_dates.get(up_id, company_founding_date)
        rel_start = parent_date + timedelta(days=random.randint(0, 300))

    dep_dates[dep_id] = rel_start
    departments.append(
        make_row(dep_id, dep["DEP_NAME"], up_id, dept_type, rel_start, use_yn="Y")
    )

department_df = pd.DataFrame(departments)

dept_structure_for_level_calc = department_df[["DEP_ID", "UP_DEP_ID"]].drop_duplicates()
parent_map = dept_structure_for_level_calc.set_index("DEP_ID")["UP_DEP_ID"].to_dict()


def calculate_dep_level(dep_id, p_map):
    level = 1
    current_id = dep_id
    while pd.notna(p_map.get(current_id)) and current_id in p_map:
        current_id = p_map.get(current_id)
        level += 1
        if level > 10:
            return -1
    return level


dept_level_map = {
    dep_id: calculate_dep_level(dep_id, parent_map)
    for dep_id in dept_structure_for_level_calc["DEP_ID"]
}
department_df["DEP_LEVEL"] = department_df["DEP_ID"].map(dept_level_map)

department_df["DEP_REL_START_DATE"] = pd.to_datetime(
    department_df["DEP_REL_START_DATE"]
).dt.strftime("%Y-%m-%d")
department_df["DEP_REL_END_DATE"] = (
    pd.to_datetime(department_df["DEP_REL_END_DATE"])
    .dt.strftime("%Y-%m-%d")
    .replace("NaT", "")
)
for col in department_df.columns:
    department_df[col] = department_df[col].astype(str)
department_df = department_df.replace({"None": "", "nan": ""})

final_cols = [
    "DEP_ID",
    "DEP_NAME",
    "UP_DEP_ID",
    "DEP_LEVEL",
    "DEPT_TYPE",
    "DEP_REL_START_DATE",
    "DEP_REL_END_DATE",
    "DEP_USE_YN",
]
department_df = department_df[final_cols]


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write(department_df)
