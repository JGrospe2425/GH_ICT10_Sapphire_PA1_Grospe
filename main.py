from pyscript import display, document

def compute(e):
    document.getElementById('output').innerHTML = ''
    fahrenheit = float(document.getElementById("input1").value)

    celsius = (fahrenheit - 32) * 5 / 9

    display(f"Temperature in Celsius: {float(celsius):.2f}", target="output")

    if celsius >= 37.8:
        display("You have a fever", target="output")
    else:
        display("Your temperature is normal", target="output")
