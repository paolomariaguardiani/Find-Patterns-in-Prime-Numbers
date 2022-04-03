#include <stdio.h>
#include <stdbool.h>

bool trova_numeri_primi(int numero) {
	bool numero_primo = false;
	if (numero == 0) {
		numero_primo == false;
	} else if (numero == 1) {
		numero_primo = true;
	}
       	if (numero == 2) {
		numero_primo = true;
	}
	for (int i = 2; i < numero; i++) {
		if (numero % i == 0) {
			numero_primo = false;
			break;
		}
		if (numero % i != 0) {
			numero_primo = true;
		}
	}
	// return numero_primo;
	return numero_primo;
}

		
// Grazie a https://www.journaldev.com/31907/calling-c-functions-from-python


