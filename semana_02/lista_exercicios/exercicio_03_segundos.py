def main():

	total_segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

	segundos = total_segundos

	horas = segundos // 3600

	dias = horas // 24
	horas = horas % 24

	segundos = segundos % 3600

	minutos = segundos // 60
	segundos = segundos % 60


	print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")

main()