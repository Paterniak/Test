#!/usr/bin/env python3
import socket
import math
import re

def main():
    host = "challenge01.root-me.org"
    port = 52002

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print("Połączono z serwerem")

            data = s.recv(1024).decode('utf-8')
            print("Otrzymane dane:", data.strip())

            # Regular expression to match the math operation in the received data
            match = re.search(r"Calculate the square root of (\d+) and multiply by (\d+) =", data)
            if not match:
                print("Nie znaleziono odpowiednich danych")
                return

            # Extracting the numbers from the match groups
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            print(f"Liczby: {num1} i {num2}")

            # Performing the calculation
            sqrt_num1 = math.sqrt(num1)
            result = sqrt_num1 * num2
            rounded_result = round(result, 2)

            # Sending the result back to the server
            response = f"{rounded_result}\n"
            s.sendall(response.encode('utf-8'))
            print("Wysłano wiadomość")

            # Receiving the final response from the server
            final_response = s.recv(1024).decode('utf-8')
            print("Odpowiedź serwera:", final_response.strip())

    except Exception as e:
        print(f"Blad: {e}")

if __name__ == "__main__":
    main()
