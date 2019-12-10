import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import ast

raw = pd.read_csv("combined_genki_lessons.csv")
raw.head()

# USE BOX PLOT, CALCULATE MAX/MIN
# Initialization
def box_1():
    container1 = [np.nan]

    stroke_char_count = [np.nan]

    # For each # of stroke (1~29)
    for strnum in np.arange(1, 30):
        # Find all rows where strokes equal to the current loop number
        raw_in_strnum = raw[raw["strokes"] == strnum]

        # Calculate the number of kanjis with that stroke (where frequency data != NaN), append to count array
        stroke_char_count.append(raw_in_strnum["frequency"].count())

        # Append those kanji's frequency ranks to a container
        container1.append(list(raw_in_strnum["frequency"].dropna()))

    # The container has (ideally) 29 lists, each contains the rank of frequencies of kanjis with corresponding strokes.
    # So container[1] is kanjis with 1 stroke, their frequency ranks

    # Title, xlabel, ylabel
    title = "number of strokes (X) - rank of frequency(Y)"
    x_label = "number of strokes (count of characters)"
    y_lable = "rank of frequency used in newspaper"

    # Generate xticks and its labels
    xticks = []
    for i in np.arange(1, 24):
        xticks.append("{} ({})".format(i, stroke_char_count[i]))

    x_ticks = np.arange(1, 24)
    x_label = xticks
    data = container1[1:24]

    res = list()
    for i, j, k in zip(data, x_label, x_ticks):
        i.sort()
        res.append(dict(
            highest=int(max(i)),
            lowest=int(min(i)),
            open=int(np.percentile(i, 25)),
            close=int(np.percentile(i, 75)),
            strokes=j,
        ))
    return res
    # useless, avoid output from set_xticklabels
def box_1():
    container1 = [np.nan]

    stroke_char_count = [np.nan]

    # For each # of stroke (1~29)
    for strnum in np.arange(1, 30):
        # Find all rows where strokes equal to the current loop number
        raw_in_strnum = raw[raw["strokes"] == strnum]

        # Calculate the number of kanjis with that stroke (where frequency data != NaN), append to count array
        stroke_char_count.append(raw_in_strnum["frequency"].count())

        # Append those kanji's frequency ranks to a container
        container1.append(list(raw_in_strnum["frequency"].dropna()))

    # The container has (ideally) 29 lists, each contains the rank of frequencies of kanjis with corresponding strokes.
    # So container[1] is kanjis with 1 stroke, their frequency ranks

    # Title, xlabel, ylabel
    title = "number of strokes (X) - rank of frequency(Y)"
    x_label = "number of strokes (count of characters)"
    y_lable = "rank of frequency used in newspaper"

    # Generate xticks and its labels
    xticks = []
    for i in np.arange(1, 24):
        xticks.append("{} ({})".format(i, stroke_char_count[i]))

    x_ticks = np.arange(1, 24)
    x_label = xticks
    data = container1[1:24]

    res = list()
    for i, j, k in zip(data, x_label, x_ticks):
        i.sort()
        res.append(dict(
            highest=int(max(i)),
            lowest=int(min(i)),
            open=int(np.percentile(i, 25)),
            close=int(np.percentile(i, 75)),
            strokes=j,
        ))
    return res


def box_2():
    raw_grades = raw["grade"].unique()
    # sort every value except NaN, which happens to be the last element
    grades = np.sort(raw_grades[:-1])
    grades

    # %%

    # Initialization. Container 2 is the list of "list of frequencies of kanjis taught in some grade"
    container2 = []

    grade_char_count = []

    # For all grades
    for gradenum in np.arange(len(grades)):
        # locate all rows with that grade
        raw_in_gradenum = raw[raw["grade"] == grades[gradenum]]

        # count the number of kanjis taught in that grade
        grade_char_count.append(raw_in_gradenum["frequency"].count())

        # append the list of frequencies to containers
        container2.append(list(raw_in_gradenum['frequency'].dropna()))


    # %%

    # Initialization, figure and axis
    fig2 = plt.figure(figsize=(12, 9))
    axis21 = fig2.add_subplot(1, 1, 1)

    # Box plot
    axis21.boxplot(container2)

    # Title, xlabel, ylabel
    axis21.set_title("Grades (X) - rank of frequency(Y)", fontsize="large")
    axis21.set_xlabel("Grades (count of characters in grade)", fontsize="large")
    axis21.set_ylabel("rank of frequency used in newspaper", fontsize="large")

    # generate and set xticks and labels
    xticks21 = []
    for i in np.arange(len(grades)):
        xticks21.append("{} ({})".format(grades[i], grade_char_count[i]))

    axis21.set_xticks(np.arange(1, len(grades) + 1))
    axis21.set_xticklabels(xticks21, rotation=30)

    # Avoid output from set_xticklabels
    data = container2
    x_ticks = np.arange(1, len(grades) + 1)
    x_label = xticks21

    res = list()
    for i, j, k in zip(data, x_label, x_ticks):
        i.sort()
        res.append(dict(
            highest=int(max(i)),
            lowest=int(min(i)),
            open=int(np.percentile(i, 25)),
            close=int(np.percentile(i, 75)),
            strokes=j,
        ))
    return res


