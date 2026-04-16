# Password-Brute-Force-Simulator
This project is a Python-based simulation of a brute force password attack.
#  Password Cracker (Brute Force Simulator)

##  Description

This project is a Python-based simulation of a brute force password attack. It demonstrates how weak passwords can be cracked using a dictionary of common passwords.

The tool iterates through a list of possible passwords (wordlist) and compares each attempt against a target password until a match is found.

---

##  Features

* Simulates a brute force / dictionary attack
* Attempts passwords sequentially
* Stops when the correct password is found
* Displays number of attempts
* Simple and easy-to-understand logic

---

##  Technologies Used

* Python
* Basic control structures (loops, conditions)

---

##  Usage

Run the program:

```bash
python main.py
```

---

## 📊 Example Output

```
 Starting brute force attack...

Trying password 1: 123456
Trying password 2: password
Trying password 3: admin
Trying password 4: admin123

 Password FOUND!
 Password is: admin123
Attempts: 4
```

---

##  What I Learned

* How brute force attacks work
* Difference between weak and strong passwords
* Basics of authentication security
* Importance of password complexity
* How attackers use dictionary-based attacks

---

##  Disclaimer

This project is for educational purposes only. It simulates password cracking in a controlled environment and should not be used against real systems without authorization.

---

##  Real-World Application

This project demonstrates how attackers attempt to break into systems using weak passwords. It highlights the importance of:

* Strong passwords
* Account lockout mechanisms
* Multi-factor authentication (MFA)

---

##  Future Improvements

* Load passwords from external wordlist file
* Add delay to simulate real attack timing
* Implement login system simulation
* Add multi-threading for faster attacks
