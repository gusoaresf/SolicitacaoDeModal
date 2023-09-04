def realizar_login():
    print("Para iniciarmos é necessário realizar um login.\n")

    user = ""
    senha = ""

    while True: 
        opcao = input("Digite 1- caso já possua cadastro.\n"
            "Digite 2- para criar um cadastro.\n\n")
        
        if opcao == "1":
            if user == "" or senha == "":
                print()
                print("Você ainda não tem uma conta cadastrada. Selecione a outra opção!\n")
                continue
            input_user = input("Digite seu usuário: \n")
            input_senha = input("Digite sua senha: \n")
            if input_user == user and input_senha == senha:
                print("Login realizado com sucesso!")
                break
            else:
                print("Usuário ou senha incorretos.")

        elif opcao == "2":
            if user != "" or senha != "":
                print("Você já tem uma conta cadastrada.")
                continue
            print()
            user = input("Digite o nome de usuário: ")
            senha = input("Digite uma senha: ")
            senha2 = input("Digite novamente sua senha: ")
            
            while senha != senha2:
                print()
                print("As senhas não se conferem! Digite novamente. \n")
                senha = input("Digite uma senha: ")
                senha2 = input("Digite novamente sua senha: ")
            print()
            print("Conta criada com sucesso!\n")
            print(user + ", Seja bem-vindo à XXXXXX!")
            print()
            break
        else:
            print("Informação inválida, digite somente 1 ou 2.\n")

    return user, senha

def determinar_tipo_veiculo():
    while True:
        eixos = input("Digite quantos eixos possui seu veículo: ")
        print()
        if not eixos.isdigit():
            print("Informação incorreta. Digite apenas números correspondentes a quantidade de eixos de seu veículo!")
            print()
        else:
            eixos = int(eixos)
            if eixos > 2:
                print("Seu veículo é considerado de grande porte.")
                print()
                return "grande porte"
            else:
                print("Seu veículo é considerado de pequeno/médio porte.")
                print()
                return "pequeno/médio porte"

def escolha_usuario_encerramento():
    while True:
        escolha = input("Selecione uma opção:\n\n"
                        "1 - Encerrar atendimento!\n"
                        "2 - Continuar navegando no menu!\n\n")
        if escolha == "1":
            print("\nAgradecemos por utilizar nosso sistema de ajuda!")
            raise SystemExit
        elif escolha == "2":
            break
        else:
            print()
            print("Opção inválida, digite somente 1 ou 2.\n")

