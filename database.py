import sqlite3
import ast


class DataBase:

    def __init__(self):
        self.conn = sqlite3.connect('ex1')
        self.cursor = self.conn.cursor()

    def kanji(self):
        jlpt_hard = {"N1": 5, "N2": 4, "N3": 3, "N4": 2, "N5": 1, "": 0}
        self.cursor.execute('''SELECT kanji, jlpt, wanikani_level FROM kanji''')
        kanji_list = dict()
        hard_list = list()
        res = self.cursor.fetchall()
        for i in res:
            wanikani = 0 if not i[2] else float(i[2])
            kanji_list[i[0]] = jlpt_hard.get(i[1]) + wanikani
            hard_list.append(jlpt_hard.get(i[1]) + wanikani)
        hard_list.sort()
        hard_list = [set(hard_list[i:i+214]) for i in range(0, len(hard_list), 214)]
        for i in kanji_list:
            for j in hard_list:
                if kanji_list[i] in j:
                    kanji_list[i] = hard_list.index(j)/2
        return kanji_list

    # def kanji_search(self, kanji):
    #     self.cursor.execute('''SELECT main_meaning, kun_readings, on_readings FROM kanji WHERE kanji == {}'''.
    #                         format(kanji))
    #
    #     return kanji_list

    def frequency(self):
        self.cursor.execute('''SELECT frequency FROM kanji''')
        data = self.cursor.fetchall()
        frequency_list = []
        for i in data:
            if not i:
                frequency_list.append(0)
            else:
                frequency_list.append(i)
        return frequency_list

    def strokes(self):
        self.cursor.execute('''SELECT strokes FROM kanji''')
        data = self.cursor.fetchall()
        strokes_list = [i[0] for i in data]
        return strokes_list

    def desc(self, kanji):
        self.cursor.execute('''SELECT main_meaning, kun_readings, on_readings FROM kanji WHERE kanji like '{}' '''
                            .format(kanji))
        data = self.cursor.fetchall()
        strokes_dict = dict()
        for i in data:
            meaning = ", ".join(i for i in i[0].strip('][').split(', '))
            kun = ast.literal_eval(i[1]) if i[1] else None
            kun = ", ".join(i for i in kun) if kun else None
            on = ast.literal_eval(i[2]) if i[2] else None
            on = ", ".join(i for i in on) if on else None
            strokes_dict.update({"name": kanji, "meaning": meaning, "kun": kun, "on": on})
        return strokes_dict

    def hard_level(self):
        jlpt_hard = {"N1": 5, "N2": 4, "N3": 3, "N4": 2, "N5": 1, "": 0}
        self.cursor.execute('''SELECT jlpt, wanikani_level FROM kanji''')
        hard_list = list()
        res = self.cursor.fetchall()
        for i in res:
            wanikani = 0 if not i[1] else float(i[1])
            hard_list.append(jlpt_hard.get(i[0]) + wanikani)
        hard_list.sort()
        hard_list = [set(hard_list[i:i+214]) for i in range(0, len(hard_list), 214)]
        return hard_list

    def data_table(self):
        kanji = self.kanji()
        frequency = self.frequency()
        strokes = self.strokes()
        res = list()
        for i, j, k in zip(kanji, frequency, strokes):
            res.append(dict(
                        name=i,
                        levels=kanji[i],
                        frequency=j,
                        strokes=k,
                        detail=0,
                       ))
        return res


if __name__ == '__main__':
    data = DataBase()
    # print(data.kanji())
    # print(data.frequency())
    # print(data.strokes())
    print(data.desc("逸"))