def box_3():
    raw_radicals = [ast.literal_eval(res).keys() for res in raw['radicals'].unique()]

    # pick only the first character of those radicals
    radicals = [list(x)[0][0] for x in raw_radicals]
    radicals
    # Initialization
    container3 = {}
    radical_char_count = []

    # For each radical
    for rad in np.arange(len(radicals)):
        # Locate all rows with that radical
        raw_in_radnum = raw[[(x.find(radicals[rad]) != -1) for x in raw['radicals']]]

        # Count the number of kanjis with that radical
        radical_char_count.append(raw_in_radnum["radicals"].count())

        # Append to container dictionary. Key is the radical, value is a list of frequencies of kanjis with that radical
        container3[radicals[rad]] = list(raw_in_radnum['frequency'].dropna())

    #
    # Combine them into 2-tuples
    container32 = [(x, container3[x]) for x in container3.keys()]

    # Sorting function
    def sort_key(x):
        a, b = x
        return -len(b)

    f = sort_key

    # Sort the list
    container32.sort(key=f)

    # Unzip them into separate lists
    rad_sorted, freq_sorted = zip(*container32)
    import matplotlib.font_manager as mfm

    font_path = "simhei.ttf"
    prop = mfm.FontProperties(fname=font_path)

    # Add figure and axis
    fig3 = plt.figure(figsize=(12, 9))
    axis31 = fig3.add_subplot(1, 1, 1)

    # Box plot
    axis31.boxplot(freq_sorted[:20])

    # Title, xlabel, ylabel
    axis31.set_title("Group of Radicals (X) - rank of frequency (Y)", fontsize="large")
    axis31.set_xlabel("Most frequently used 20 Radicals (count of characters with that radical)", fontsize="large")
    axis31.set_ylabel("rank of frequency used in newspaper", fontsize="large")

    # Xticks, labels
    xticks31 = []
    for i in np.arange(20):
        xticks31.append("{} ({})".format(rad_sorted[i], len(freq_sorted[i])))

    axis31.set_xticks(np.arange(1, 21))
    axis31.set_xticklabels(xticks31, rotation=45, fontdict={'fontproperties': prop, 'fontsize': 14})

    # avoid output from set_xticklabels
    data = freq_sorted[:20]
    x_ticks = np.arange(1, 24)
    x_label = xticks31
    res = list()
    for i, j, k in zip(data, x_label, x_ticks):
        i.sort()
        res.append(dict(
            highest=int(max(i)),
            lowest=int(min(i)),
            open=int(np.percentile(i, 25)),
            close=int(np.percentile(i, 75)),
            strokes=j,
        ))
    return res


def chart_4():
    raw_grades = raw["grade"].unique()

    # List of all JLPT levels
    jlpt = ['N5', 'N4', 'N3', 'N2', 'N1']
    grades = np.sort(raw_grades[:-1])

    # Initialization
    container4 = []

    jlpt_char_count = []
    grade_char_count = []

    # For all grades
    for gradenum in np.arange(len(grades)):
        # locate all rows with that grade
        raw_in_gradenum = raw[raw["grade"] == grades[gradenum]]

        # count the number of kanjis taught in that grade
        grade_char_count.append(raw_in_gradenum["frequency"].count())
    # For each JLPT level
    for jlptnum in np.arange(len(jlpt)):
        # Locate all kanjis with that JLPT level
        raw_in_jlptnum = raw[raw["jlpt"] == jlpt[jlptnum]]

        # Count the number of kanjis with that JLPT level
        jlpt_char_count.append(raw_in_jlptnum["frequency"].count())

        # Append those kanjis' frequencies to the container
        container4.append(list(raw_in_jlptnum['frequency'].dropna()))

    # This part contains two axis comparisons: The Grades in part 2 ('grade 1, grade 2, etc.') and JLPT levels done above
    fig4 = plt.figure(figsize=(12, 4))
    axis41 = fig4.add_subplot(1, 2, 1)
    # Grades: bar plot of kanjis studied in that grade
    axis41.bar(np.arange(len(grades)), grade_char_count, alpha=0.5, color="blue", label='Kanjis learned in that grade')

    # Grades: plot of cumulative kanjis learned from grade 1
    axis41.plot(np.array(grade_char_count).cumsum(), color="green", label='cumulative Kanjis learned')

    # Titles etc.
    axis41.set_title("Grades (X) - number of Kanji learned(Y)", fontsize="large")
    axis41.set_xlabel("Grades", fontsize="large")
    axis41.set_ylabel("rank of frequency used in newspaper", fontsize="large")

    xticks41 = []
    for i in np.arange(len(grades)):
        xticks41.append("{} ({})".format(grades[i], grade_char_count[i]))

    axis41.set_xticks(np.arange(len(grades)))
    axis41.set_xticklabels(xticks41, rotation=30)
    axis41.legend(loc='best')

    # Axis 2: kanjis and JLPT levels
    axis42 = fig4.add_subplot(1, 2, 2)

    # JLPT: bar plot of kanjis studied in that level
    axis42.bar(np.arange(len(jlpt)), jlpt_char_count, alpha=0.5, color="blue", label='Kanjis learned in that level')

    # JLPT: plot of kanjis studied till that level
    axis42.plot(np.array(jlpt_char_count).cumsum(), color="green", label='cumulative Kanjis learned')

    # Titles etc.
    axis42.set_title("JLPT Level (X) - number of Kanji learned(Y)", fontsize="large")
    axis42.set_xlabel("JLPT Level", fontsize="large")
    axis42.set_ylabel("rank of frequency used in newspaper", fontsize="large")

    xticks42 = []
    for i in np.arange(len(jlpt)):
        xticks42.append("{} ({})".format(jlpt[i], jlpt_char_count[i]))

    axis42.set_xticks(np.arange(len(jlpt)))
    axis42.set_xticklabels(xticks42, rotation=30)
    axis42.legend(loc='best')


if __name__ == '__main__':
    print(box_1())