def lidar_com_problemas():

    tipo_veiculo = determinar_tipo_veiculo()

    localizacao_do_usuario = input("Para que podemos te ajudar, digite sua localização: ")

    while True:   
        print()
        escolha_usuario = input("Selecione o tipo de problema:\n\n"
                            "1 - Acidentes de trânsito\n"
                            "2 - Roubo ou furto\n"
                            "3 - Problema elétrico\n"
                            "4 - Problema mecânico\n"
                            "5 - Danos causados por fenômenos naturais\n"
                            "6 - Sair\n\n")                                
        
        if escolha_usuario == "1":
            while True:
                print()
                tipo_problemas = input("Selecione uma opção:\n\n"
                                    "1 - Verificar se há vítimas e prestar socorro\n"
                                    "2 - Registrar o acidente junto às autoridades\n"
                                    "3 - Acionar o seguro\n"
                                    "4 - Retornar para página anterior\n"
                                    "5 - Encerrar atendimento\n\n")
                if tipo_problemas == "1":
                    print()
                    print("Estamos enviando uma viatura particular para o endereço", localizacao_do_usuario, ". Iremos te fornecer todo suporte necessário!\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "2":
                    print()
                    print("Estamos acionando as autoridades e enviando nosso suporte para te auxiliar!\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "3":
                    print()
                    print("Estamos acionando o seguro para te ajudar com o acidente!\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "4":
                    break
                elif tipo_problemas == "5":
                    print()
                    print("Agradecemos por utilizar nosso sistema de ajuda!")
                    raise SystemExit
                else:
                    print()
                    print("Opção inválida. Por favor, selecione uma opção válida.")
                    
        if escolha_usuario == "2":
            while True:
                print()
                tipo_problemas = input("Selecione uma opção:\n\n"
                                    "1 - Registrar o roubo ou furto junto às autoridades\n"
                                    "2 - Acionar o seguro\n"
                                    "3 - Tomar medidas de segurança para evitar futuros roubos ou furtos\n"
                                    "4 - retornar para página anterior\n"
                                    "5 - Encerrar atendimento\n\n")
                if tipo_problemas == "1":
                    print()
                    print("Estamos registrando o roubo ou furto junto às autoridades!\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "2":
                    print()
                    print("Estamos acionando o seguro para te ajudar!\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "3":
                    print()
                    print("Algumas de nossas medidas são instalar alarmes, rastreadores e entre outros diversos meios. " 
                          "Traga seu veículo em uma de nossas concessionárias para tomarmos a melhor decissão\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "4":
                    break
                elif tipo_problemas == "5":
                    print()
                    print("Agradecemos por utilizar nosso sistema de ajuda!")
                    raise SystemExit
                else:
                    print()
                    print("Opção inválida. Por favor, selecione uma opção válida.")

        elif escolha_usuario == "3":
            while True:
                print()
                tipo_problemas = input("Selecione uma opção:\n\n"
                                    "1 - Verificar se há problemas na bateria ou no alternador\n"
                                    "2 - Verificar se há fusíveis queimados\n"
                                    "3 - Levar o veículo a um mecânico especializado\n"
                                    "4 - retornar para página anterior\n"
                                    "5 - Encerrar atendimento\n\n")
                if tipo_problemas == "1":
                    print()
                    print("Estamos a seu caminho para que possamos verificar se a bateria ou o alternador estão com problemas e fazer os reparos necessários.\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "2":
                    print()
                    print("Estamos a seu caminho para que possamos verificar se há fusíveis queimados e realizar a troca, caso necessário.\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "3":
                    print()
                    if tipo_veiculo == "grande porte":
                        print("Estamos encaminhando a sua localização um guincho para veículos de grande porte, "
                              "para que possamos levar o seu veículo a um mecânico especializado para diagnosticar e reparar o problema elétrico.\n")
                    else:
                        print("Estamos encaminhando a sua localização um guincho para veículos de pequeno/médio porte, "
                              "para que possamos levar o seu veículo a um mecânico especializado para diagnosticar e reparar o problema elétrico.\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "4":
                    break
                elif tipo_problemas == "5":
                    print()
                    print("Agradecemos por utilizar nosso sistema de ajuda!")
                    raise SystemExit
                else:
                    print()
                    print("Opção inválida. Por favor, selecione uma opção válida.")

        elif escolha_usuario == "4":
            while True:
                print()
                tipo_problemas = input("Selecione uma opção:\n\n"
                                    "1 - Verificar o óleo e o líquido de arrefecimento\n"
                                    "2 - Verificar os pneus e o sistema de suspensão\n"
                                    "3 - Levar o veículo a um mecânico especializado\n"
                                    "4 - retornar para página anterior\n"
                                    "5 - Encerrar atendimento\n\n")
                if tipo_problemas == "1":
                    print()
                    print("Estamos a seu caminho para que possamos verificar o nível e a qualidade do óleo e do líquido de arrefecimento e fazer os reparos necessários.\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "2":
                    print()
                    print("Estamos a seu caminho para que possamos verificar o estado dos pneus e do sistema de suspensão, e realizar os devidos reparos.\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "3":
                    print()
                    if tipo_veiculo == "grande porte":
                        print("Estamos encaminhando a sua localização um guincho para veículos de grande porte, "
                              "para que possamos levar o seu veículo a um mecânico especializado para diagnosticar e reparar o problema mecâmico.\n")
                    else:
                        print("Estamos encaminhando a sua localização um guincho para veículos de pequeno/médio porte, "
                              "para que possamos levar o seu veículo a um mecânico especializado para diagnosticar e reparar o problema mecâmico.\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "4":
                    break
                elif tipo_problemas == "5":
                    print()
                    print("Agradecemos por utilizar nosso sistema de ajuda!")
                    raise SystemExit
                else:
                    print()
                    print("Opção inválida. Por favor, selecione uma opção válida.")

        elif escolha_usuario == "5":
            while True:
                print()
                tipo_problemas = input("Selecione uma opção:\n\n"
                                    "1 - Verificar se há danos visíveis no veículo\n"
                                    "2 - Atolamento\n"
                                    "3 - Tomar medidas de segurança para evitar futuros danos\n"
                                    "4 - retornar para página anterior\n"
                                    "5 - Encerrar atendimento\n\n")
                if tipo_problemas == "1":
                    print()
                    print("Estamos a seu caminho para que possamos verificar se há danos visíveis no veículo e realizar os reparos necessários.\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "2":
                    print()
                    if tipo_veiculo == "grande porte":    
                        print("Estamos encaminhando a sua localização um guincho para veículos de grande porte, "
                              "para que possamos desatolar e caso necessário levar o seu veículo a um mecânico especializado para diagnosticar e reparar " 
                              "caso há problemas com seu veículo.\n")
                    else:
                        print("Estamos encaminhando a sua localização um guincho para veículos de pequeno/médio porte, "
                              "para que possamos desatolar e caso necessário levar o seu veículo a um mecânico especializado para diagnosticar e reparar " 
                              "caso há problemas com seu veículo.\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "3":
                    print()
                    print("Te recomendamos verificar os pneus, os lipadores para-brisa com frenquência, manter a lataria em bom estado, "
                          "e manter um kit de emergência dentro do veículo.\n"
                          "Caso precise de auxilio traga seu veículo em uma de nossas concessionárias para tomarmos as melhores decisões.\n")
                    escolha_usuario_encerramento()
                elif tipo_problemas == "4":
                    break
                elif tipo_problemas == "5":
                    print()
                    print("Agradecemos por utilizar nosso sistema de ajuda!")
                    raise SystemExit
                else:
                    print()
                    print("Opção inválida. Por favor, selecione uma opção válida.")

        elif escolha_usuario == "6":
            print()
            print("Agradecemos por utilizar nosso sistema de ajuda!")
            raise SystemExit 

        else:
            print()
            print("Opção inválida. Por favor, selecione uma opção válida.")

realizar_login()
lidar_com_problemas()