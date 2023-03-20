def load():
    global client_info
    with open("client_info.json", "r", encoding="utf-8") as json_file:
        client_info = json.load(json_file)

def save(info: dict):
    with open("client_info.json", "w", encoding=" utf-8") as json_file:
        json.dump(info, json_file)

def show_info():
    load()
    print("Информация о счетах:")
    print("----------------------------------")
    for info in text["accounts"]:
       print("Имя:", info["name"])
       print("Платежная система:", info["system"])
       print("Номер:", info["number"])
       print("Тип:", info["type"])
       print("Баланс:", info["balance"])
       print("Срок действия:", info["validity period"])
       print("----------------------------------")
show_info()




def predict():
    with open("client_info.json", "r", encoding="utf-8") as json_file:
        text = json.load(json_file)

    global income_len
    global client_info

    expenses_len = 0
    income_len = 0
    expenses = 0
    income = 0
    months = []
    load()

    for transaction in text['transactions']:
        if transaction["type"] == "списание":
            expenses += transaction["amount"]

        if transaction["type"] == "зачисление":
            income += transaction["amount"]

        if transaction["date"] not in months:
            months.append(transaction["date"])

    print("Предполагаемые расходы в следующем месяце:", expenses / len(months))
    print("Предполагаемые доходы в следующем месяце:", income / len(months))
