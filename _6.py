# Напишіть клас Person, який містить наступну інформацію: прізвище, ім’я, по-батькові та дата народження людини. В
# класі створіть метод, який по заданій даті народження виводитиме повну кількість років людини. Напишіть клас
# Candidate, який наслідуватиме Person і доповнюватиме його наступною інформацією про кандидата у депутати: номер
# округу, кількість виборців в окрузі, кількість виборців, що проголосувала за кандидата, партійна приналежність. Для
# заданої партії знайдіть кандидата, за якого віддали голоси найбільший процент виборців та знайдіть найстаршого
# кандидата серед усіх, хто подолав 50%.

from datetime import datetime


class Person:
    def __init__(self, first_name, middle_name, last_name, birth_date):
        self.first_name = str(first_name)
        self.middle_name = str(middle_name)
        self.last_name = str(last_name)
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y")

    def get_age(self):
        return int((datetime.now() - self.birth_date).days / 365.25)

    def __str__(self):
        return " ".join([self.first_name, self.middle_name, self.last_name])


class Candidate(Person):
    def __init__(self, first_name, middle_name, last_name, birth_date, district, electorate, votes, party):
        super().__init__(first_name, middle_name, last_name, birth_date)
        self.district = int(district)
        self.electorate = int(electorate)
        self.votes = int(votes)
        if self.votes > self.electorate:
            self.votes = self.electorate

        self.party = str(party)


def get_the_best(candidates):
    """
    Повертає найкращого кандидата. По відсотку голосів.
    :param candidates:
    :return:
    """
    result = candidates[0]
    percent = result.votes / result.electorate
    for i in candidates:
        current = i.votes / i.electorate
        if current > percent:
            percent = current
            result = i
    return result


def get_oldest(candidates):
    """
    Повертає найстаршого кандидата
    :param candidates:
    :return:
    """
    result = candidates[0]
    max = result.get_age()
    for i in candidates:
        current = i.get_age()
        if current > max:
            max = current
            result = i
    return result


def get_more_than(candidates, percent=0.5):
    """
    Повертає кандидатів у яких процен голосів більше ніж деяке число(0.5 == 50%)
    :param candidates:
    :param percent:
    :return:
    """
    result = []
    for i in candidates:
        if i.votes / i.electorate >= percent:
            result.append(i)
    return result


if __name__ == '__main__':
    putin = Candidate("Vladimir", "Vladimirovich", "Putin", "06-04-1964", 1, 1000, 1200, "Edinaya Rosiya")
    poroshenko = Candidate("Poroshenko", "Ivan", "Ivanovuch", "07-05-1910", 10, 1000, 1100, "Roshen")
    tamara = Candidate("Tamara", "Prosto", "Tamara", "21-09-1997", 1, 12, 4, "Tamara")
    #Додаш сама.

    all = [putin, poroshenko, tamara]
    print("за якого віддали голоси найбільший процент виборців:" + str(get_the_best(all)))
    print("знайдіть найстаршого кандидата серед усіх, хто подолав 50%.", str(get_oldest(get_more_than(all))))