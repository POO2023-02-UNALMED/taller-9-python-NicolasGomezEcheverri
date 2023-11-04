from tkinter import Tk, Button, Entry, END

numeros = []
operadores = []
ultimo_fue_operador = False

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("290x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)


def calcular_resultado():
    global ultimo_fue_operador
    global numeros
    global operadores

    if len(operadores) + 1 != len(numeros):
        return

    resultado = 0.0

    operadores_multiplicacion_division = ["*", "/"]

    while len(operadores) > 0:
        index = 0
        while index < len(operadores):
            operador = operadores[index]
            if operador in operadores_multiplicacion_division:
                num1 = float(numeros[index])
                num2 = float(numeros[index + 1])

                operadores.pop(index)
                numeros.pop(index)

                if operador == "*":
                    resultado = num1 * num2
                elif operador == "/":
                    resultado = num1 / num2
                elif operador == "+":
                    resultado = num1 + num2
                elif operador == "-":
                    resultado = num1 - num2

                numeros[index] = str(resultado)
                index = 0
            else:
                index += 1
        if operadores == operadores_multiplicacion_division and len(list(filter(lambda op: op in operadores_multiplicacion_division, operadores))) == 0:
            operadores_multiplicacion_division = ["+", "-"]

    numeros = [str(resultado)]
    operadores = []
    pantalla.delete(0, END)
    pantalla.insert("end", str(resultado))


def manejar_click(texto):
    global ultimo_fue_operador
    global numeros
    global operadores

    if texto == "=":
        calcular_resultado()
        return

    pantalla.insert("end", texto)
    if texto in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        if ultimo_fue_operador or len(numeros) == 0:
            numeros.append(texto)
        else:
            numeros[-1] += texto
        ultimo_fue_operador = False
    else:
        if ultimo_fue_operador:
            operadores[-1] = texto
            longitud = len(pantalla.get())
            pantalla.delete(longitud - 2, longitud - 1)
        else:
            operadores.append(texto)
        ultimo_fue_operador = True

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: manejar_click("1")).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: manejar_click("2")).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: manejar_click("3")).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: manejar_click("4")).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: manejar_click("5")).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: manejar_click("6")).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: manejar_click("7")).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: manejar_click("8")).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: manejar_click("9")).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=lambda: manejar_click("=")).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: manejar_click(".")).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: manejar_click("+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: manejar_click("-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: manejar_click("*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: manejar_click("/")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()