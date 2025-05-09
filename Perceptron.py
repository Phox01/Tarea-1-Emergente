import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

##Functions
def createInputsByUser():
    global inputList

    messagebox.showinfo(
        "Alerta",
        "Ingresa tu input separados por una coma.\nEjemplo: 4.5,6.7,8.8\nLa cantidad de valores debe coincidir con el tamaño del vector de pesos."
    )

    inputValuesFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=1)

    valueInput = tk.Entry(inputValuesFrame)
    valueInput.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    submitButton = tk.Button(inputValuesFrame, text="Guardar Input", command=lambda:processInput(valueInput))
    submitButton.pack(side=tk.TOP, padx=5, pady=5)

def processInput(valueInput):
        global inputList
        raw_input = valueInput.get()
        try:
            input_vector = [float(x.strip()) for x in raw_input.split(",")]
            if len(input_vector) != weightVector.size:
                raise ValueError("Número de valores no coincide con el tamaño del vector de pesos.")
            inputList = [np.array(input_vector)]
            messagebox.showinfo("Éxito", "Vector ingresado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

def openFile():
    filePath = filedialog.askopenfilename(
    title="Open Text File",
    filetypes=[("Text Files", "*.txt")]
    )
    if filePath:
        with open(filePath, "r") as file:
            content = file.read()
    return content

def sigmoid(x):
    return 1 / (1 + np.exp(-x))



def loadInputValues(weightSize):
    messagebox.showinfo("Archivo", "Ingresa tu archivo con los inputs para continuar")
    global inputList

    while inputList == [] or verifysizeList(inputList, weightSize):
        try:
            rawData = openFile() 
            inputLines = rawData.strip().split("\n")
            inputList = []

            for line in inputLines:
                str_vector = line.strip().split(",")
                float_vector = [float(j) for j in str_vector]  
                vectorNp = np.array(float_vector)
                inputList.append(vectorNp)

        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "Recuerda que los números deben estar separados por comas y deben contener la misma cantidad de números que de pesos")

    createFrames(inputList)
    buttons.destroy()
    return inputList

def verifysizeList(inputList, weightSize): ## Función para verificar si cada vector dentro de la lista tenga 
#la misma cantidad de componentes que la matriz de peso
    value=False
    for i in inputList:
        if len(i)!=weightSize:
            value=True
    return value

def loadInitialValues():
    messagebox.showinfo("Archivo", "Ingresa tu archivo con los parámetros para continuar")
    weightList=[]
    bias=0
    while(weightList==[] or bias==0):
            try:
                 
                configNumbers=openFile().strip().split(",")
                bias=float(configNumbers[0])
                for i in range(1, len(configNumbers)):
                    weightList.append(float(configNumbers[i]))
                weightVector=np.array(weightList)
            except Exception as e:
                messagebox.showerror("Error", "Recuerda que los números deben estar separados por comas y debe contener el bias y los parámetros")
    return bias, weightVector

def createResults(inputs, weightValue, sigmoid_var, tanh_var):
    use_sigmoid = sigmoid_var.get()
    use_tanh = tanh_var.get()
    if not (use_sigmoid or use_tanh):
        messagebox.showerror("Error", "Debes seleccionar al menos una función de activación.")
        return
    
    if use_sigmoid and use_tanh:
        messagebox.showerror("Error", "No puedes seleccionar ambas funciones de activación al mismo tiempo.")
        return
    outputFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, pady=1)
    for i in inputs:
        result= calculateResult(i, weightValue, sigmoid_var, tanh_var)
        resultInput = tk.Label(outputFrame, text=f"Resultado= {result}", bg="lightgray", padx=10, pady=10)
        resultInput.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

def createFrames(inputList):
    inputValuesFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=1)

    for idx, vector in enumerate(inputList):
        valueInput = tk.Label(inputValuesFrame, text=f"Input {idx} = {vector}")
        valueInput.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

def calculateResult(inputList, weightList, use_sigmoid, use_tanh):
    use_sigmoid = sigmoid_var.get()
    use_tanh = tanh_var.get()
    dot_product = np.dot(inputList, weightList)
    result = dot_product + bias
    if use_sigmoid:
        result = sigmoid(result)
        return  result 
    elif use_tanh:
        result = np.tanh(result)
        return result

def on_calculate_button():
    use_sigmoid = sigmoid_var.get()
    use_tanh = tanh_var.get()
    if use_sigmoid and use_tanh:
        messagebox.showerror("Error", "No puedes seleccionar ambas funciones de activación al mismo tiempo.")
        return
    if not (use_sigmoid or use_tanh):
        messagebox.showerror("Error", "Debes seleccionar al menos una función de activación.")
        return

##Lo que sería el Main


info=loadInitialValues()
bias=info[0]
weightVector=info[1]
inputList=[]


# Creación de la base de la ventana
root = tk.Tk()
root.geometry("800x500")
root.title("Perceptrón")

sigmoid_var = tk.BooleanVar()
tanh_var = tk.BooleanVar()

#Acá están todos los containers
inputSection= tk.Frame(root, padx=10, pady=10)
buttons = tk.Frame(inputSection, bg="lightgray", padx=10, pady=10)
allDataFrame=tk.Frame(root, padx=10, pady=10)
valuesFrame=tk.Frame(allDataFrame, padx=10, pady=10)
outputFrame=tk.Frame(allDataFrame, padx=10, pady=10)
initialValuesFrame=tk.Frame(valuesFrame, bg="lightgray", padx=10, pady=10)
inputValuesFrame=tk.Frame(valuesFrame, bg="lightgray", padx=10, pady=10)
checkFrame=tk.Frame(root, padx=10, pady=10)

#Acá están los componentes
title= tk.Label(root, text="Perceptrón 🤖", font=("Arial", 20, "bold"), padx=10, pady=10)
titleInput=tk.Label(inputSection, text="Ingresa el método para añadir los valores de tus inputs", font=("Arial", 14), wraplength=300)
biasValueLabel = tk.Label(initialValuesFrame, text=f"Bias= {bias}")
weightsLabel = tk.Label(initialValuesFrame, text=f"Weights= {weightVector}")
txtEntry= tk.Button(buttons, text="Enter Txt", command=lambda:loadInputValues(weightVector.size))
manualEntry=tk.Button(buttons, text="Enter values", command=createInputsByUser)
resultBoton=tk.Button(root, text="Calculate", command=lambda:createResults(inputList, weightVector, sigmoid_var, tanh_var))
sigmoid_checkbox = tk.Checkbutton(checkFrame, text="Sigmoide", variable=sigmoid_var)
tanh_checkbox = tk.Checkbutton(checkFrame, text="Tanh", variable=tanh_var)
calculate_button = tk.Button(root, text="Escoger función", command=on_calculate_button)

#textWidget = tk.Text(root)


#Se inician todos los componentes
title.pack()
inputSection.pack()
titleInput.pack()
buttons.pack(pady=1)
txtEntry.pack(side="left", padx=5, pady=5)
manualEntry.pack(side="right", padx=5, pady=5)
allDataFrame.pack() 
valuesFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=1)

initialValuesFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=1)
biasValueLabel.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
weightsLabel.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
checkFrame.pack()
sigmoid_checkbox.pack(side=tk.LEFT, pady=5)
tanh_checkbox.pack(side=tk.RIGHT, pady=5)
calculate_button.pack(pady=10)
resultBoton.pack(pady=1)
#textWidget.pack()

# label = tk.Label(buttons, text="Username:")
# label.pack(side="left")

# entry = tk.Entry(buttons)
# entry.pack(side="left")

# Button that reads input






root.mainloop()