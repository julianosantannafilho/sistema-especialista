def choose_car_category():
    score = {
        'aventureiro compacto' : 0,
        'hatch subcompacto' : 0, 'hatch compacto' : 0, 'hatch médio' : 0,
        'sedã compacto' : 0, 'sedã médio' : 0, 'sedã grande' : 0,
        'familiar compacto' : 0, 'familiar médio' : 0, 'familiar grande' : 0,
        'picape compacta' : 0, 'picape média' : 0, 'picape grande' : 0,
        'suv compacto' : 0, 'suv médio' : 0, 'suv grande' : 0,
        'esportivo compacto' : 0, 'esportivo médio' : 0, 'esportivo grande' : 0,
        'conversível compacto' : 0, 'conversível médio' : 0, 'conversível grande' : 0,
        'van média' : 0, 'van grande' : 0,
        'jipe' : 0,
        'furgão compacto' : 0, 'furgão médio' : 0,
        'caminhão urbano' : 0
    }

    questions_offroad = [
        "Você deseja um carro com foco offroad?(s/n)",
        "Vai ser usado para trilhas e terrenos extremos?(s/n)",
        "Dinheiro ou conveniência é um problema?(s/n)",
        "É necessário grande capacidade de carga?(s/n)",
        "Há necessidade de no mínimo 4 lugares?(s/n)",
        "Você gosta do estilo picape?(s/n)"

    ]
    
    answers = []
    for i, question in enumerate(questions_offroad):
        answer = input(question).strip().lower()
        answers.append(answer)

        if i == 0:
            if answer == 's':
                score['aventureiro compacto'] += 1
                score['picape compacta'] += 1
                score['picape média'] += 1
                score['picape grande'] += 1
                score['jipe'] += 1
        elif i == 1:
            if answer == 's':
                score['jipe'] += 1
        elif i == 2:
            if answer == 's':
                score['aventureiro compacto'] += 1
                score['picape compacta'] += 1
                score['picape média'] += 1
        elif i == 3:
            if answer == 's':
                score['picape média'] += 1
                score['picape grande'] += 1
        elif i == 4:
            if answer == 's':
                score['aventureiro compacto'] += 1
        elif i == 5:
            if answer == 's':
                score['picape compacta'] += 1
                score['picape média'] += 1
                score['picape grande'] += 1

    chosen_category = max(score, key = score.get)

    print(f"A categoria que melhor combina com você é: {chosen_category.capitalize()}")
choose_car_category()