# Telstra-Cybersecurity-Virtual-Experience-Program

I participated in Telstra's Security Operations Centre as an Information Security Analyst to gain first-hand experience of the daily tasks and responsibilities of a Security Analyst at Telstra. The tasks carried out:

1. Triaged a malware attack (CVE-2022-22965) on their nbn services and respond to the malware attack by contacting the appropriate team.
2. Analyzed the data of the malware to identify how it spreads.
3. Utilize the patterns identified to formulate a firewall rule with Python programming language in order to mitigate the malware from spreading.
4. Drafted an incident postmortem of the malware attack, covering the details I picked up in the previous task.

# Firewall Rule

This is a simple Python project I was tasked to perform as a participant of Telstra Virtual Experience Program with Forage. My task was to utilize Python to develop a firewall rule to mitigate a zero-day vulnerability malware attack (CVE-2022-22965), known as Spring4Shell. Therefore, I developed a firewall rule in the firewall_server.py script provided by Telstra to mitigate the attack on their nbn services. The rule blocks:

1. Incoming traffic on client request path “/tomcatwar.jsp”
2. Any request which is used in the malicious Spring4Shell payload, as listed in this PoC: https://github.com/craig/SpringCore0day/blob/main/exp.py

## Prerequisites
- Python 3.x

## Installation and Setup
1. Clone or download the project repository to your device.
2. Open a terminal or command prompt and navigate to the project directory.

## Usage
- python firewall_server.py
- Ctrl + C to stop the server

After executing the script, the server will listen for incoming requests and any incoming GET or POST request that matches the stipulated rule above will be blocked and a 403 response code will be sent to the client. I tested the firewall_server.py script against the "test_resquests.py" script provided by Telstra.

## PoC

![image](https://github.com/bL34cHig0/Telstra-Cybersecurity-Virtual-Experience-/assets/133022207/7a0660ae-7ee0-4c2f-80be-59d9fbde457f)

## Resources

1. https://github.com/craig/SpringCore0day/blob/main/exp.py
2. https://docs.python.org/3/library/http.server.html
3. https://spring.io/security/cve-2022-22965
4. https://www.cisa.gov/news-events/alerts/2022/04/01/spring-releases-security-updates-addressing-spring4shell-and-spring

## Disclaimer
This project is for educational purpose only. Telstra, Forage, and the author are not responsible for any misuse or illicit activities performed using this code. Any 
consequences arising from the misuse or unlawful use of this project are solely the responsibility of the user.
