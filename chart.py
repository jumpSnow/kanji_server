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
    title = "Number of strokes (X) - rank of frequency(Y)"
    x = "Number of strokes (count of characters)"
    y = "Rank of frequency used in newspaper"
    return dict(data=res, title=title, x_name=x, y_name=y)


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
    title = "Grades (X) - rank of frequency(Y)"
    x = "Grades (count of characters in grade)"
    y = "Rank of frequency used in newspaper"
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
    return dict(data=res, title=title, x_name=x, y_name=y)


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


def scatter(n):
    filename = "level_correlation_results.csv"
    df = pd.read_csv(filename)
    print(len(df))
    df.head()
    # Index and Unnamed: 0 are the Joyo ranking.
    # When using the Joyo ranking I use the Unnamed: 0 as the column, so the index should be irrelevant to this program.
    # TODO: maybe just remove Joyo analysis.

    # %%

    datasources = ["Twitter", "Aozora", "Wikipedia", "News"]
    # levelsources = ["wanikani_level"]
    kanjis = df["kanji"]

    # %%

    def createBins(numberOfBins, col):
        # Create a sorted version of the column.
        arr = []
        for value in col:
            arr.append(value)
        arr.sort()
        # qcut to get bin numbers for the column.
        #    Each column's kanji now has a numeric level equivalent based on frequency.
        #    This will allow us to compare bins, like N5 through N1 vs bins 1 through 5.
        bins = pd.qcut(arr, numberOfBins, labels=False)
        # Lets not start at 0, levels start at 1 for everything.
        bins += 1
        print("Created", len(bins), "bins: " + str(bins))
        return bins

    # %%

    # Col name should be the col of the dataframe with the levels,
    #    translator translates those level strings to integer levels from 1..max_level, inclusive,
    #        Ex: "N5" translator should say is 1, while "N1" should be 5. (lowest to highest difficulty)
    #    max_level is how many levels, like 60 for WaniKani's 1..60 system, or 5 for JLPT.
    def getAvgLevelDiff(level_col_name, translator, max_level):
        results = []
        for sourceName in datasources:
            bins = createBins(max_level, df["Rank of Appearances on " + sourceName])
            rankLevel_col = pd.DataFrame(bins)
            rankLevel_col.columns = ["Rank Converted to Level"]
            new_df = df.join(rankLevel_col)
            numberOfComparisons = 0
            numberOfLevelDifference = 0
            for kanji in kanjis:
                row = new_df[kanjis == kanji].iloc[0]
                colValue = row[level_col_name]
                # We need a numeric representation of the level, which our caller will define
                colLevel = translator(colValue)
                # I should maybe separate into 60 bins for comparison.
                # Then take the average "level" number compared with the waniLevel?
                # rank = row["Rank of Appearances on "+sourceName]
                # print("rank="+str(rank))
                rankLevel = row["Rank Converted to Level"]
                # print("rankLevel="+str(rankLevel))
                diff = abs(colLevel - rankLevel)
                if (not np.isnan(diff)):
                    numberOfComparisons += 1
                    numberOfLevelDifference += diff
                    # print("Adding diff "+str(diff)+" because wkl="+str(waniLevel)+" versus rankLevel="+str(rankLevel))
            averageLevelDifference = numberOfLevelDifference / numberOfComparisons
            results.append(averageLevelDifference)
            print(sourceName + " vs " + level_col_name + " average level difference=" + str(averageLevelDifference))
        return results

    # %%

    # How strongly does WaniKani level corrolate with each source?
    # WaniKani levels range from 1 to 60, with higher being harder (or rather, learned later. Harder or more obscure.).
    intIsJustItself = lambda x: x
    wani_levels = 60
    wani_results = getAvgLevelDiff("wanikani_level", intIsJustItself, wani_levels)

    # %%

    # How strongly does JLPT level corrolate with each source?
    # Low N# means higher level. Scale of N1 to N5.
    levelValues = {"N" + str(i): (5 + 1) - i for i in range(1, 5 + 1)}
    print(levelValues)
    print(type(levelValues))

    def translateJLPT(levelStr):
        try:
            return levelValues[levelStr]
        except:
            return float('nan')

    print(translateJLPT("N1"))
    JLPT_levels = 5
    JLPT_results = getAvgLevelDiff("jlpt", translateJLPT, JLPT_levels)

    # %%

    # How strongly does grade level corrolate with each source?
    print(df["grade"].unique())
    gradeLevels = {
        'grade 1': 1,
        'grade 2': 2,
        'grade 3': 3,
        'grade 4': 4,
        'grade 5': 5,
        'grade 6': 6,
        'junior high': 7,
    }

    def translateGradeLevel(levelStr):
        try:
            return gradeLevels[levelStr]
        except:
            return float('nan')

    grade_levels = 7
    grade_results = getAvgLevelDiff("grade", translateGradeLevel, grade_levels)

    # %%

    # How strongly does Jisho frequency level corrolate with each source?
    print(max(df["frequency"].unique()))  # Ranges from 1 to 2495. So it's including more entries than joyo.
    jisho_levels = 2495
    # See comment on Joyo below. Bugged, and not really meaningful anyway.
    # jisho_results = getAvgLevelDiff("frequency", intIsJustItself, jisho_levels)

    # %%

    # How strongly does Joyo rank corrolate with each source?
    # TODO should really just rename that column.
    print(max(df["Unnamed: 0"].unique()))  # Ranges from 0 to 2135.
    joyo_levels = 2136

    # We need level numbers to be 1..joyo_levels, inclusive
    def translateJoyo(x):
        try:
            return x + 1
        except:
            return float('nan')

    # Those bins look a little weird? Why's it using e^0 to e^3?
    #    Each bin should correspond to a level number. We have more levels than bins though so something's wrong here.
    # But really, these results aren't useful anyway since you don't learn by Joyo ranking. Same with Jisho.
    # joyo_results = getAvgLevelDiff("Unnamed: 0", translateJoyo, joyo_levels)

    # %%

    # How strongly does Genki frequency level corrolate with each source?
    # max isn't working on this? NaN throwing it off ?
    possibleGenkiValues = df["Genki_Lesson"].unique()
    possibleGenkiValues.sort()
    print(possibleGenkiValues)

    genki_levels = 0
    for value in df["Genki_Lesson"].unique():
        if (not np.isnan(value)):
            genki_levels += 1
    print(genki_levels, "possible valid values.")

    # It looks like there is no lesson before lesson 3. A consequence of our source?
    # http://genki.japantimes.co.jp/self/genki-kanji-list-linked-to-wwkanji
    # We need level numbers to be 1..genki_levels, inclusive
    def translateGenki(x):
        try:
            return x - 2
        except:
            return float('nan')

    # Test that we get 1..genki_levels
    print("1 =?=", translateGenki(3))
    print(genki_levels, "=?=", translateGenki(23))
    genki_results = getAvgLevelDiff("Genki_Lesson", translateGenki, genki_levels)

    # %%

    # Now compare them. If I want to read Twitter, what's the best option to learn? Wikipedia? Etc.
    # Note that there is some inherent inaccuracy/rounding with 5 levels versus 60, need to take that into account.
    results = [(wani_results, wani_levels, "WaniKani"),
               (JLPT_results, JLPT_levels, "JLPT"),
               (grade_results, grade_levels, "Grade"),
               # (jisho_results, jisho_levels, "Jisho"), #This is frequency, not really a sequence you'd learn.
               # (joyo_results, joyo_levels, "Jōyō"),  #This is a ranking system, not very relevant.
               (genki_results, genki_levels, "Genki")]
    # String for datasource name, string for best sequence, float for % match.
    best_sequence_for_sources = {datasources[i]: ("Name of best sequence goes here", 1.0)
                                 for i in range(len(datasources))}

    # TODO I really should just use a dataframe from the start
    percent_results_of_each_source = [[], [], [], []]
    # Could also do it based on each sequence, might be more useful since we're picking a sequence?
    # percent_results_of_each_sequence = [[]]
    for (result, level, name) in results:
        i = 0
        for datasource in datasources:
            correlationWithThisSource = result[i]
            correlationWithThisSource = correlationWithThisSource / level
            percent_results_of_each_source[i].append(correlationWithThisSource)
            print(datasource, name, correlationWithThisSource)
            # For now I'll just take the lowest percent, TODO figure out how to deal with inaccuracy later.
            #    Maybe just say each has some +- inaccuracy based on number of levels.
            if (best_sequence_for_sources[datasource][1] > correlationWithThisSource):
                new_tup = (name, correlationWithThisSource)
                best_sequence_for_sources[datasource] = new_tup
            i = i + 1

    result_df = pd.DataFrame(percent_results_of_each_source)
    result_df.columns = [name for (_, _, name) in results]
    result_df.index = [source for source in datasources]
    print(result_df)

    print("")
    print("Results: ")
    for result in best_sequence_for_sources:
        print("Best for learning to read", result, ": ",
              best_sequence_for_sources[result][0],
              "with" + " {:.2f}".format(best_sequence_for_sources[result][1] * 100),
              "% inaccuracy compared to actual usage on", result)
    # The most levels are the most accurate right now. Joyo has perfect coverage obviously. Looks like Jisho also does.
    # Why are they all around 32-36%? Consequence of only using joyo?
    #    I guess it's a reasonable variation, these systems weren't chosen randomly, but can't perfectly model use.
    # Also we only have the WaniKani/JLPT/Genki/etc data for the Joyo set, results might vary with more than the 2136.
    #  Also maybe even ignore rank and just consider # appearances?

    # Is Genki very good to consider? So little coverage. Additional metric to display?

    # %% md

    # https://stackoverflow.com/a/43348337
    import matplotlib.ticker as ticker
    # Currently this xaxis function is unused, doesn't work for scatter plot or something.
    # Turn the x axis into names of sources
    def formatterX(x, pos):
        # The name of the data source
        return results[x][2]
        # if(x >= 1 and x <= 4):
        #    return datasources[x-1]
        # This shouldn't occur. Maybe print a warning but it'd be pretty noticeable.
        # return x

    # Translate 0.0 to 1.0 to 0.0 to 100.0
    # Long floating points is an issue.
    # Maybe force the y axis to use nice round numbers? 0, 10, 20...
    #    Maybe we won't end up using this type of chart though.
    def formatterY(y, pos):
        return y * 100

    fig = plt.figure(figsize=(13, 10))

    dataX = [i for i in range(0, len(results))]
    dataY = []
    for source in datasources:
        dataYPiece = [val for val in result_df.loc[source]]
        dataY.append(dataYPiece)
    sequence_names = [val[2] for val in results]
    # Only need colors if I show them all on the same vertical line.
    # colors = ["black", "blue", "red", "green"]
    # correspondingColors = [colors[0] for i in range(1, 4*4+1)]

    for ax_index in range(0, len(datasources)):
        ax = fig.add_subplot(2, 2, ax_index + 1)
        ax.scatter(dataX, dataY[ax_index])
        props = {
            # Inaccuracy is a strange word to use here. If there were 4 levels and it was
            #    all off by 1 it'd be 25% "inaccuracy," right (should probably develop better tests, hard to
            #    verify these large calculations)? So more, the average difference in level.
            'title': 'Inaccuracy of learning ' + datasources[ax_index] + ' using each sequence',
            'ylabel': 'Percent of inaccuracy'
        }
        ax.set(**props)
        plt.xticks(range(len(results)), sequence_names, size='medium')
    # plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(formatterX))#Doesn't work for scatter plot?
    # plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatterY))

    # fig.subplots_adjust(wspace=0, hspace=0)
    # Prevent overlap
    data = datasources[n]
    data_x = dataX
    data_y = dataY[n]
    res = list()
    for i, j, k in zip(data, data_x, data_y):
        i.sort()
        res.append(dict(
            highest=int(max(i)),
            lowest=int(min(i)),
            open=int(np.percentile(i, 25)),
            close=int(np.percentile(i, 75)),
            strokes=j,
        ))
    return res


if __name__ == '__main__':
    print(scatter(1))
