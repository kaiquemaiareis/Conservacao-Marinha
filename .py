import matplotlib.pyplot as plt

# calcula o valor total para cada area marinha
def calcular_valor(a, b, c, d):
    # o valor é uma combinação ponderada da biodiversidade, vulnerabilidade e conectividade
    return a * (0.4 * b + 0.3 * c + 0.3 * d)

# checa se o valor esta entre 0 e 10 e é um numero inteiro
def checar_entrada(valor):
    try:
        v = float(valor)
        if v < 0 or v > 10 or v % 1 != 0:
            return False
        return True
    except ValueError:
        return False

# aloca os recursos com base no valor de cada area marinha
def alocar_recursos(areas, total):
    aloc = []
    # ordena as areas do valor mais alto para o mais baixo
    ordenado = sorted(enumerate(areas), key=lambda x: calcular_valor(*x[1]), reverse=True)
    valor_total = sum(calcular_valor(*area) for _, area in ordenado)
    if valor_total == 0:
        valor_total = 1  # evita divisao por zero
    
    # distribui os recursos proporcionalmente ao valor de cada area
    for i, area in ordenado:
        area_valor = calcular_valor(*area)
        alocado = (area_valor / valor_total) * total
        aloc.append((i+1, area, alocado))

    return aloc

# plota a alocaçao de recursos para visualizaçao
def plotar_alocacao(areas, alocacao):
    nomes = [f"Área {num}" for num, _, _ in alocacao]
    recursos = [recursos for _, _, recursos in alocacao]

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(nomes)), recursos, color='red', alpha=0.5, label='Recursos')

    plt.xlabel('Áreas Marinhas')
    plt.ylabel('Recursos Alocados')
    plt.title('Visualização da Alocação de Recursos')
    plt.xticks(range(len(nomes)), nomes)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    # pede ao usuario quantas areas marinhas eles querem incluir
    while True:
        num = input("Quantas áreas marinhas você quer incluir? (máx 20): ")
        if num.isdigit() and 0 < int(num) <= 20:
            num = int(num)
            break
        print("Número inválido. Tente de novo.")

    areas = []
    for i in range(num):
        print(f"\nÁrea {i+1}:")
        
        # pede e valida a area em km2
        while True:
            area = input("Área em km2 (máx 500000): ")
            if area.isdigit() and 0 < int(area) <= 500000:
                area = float(area)
                break
            print("Valor inválido. Insira um valor entre 1 e 500000.")

        # pede e valida a biodiversidade
        while True:
            bio = input("Biodiversidade (0-10): ")
            if checar_entrada(bio):
                bio = float(bio)
                break
            print("Valor inválido. Insira um valor entre 0 e 10.")

        # pede e valida a vulnerabilidade
        while True:
            vuln = input("Vulnerabilidade (0-10): ")
            if checar_entrada(vuln):
                vuln = float(vuln)
                break
            print("Valor inválido. Insira um valor entre 0 e 10.")

        # pede e valida a conectividade
        while True:
            conect = input("Conectividade (0-10): ")
            if checar_entrada(conect):
                conect = float(conect)
                break
            print("Valor inválido. Insira um valor entre 0 e 10.")

        areas.append((area, bio, vuln, conect))

    # eede e valida os recursos totais disponiveis
    while True:
        recursos = input("Quantos recursos você tem para alocar? (máx 999000000): ")
        if recursos.isdigit() and 0 < int(recursos) <= 999000000:
            recursos = float(recursos)
            break
        print("Valor inválido. Insira um valor entre 1 e 999000000.")

    # calcula a alocaçao dos recursos
    aloc = alocar_recursos(areas, recursos)

    print("\nAqui está a alocação de recursos:")
    for num, area, rec in aloc:
        # mostra quanto foi alocado para cada area marinha
        print(f"Área Marinha {num}: {area}, Recursos Alocados: {rec}")

    # mostra o grafico com a alocaçao de recursos
    plotar_alocacao(areas, aloc)

if __name__ == "__main__":
    main()

