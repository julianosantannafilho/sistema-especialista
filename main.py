def choose_car_category():
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

    questions_offroad = [
        "Você deseja um carro com foco offroad?(s/n)",
        "Vai ser usado para trilhas e terrenos extremos?(s/n)",
        "Dinheiro ou conveniência é um problema?(s/n)",
        "É necessário grande capacidade de carga?(s/n)",
        "Há necessidade de no mínimo 4 lugares?(s/n)",
        "Você gosta do estilo picape?(s/n)"
    ]

    questions_asphalt = [
        "Você quer um carro para asfalto?(s/n)",
        "Você prefere um carro esportivo?(s/n)",
        "Será necessário carregar alguma carga comercial?(s/n)",
        "Será usado para cargas pesadas?(ex: materiais de construção)(s/n)",
        "Será usado para cargas leves?(ex: correios, encomendas, delivery)(s/n)",
        "Prefere veículos pequenos?(s/n)",
        "Prefere veículos médios?(s/n)",
        "Prefere veículos grandes?(s/n)",
        "Precisa ser um veículo conveniente para cidades?(s/n)",
        "Precisa ser um veículo voltado para viagens longas?(s/n)",
        "Vai ser transportado regularmente com vários passageiros?(s/n)",
        "Seu orçamento é grande?(s/n)",
        "Prefere carros conversíveis?(s/n)",
        "Precisa ter um porta-malas grande?(s/n)",
        "Precisa ser um carro grande ou luxuoso?(s/n)",
        "Será utilizado comercialmente com transporte de pessoas?(s/n)",
        "Gostaria de um carro exclusivo e único?(s/n)",
        "Precisa ter um perfil mais alto?(s/n)",
        "Você prefere veículos estilo perua ou station wagon?(s/n)",
        "Seu orçamento é pequeno?(s/n)",
        "Precisa ter espaço para mais de duas pessoas?(s/n)"
    ]

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
                    score['picape média'] +=  1
                    score['picape grande'] += 1
                elif i == 4 and answer == 's':
                    score['aventureiro compacto'] += 1
                elif i == 5 and answer == 's':
                    score['picape compacta'] += 1
                    score['picape média'] += 1
                    score['picape grande'] += 1
            else:
                if i == 0 and answer == 's':
                    score['hatch subcompacto'] += 1
                    score['hatch compacto'] += 1
                    score['hatch médio'] += 1
                    score['sedã compacto'] += 1
                    score['sedã médio'] += 1
                    score['sedã grande'] += 1
                    score['familiar compacto'] += 1
                    score['familiar médio'] += 1
                    score['familiar grande'] += 1
                    score['suv compacto'] += 1
                    score['suv médio'] += 1
                    score['suv grande'] += 1
                    score['esportivo compacto'] += 1
                    score['esportivo médio'] += 1
                    score['esportivo grande'] += 1
                    score['conversível compacto'] += 1
                    score['conversível médio'] += 1
                    score['conversível grande'] += 1
                    score['van média'] += 1
                    score['van grande'] += 1
                    score['furgão compacto'] += 1
                    score['furgão médio'] += 1
                    score['caminhão urbano'] += 1
                elif i == 1 and answer == 's':
                    score['esportivo compacto'] += 1
                    score['esportivo médio'] += 1
                    score['esportivo grande'] += 1
                elif i == 2 and answer == 's':
                    score['furgão compacto'] += 1
                    score['furgão médio'] += 1
                    score['caminhão urbano'] += 1
                elif i == 3 and answer == 's':
                    score['caminhão urbano'] += 1
                elif i == 4 and answer == 's':
                    score['furgão compacto'] += 1
                    score['furgão médio'] += 1
                elif i == 5 and answer == 's':
                    score['hatch subcompacto'] += 1
                    score['hatch compacto'] += 1
                    score['sedã compacto'] += 1
                    score['familiar compacto'] += 1
                    score['suv compacto'] += 1
                    score['esportivo compacto'] += 1
                    score['conversível compacto'] += 1
                    score['furgão compacto'] += 1
                elif i == 6 and answer == 's':
                    score['hatch médio'] += 1
                    score['sedã médio'] += 1
                    score['familiar médio'] += 1
                    score['suv médio'] += 1
                    score['esportivo médio'] += 1
                    score['conversível médio'] += 1
                    score['van média'] += 1
                    score['furgão médio'] += 1
                elif i == 7 and answer == 's':
                    score['sedã grande'] += 1
                    score['familiar grande'] += 1
                    score['suv grande'] += 1
                    score['esportivo grande'] += 1
                    score['conversível grande'] += 1
                    score['van grande'] += 1
                    score['caminhão urbano'] += 1
                elif i == 8 and answer == 's':
                    score['hatch subcompacto'] += 1
                    score['hatch compacto'] += 1
                    score['hatch médio'] += 1
                    score['sedã compacto'] += 1
                    score['esportivo compacto'] += 1
                    score['conversível compacto'] += 1
                elif i == 9 and answer == 's':
                    score['sedã médio'] += 1
                    score['sedã grande'] += 1
                    score['familiar compacto'] += 1
                    score['familiar médio'] += 1
                    score['familiar grande'] += 1
                    score['suv compacto'] += 1
                    score['suv médio'] += 1
                    score['suv grande'] += 1
                    score['esportivo médio'] += 1
                    score['esportivo grande'] += 1
                    score['conversível médio'] += 1
                    score['conversível grande'] += 1
                elif i == 10 and answer == 's':
                    score['sedã grande'] += 1
                    score['familiar compacto'] += 1
                    score['familiar médio'] += 1
                    score['familiar grande'] += 1
                    score['suv médio'] += 1
                    score['suv grande'] += 1
                    score['van média'] += 1
                    score['van grande'] += 1
                elif i == 11 and answer == 's':
                    score['sedã grande'] += 1
                    score['suv grande'] += 1
                    score['familiar grande'] += 1
                    score['esportivo compacto'] += 1
                    score['esportivo médio'] += 1
                    score['esportivo grande'] += 1
                    score['conversível compacto'] += 1
                    score['conversível médio'] += 1
                    score['conversível grande'] += 1
                elif i == 12 and answer == 's':
                    score['conversível compacto'] += 1
                    score['conversível médio'] += 1
                    score['conversível grande'] += 1
                elif i == 13 and answer == 's':
                    score['sedã grande'] += 1
                    score['familiar compacto'] += 1
                    score['familiar médio'] += 1
                    score['familiar grande'] += 1
                    score['suv médio'] += 1
                    score['suv grande'] += 1
                    score['furgão compacto'] += 1
                    score['furgão grande'] += 1
                elif i == 14 and answer == 's':
                    score['sedã grande'] += 1
                    score['familiar grande'] += 1
                    score['suv grande'] += 1
                    score['esportivo médio'] += 1
                    score['esportivo grande'] += 1
                    score['conversível médio'] += 1
                    score['conversível grande'] += 1
                elif i == 15 and answer == 's':
                    score['van média'] += 1
                    score['van grande'] += 1
                elif i == 16 and answer == 's':
                    score['esportivo médio'] += 1
                    score['esportivo grande'] += 1
                    score['conversível grande'] += 1
                elif i == 17 and answer == 's':
                    score['s uv compacto'] += 1
                    score['suv médio'] += 1
                    score['suv grande'] += 1
                elif i == 18 and answer == 's':
                    score['familiar compacto'] += 1
                    score['familiar médio'] += 1
                    score['familiar grande'] += 1
                elif i == 19 and answer == 's':
                    score['hatch compacto'] += 1
                    score['sedã compacto'] += 1
                    score['suv compacto'] += 1
                    score['familiar compacto'] += 1
                    score['furgão compacto'] += 1
                elif i == 20 and answer == 's':
                    score['hatch compacto'] += 1
                    score['hatch médio'] += 1
                    score['sedã compacto'] += 1
                    score['sedã médio'] += 1
                    score['sedã grande'] += 1
                    score['familiar compacto'] += 1
                    score['familiar médio'] += 1
                    score['familiar grande'] += 1
                    score['suv compacto'] += 1
                    score['suv médio'] += 1
                    score['suv grande'] += 1
                    score['conversível médio'] += 1
                    score['conversível grande'] += 1

    first_question_answer = input(questions_offroad[0]).strip().lower()

    if first_question_answer == 's':
        process_questions(questions_offroad[1:], True)
    else:
        process_questions(questions_asphalt, False)

    max_score = max(score.values())
    best_fits = [category for category, score_value in score.items() if score_value == max_score]

    if len(best_fits) > 1:
        print("Essas são suas melhores escolhas:")
        for fit in best_fits:
            print(f"- {fit.capitalize()}")
    else:
        chosen_category = best_fits[0]
        print(f"A categoria que melhor combina com você é: {chosen_category.capitalize()}")

choose_car_category()