class ConvertidorTemperatura:
    MAX_CELCIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cls, celcius):
        if celcius > cls.MAX_CELCIUS:
            raise ValueError(f"Temperatura C demaciado alta: {celcius}")

        return celcius * 9 / 5 + 32

    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f"Temperatura F demaciado alta: {fahrenheit: .2f}")
        return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    temperatura_celcius = float(input("Ingresa temperatura en grados celcius:   "))
    temperatura_fahrenheit = float(
        input("Ingresa temperatura en grados fahrenheit:   ")
    )
    res_fahre = ConvertidorTemperatura.c_f(temperatura_celcius)
    res_cel = ConvertidorTemperatura.f_c(temperatura_fahrenheit)
    print(
        f"{temperatura_celcius} en grados celcius es igual a {res_fahre} en grados fahrenheit"
    )
    print(
        f"{temperatura_fahrenheit} en grados celcius es igual a {res_cel:.2f} en grados fahrenheit"
    )
