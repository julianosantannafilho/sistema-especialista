def choose_car_category():
    # Score dictionary for both categories
    score = {
        'aventureiro compacto': 0,
        'hatch subcompacto': 0, 'hatch compacto': 0, 'hatch médio': 0,
        'sedã compacto': 0, 'sedã médio': 0, 'sedã grande': 0,
        'familiar compacto': 0, 'familiar médio': 0, 'familiar grande': 0,
        'picape compacta': 0, 'picape média': 0, 'picape grande': 0,
        'suv compacto': 0, 'suv médio': 0, 'suv grande': 0,
        'esportivo compacto': 0, 'esportivo médio': 0, 'esportivo grande': 0,
        'conversível compacto': 0, 'conversível médio': 0, 'conversível grande': 0,
        'van média': 0, 'van grande': 0,
        'jipe': 0,
        'furgão compacto': 0, 'furgão médio': 0,
        'caminhão urbano': 0
    }

    # Questions for off-road vehicles
    questions_offroad = [
        "Você deseja um carro com foco offroad?(s/n)",
        "Vai ser usado para trilhas e terrenos extremos?(s/n)",
        "Dinheiro ou conveniência é um problema?(s/n)",
        "É necessário grande capacidade de carga?(s/n)",
        "Há necessidade de no mínimo 4 lugares?(s/n)",
        "Você gosta do estilo picape?(s/n)"
    ]

    # Questions for tarmac-centered vehicles
    questions_tarmac = [
        "Você deseja um carro com foco em estrada?(s/n)",
        "Você prefere conforto em vez de performance?(s/n)",
        "Você viaja longas distâncias com frequência?(s/n)",
        "Você precisa de um carro econômico?(s/n)",
        "Você considera a estética do carro importante?(s/n)",
        "Você prefere um carro esportivo?(s/n)"
    ]

    # Function to process questions and scoring
    def process_questions(questions, is_offroad):
        for i, question in enumerate(questions):
            answer = input(question).strip().lower()
            if is_offroad:
                if i == 0 and answer == 's':
                    score['aventureiro compacto'] += 1
                    score['picape compacta'] += 1
                    score['picape média'] += 1
                    score['picape grande'] += 1
                    score['jipe'] += 1
                elif i == 1 and answer == 's':
                    score['jipe'] += 1
                elif i == 2 and answer == 's':
                    score['aventureiro compacto'] += 1
                    score['picape compacta'] += 1
                    score['picape média'] += 1
                elif i == 3 and answer == 's':
                    score['picape média'] += 1
                    score['picape grande'] += 1
                elif i == 4 and answer == 's':
                    score['aventureiro compacto'] += 1
                elif i == 5 and answer == 's':
                    score['picape compacta'] += 1
                    score['picape média'] += 1
                    score['picape grande'] += 1
            else:
                if i == 0 and answer == 's':
                    score['hatch compacto'] += 1
                    score['sedã médio'] += 1
                elif i == 1 and answer == 's':
                    score['sedã grande'] += 1
                elif i == 2 and answer == 's':
                    score['familiar grande'] += 1
                elif i == 3 and answer == 's':
                    score['hatch subcompacto'] += 1
                elif i == 4 and answer == 's':
                    score['sedã compacto'] += 1
                elif i == 5 and answer == 's':
                    score['esportivo compacto'] += 1

    # Ask the first question to determine the path
    first_question_answer = input(questions_offroad[0]).strip().lower()

    if first_question_answer == 's':
        # Process all off-road questions if the answer is 'yes'
        process_questions(questions_offroad[1:], True)
    else:
        # Process all tarmac-centered questions if the answer is 'no'
        process_questions(questions_tarmac, False)

    # Determine the best fit
    chosen_category = max(score, key=score.get)

    print(f"A categoria que melhor combina com você é: {chosen_category.capitalize()}")

choose_car_category()