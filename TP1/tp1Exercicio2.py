#Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.
minutos_a_serem_convertido = int(input("Escolha um número para ser convertido: "))
minutos_para_horas = minutos_a_serem_convertido // 60
minutos_restantes = minutos_a_serem_convertido % 60
print(f"São {minutos_para_horas} hora(s) e {minutos_restantes} minuto(s)")
minutos_totais = minutos_para_horas * 60 + minutos_restantes
print("Convertendo novamente para minutos",minutos_totais, "minutos")