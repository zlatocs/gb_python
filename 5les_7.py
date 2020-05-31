import json
result = []
with open('my_ex7.json','w') as write_f:
    with open('text_7.txt', encoding='utf-8') as f_obj:
        profit = {}
        for line in f_obj:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        avr_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({'avr_profit': round(avr_profit)})
    json.dump(result,write_f)
