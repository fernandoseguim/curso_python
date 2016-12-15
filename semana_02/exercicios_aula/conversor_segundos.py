total_segundos = int(input("Entre com o número de segundos que deseja converter: "))

segundos = total_segundos

horas = segundos // 3600

dias = horas // 24
horas = horas % 24

segundos = segundos % 3600

minutos = segundos // 60
segundos = segundos % 60


print()
print(total_segundos, " equivale à ",dias, "dias", horas, "h", minutos, "min", segundos, "s")

