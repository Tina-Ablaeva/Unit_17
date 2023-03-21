per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую планируете внести в банк: "))
m_new = money/100
deposit = [int(per_cent.get("ТКБ")*m_new), int(per_cent.get("СКБ")*m_new),
           int(per_cent.get("ВТБ")*m_new), int(per_cent.get("СБЕР")*m_new)]
print("Ставки, которые предлагают банки на сегодняшний день: ", list(per_cent.values()))
print("Доход, который будет получен от размещения средств:   ", deposit)
print("При внесении", money, "максимальная выгода от размещения составит: ", max(deposit))