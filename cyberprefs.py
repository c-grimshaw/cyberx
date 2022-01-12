import os
import pandas as pd


def get_files():
    """Collects all .xlsx files in current working directory."""
    return [file for file in os.listdir() if file.endswith(".xlsx")]


def get_name(df):
    """Returns the name of the student from the DataFrame."""
    ROW_IDX, COL_IDX = 2, 1
    name = df.iloc[ROW_IDX][COL_IDX]
    name = name.replace("_", "").replace("Your Name: ", "")
    return name


def get_choices(df):
    """Subsets parent DataFrame, yielding student choices for roles."""
    role_choices = (
        pd.DataFrame(df.loc[6:40, df.columns[[1, 3, 4, 5]]])
        .dropna(how="all")
        .fillna("")
    )

    # Remove remaining non-role rows from DF.
    role_choices = role_choices[
        role_choices["Unnamed: 1"].str.contains(" Team") == False
    ]
    return role_choices


def count_roles(df, counter, name):
    """Counts role choices for a given student."""
    ROLE, FIRST, SECOND, THIRD = range(0, 4)
    for _, row in df.iterrows():
        role = row[ROLE]
        if role not in counter:
            counter[role] = {"first": [], "second": [], "third": []}

        if row[FIRST]:  counter[role]["first"].append(name)
        if row[SECOND]: counter[role]["second"].append(name)
        if row[THIRD]:  counter[role]["third"].append(name)

    return counter


if __name__ == "__main__":
    rolesCounter = {}

    for student_file in get_files():
        df = pd.read_excel(student_file, nrows=52)
        student = get_name(df)

        roles = get_choices(df)
        count_roles(roles, rolesCounter, student)

    for role in rolesCounter:
        print(
            f"""\
        {role.upper()}
        First choices: {', '.join(student for student in sorted(rolesCounter[role]['first']))}
        Second choices: {', '.join(student for student in sorted(rolesCounter[role]['second']))}
        Third choices: {', '.join(student for student in sorted(rolesCounter[role]['third']))}
        """
        )