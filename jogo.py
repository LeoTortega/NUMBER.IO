import random


def introducao():
    print("""    ....................................................................................................
    .....,+++...:++:.:++;...;++,.;+++:..:+++;,,+++++++:..,++++++++,.+++++++;.......,+++,...,;++;,.......
    .....:000+..?00*.*00%..,#00;.S000%..?000S,:00000000+.:00000000;,#0000000?,.....:000:..+#0000#*,.....
    .....:000#:.*00*.*00?..,S00;.%000#,,S000S,:000##000S,,#00#####:,#000##000;.....:00#:.;000##000*.....
    .....:0000%.*00*.*00?..,S00;.%00#0;:0##0S,:00#:,*00S,,#00:,,,,.,#00;,:#00+.....:00#:,S00?,,*00#,....
    .....:00000+*00*.*00?..,S00;.%0SS0*+0SS0S,:000##00#:.:#00####%.,#00###00#:.....:00#,:#0#:..,#00:....
    .....:00SS0#%00*.*00?..,S00;.%0S*0S%0?%0S,:0000000#+.,#000000S.,#000000S;......:00#,:00#,..,S00;....
    .....:00%;00000*.*00?...S00;.%0S;0000;%0S,:000*+*000;,#00*+++;.,#00?S00%,......:000,:#0#:..,#00:....
    .....:00%.*0000*.;00#:.;000:.%0S,S00#,%0S,:00#,.,S00+,#00,.....,#00:,#00?.,+*+,:000:,S00*,.*00#,....
    .....:00S.,S000*.,#000#000%,,%0S,?00%.%0S,:000###000;,#00#####;,#00;.*000:,#0#,,00#:.+000##000*.....
    .....;00S..:000*..;S00000%,.,S0#,+00*.S0S,:00000000?.,00000000+,#00;.,S00%:#0#,,000:..*#0000#*,.....
    .....,**+...;**;...,;***;....+*+.,**:.+*+.,******+:..,+*******:.+**,..:***,+*+,,***,...,+**+,.......
    ....................................................................................................

    """)

    print("##########################################################################################################\n"
          "\nNUMBER.IO é um jogo onde a máquina vai escolher um numero aleatório de 4 digitos e o usuário vai ter que"
          "\nacertar o mesmo na menor quantidade de tentativas. Quando receber um V na saída, significa que digitou"
          "\no numero certo na posição certa, Q é para número certo na posição errada e F é para número errado.\n")

    print(
        "##########################################################################################################\n")


def gerador():
    numero = random.randint(0, 9999)

    return numero


def input_user():
    numerocorreto = False

    while not numerocorreto:
        try:
            numuser = int(input(f"Digite um número de 4 digitos: "))
        except ValueError:
            print("Digite apenas números...")
            continue
        if numuser <= 9999:
            numerocorreto = True
        else:
            print(f"O número tem que ter apenas 4 digitos...")
            continue
        return numuser


def inserir_array(num):
    numeroarray = []
    for i in range(len(str(num))):
        numeroarray.append(num % 10)
        num = int((num - (num % 10)) / 10)

    return numeroarray


introducao()

pcnum = gerador()
pcnumarray = inserir_array(pcnum)

verificador = False
tentativas = 1

while not verificador:
    numuser = input_user()
    arrayuser = inserir_array(numuser)
    while len(arrayuser) <= 3:
        arrayuser.append(0)
    for i in range(3, -1, -1):
        if arrayuser[i] == pcnumarray[i]:
            print("V", end="")
        elif arrayuser[i] == pcnumarray[0] or arrayuser[i] == pcnumarray[1] or arrayuser[i] == pcnumarray[2] or \
                arrayuser[i] == pcnumarray[3]:
            print("Q", end="")
        else:
            print("F", end="")
    if pcnum == numuser:
        if tentativas == 1:
            print(f"\nParabéns, você acertou de primeira")
            verificador = True
        else:
            print(f"\nParabéns, você acertou o numero com {tentativas} tentativas")
            verificador = True
    else:
        print("\nNúmero errado, tente novamente\n")
        print(
            "##########################################################################################################"
            "\n")
        tentativas += 1
